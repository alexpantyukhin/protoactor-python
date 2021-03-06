from protoactor.messages import SystemMessage
from protoactor.utils import singleton


@singleton
class SuspendMailbox(SystemMessage):
    pass


@singleton
class ResumeMailbox(SystemMessage):
    pass
