from abc import ABCMeta, abstractmethod
from asyncio import Task
from datetime import timedelta
from typing import Callable, Set, List
import threading

from protoactor.mailbox.messages import ResumeMailbox

from . import invoker, messages, restart_statistics
from .mailbox import messages as mailbox_msg
from .protos_pb2 import PID
from .process_registry import ProcessRegistry
from .messages import Continuation, Restart, Stop
from .supervision import Supervisor


class AbstractContext(metaclass=ABCMeta):
    def __init__(self):
        self._sender = None
        self._message = None
        self._receive_timeout = None
        self._actor = None
        self._my_self = None
        self._parent = None

    @property
    def parent(self) -> PID:
        return self._parent

    @property
    def my_self(self) -> PID:
        return self._my_self

    @property
    def sender(self) -> PID:
        return self._sender

    @property
    def actor(self) -> 'Actor':
        return self._actor

    @property
    def message(self) -> object:
        return self._message

    @property
    def receive_timeout(self) -> timedelta:
        return self._receive_timeout

    @property
    @abstractmethod
    def children(self):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def respond(self, message: object):
        raise NotImplementedError("Should Implement this method")

    @property
    @abstractmethod
    def stash(self):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def spawn(self, props: 'Props') -> PID:
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def spawn_prefix(self, props: 'Props', prefix: str) -> PID:
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def spawn_named(self, props: 'Props', name: str) -> PID:
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def watch(self, pid: PID):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def unwatch(self, pid: PID):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def set_receive_timeout(self, receive_timeout: timedelta) -> None:
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def cancel_receive_timeout(self) -> None:
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def _incarnate_actor(self):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def tell(self, target: PID, message: object):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def request(self, target: PID, message: object):
        raise NotImplementedError("Should Implement this method")

    @abstractmethod
    def reenter_after(self, target: Task, action: Callable):
        raise NotImplementedError("Should Implement this method")


class MessageEnvelope:
    def __init__(self, message: object, pid: PID, header: object):
        self.__message = message
        self.__pid = pid
        self.__header = header


class LocalContext(AbstractContext, invoker.AbstractInvoker, Supervisor):
    def __init__(self, producer: Callable[[], 'Actor'], supervisor_strategy, middleware, parent: PID) -> None:
        super().__init__()
        self.__producer = producer
        self.__supervisor_strategy = supervisor_strategy
        self.__middleware = middleware
        self._parent = parent

        self.__stopping = False
        self.__restarting = False
        self.__receive = None
        self.__restart_statistics = None

        self._receive_timeout = timedelta(milliseconds=0)

        self.__behaviour = []
        self._incarnate_actor()
        self.__timer = None
        self.__stack = []
        self.__children = set()

    def watch(self, pid: PID):
        raise NotImplementedError("Should Implement this method")

    def unwatch(self, pid: PID):
        raise NotImplementedError("Should Implement this method")

    def spawn(self, props: 'Props') -> PID:
        p_id = ProcessRegistry().next_id()
        return self.spawn_named(props, p_id)

    def set_behavior(self, receive: Callable[['Actor', AbstractContext], Task]):
        self.__behaviour.clear()
        self.__behaviour.append(receive)
        self.__receive = receive

    def respond(self, message: object):
        # TODO: implement sender
        self.sender.tell(message)

    def spawn_named(self, props: 'Props', name: str) -> PID:
        # TODO: check for guardian

        pid = props.spawn('{0}/{1}'.format(self.my_self, name), self.my_self)
        self.__children.add(pid)
        return pid

    def spawn_prefix(self, props: 'Props', prefix: str) -> PID:
        p_id = prefix + ProcessRegistry().next_id()
        return self.spawn_named(props, p_id)

    def stash(self):
        self.__stack.append(self.message)

    @property
    def children(self) -> Set[PID]:
        return self.__children

    @property
    def watchers(self) -> Set[PID]:
        raise NotImplementedError("Should Implement this method")

    @property
    def watching(self) -> Set[PID]:
        raise NotImplementedError("Should Implement this method")

    def tell(self, target: PID, message: object):
        self.__send_user_message(target, message)

    def request(self, target: PID, message: object):
        message_envelope = MessageEnvelope(message, self.my_self, None)
        self.__send_user_message(target, message_envelope)

    def set_receive_timeout(self, receive_timeout: timedelta) -> None:
        if receive_timeout == self.receive_timeout:
            return None

        self.__stop_receive_timeout()
        self._receive_timeout = receive_timeout

        if self.__timer is None:
            self.__timer = threading.Timer(self.__get_receive_timeout_seconds(), self._receive_timeout_callback)
        else:
            self.reset_receive_timeout()

    def _incarnate_actor(self):
        self.__restarting = False
        self.__stopping = False
        self.actor = self.__producer()
        self.set_behavior(self.actor.receive)

    def __get_receive_timeout_seconds(self):
        return self.receive_timeout.total_seconds()

    def resume_children(self, *pids: List['PID']) -> None:
        process_registry = ProcessRegistry()
        for pid in pids:
            reff = process_registry.get(pid)
            reff.send_system_message(self.my_self, ResumeMailbox())

    def stop_children(self, *pids: List['PID']) -> None:
        process_registry = ProcessRegistry()
        for pid in pids:
            reff = process_registry.get(pid)
            reff.send_system_message(self.my_self, Stop())

    def restart_children(self, reason: Exception, *pids: List['PID']) -> None:
        process_registry = ProcessRegistry()
        for pid in pids:
            reff = process_registry.get(pid)
            reff.send_system_message(self.my_self, Restart(reason))

    # invoker.AbstractInvoker Methods
    async def invoke_system_message(self, message: object) -> None:
        try:
            if isinstance(message, messages.Started):
                await self.invoke_user_message(message)
            elif isinstance(message, messages.Stop):
                await self.__handle_stop()
            elif isinstance(message, messages.Terminated):
                await self.__handle_terminated()
            elif isinstance(message, messages.Watch):
                await self.__handle_watch(message)
            elif isinstance(message, messages.Unwatch):
                await self.__handle_unwatch(message)
            elif isinstance(message, messages.Failure):
                await self.__handle_failure(message)
            elif isinstance(message, messages.Restart):
                await self.handle_restart()
            elif isinstance(message, mailbox_msg.SuspendMailbox):
                pass
            elif isinstance(message, mailbox_msg.ResumeMailbox):
                pass
            else:
                pass

        except Exception as e:
            self.escalate_failure(e, message)

    def __send_user_message(self, target, message):
        # TODO: check for middleware

        target.tell(message)

    async def invoke_user_message(self, message: object) -> None:
        influence_timeout = True
        if self.receive_timeout > timedelta(milliseconds=0):
            influence_timeout = not isinstance(message, messages.NotInfluenceReceiveTimeout)
            if influence_timeout is True:
                self.__stop_receive_timeout()

        await self._process_message(message)

        if self.receive_timeout > timedelta(milliseconds=0) and influence_timeout is True:
            self.reset_receive_timeout()

    def escalate_failure(self, reason: Exception, message: object) -> None:
        if not self.__restart_statistics:
            self.__restart_statistics = restart_statistics.RestartStatistics(1, None)

    async def __handle_stop(self):
        self.__restarting = False
        self.__stopping = True
        await self.invoke_user_message(messages.Stopping())
        if self.children:
            for child in self.children:
                child.stop()

        await self.__try_restart_or_terminate()

    async def __handle_terminated(self, message: object):
        self.children.remove(message.who)
        self.watching.remove(message.who)
        await self.invoke_user_message(message)
        await self.__try_restart_or_terminate()

    async def __handle_watch(self, message: object):
        if self.watchers is None:
            self.watchers = Set()
        self.watchers.add(message)

    async def __handle_unwatch(self, message: object):
        if self.watchers is not None:
            self.watchers.remove(message)

    async def __handle_failure(self, message: object):
        raise NotImplementedError("Should Implement this method")

    async def handle_restart(self):
        raise NotImplementedError("Should Implement this method")

    def __try_restart_or_terminate(self):
        raise NotImplementedError("Should Implement this method")

    def __stop_receive_timeout(self):
        self.__timer.cancel()

    def reset_receive_timeout(self):
        self.__timer.cancel()
        self.__timer = threading.Timer(self.__timer.interval, self.__timer.function)
        self.__timer.start()

    def cancel_receive_timeout(self):
        if self.__timer is None:
            return

        self.__stop_receive_timeout()
        self.__timer = None
        self._receive_timeout = None

    def reenter_after(self, target: Task, action: Callable):
        msg = self._message

        def act():
            action()
            return None

        cont = Continuation(act, msg)

        target.add_done_callback(lambda _: self.my_self.send_system_message(cont))

    def _receive_timeout_callback(self):
        if self.__timer is None:
            return

        self._cancel_receive_timeout()
        # TODO: Self.Request(Proto.ReceiveTimeout.Instance, null); from the .Net implemenation

    async def _process_message(self, message: object) -> None:
        self._message = message

        if self.__middleware is not None:
            await self.__middleware(self)
        elif isinstance(message, messages.PoisonPill) is True:
            self.my_self.stop()
        else:
            await self.__receive(self)

        self._message = None
