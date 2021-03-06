# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos_remote.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protos_pb2 as protos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos_remote.proto',
  package='remote',
  syntax='proto3',
  serialized_pb=_b('\n\x13protos_remote.proto\x12\x06remote\x1a\x0cprotos.proto\"d\n\x0cMessageBatch\x12\x12\n\ntype_names\x18\x01 \x03(\t\x12\x14\n\x0ctarget_names\x18\x02 \x03(\t\x12*\n\tenvelopes\x18\x03 \x03(\x0b\x32\x17.remote.MessageEnvelope\"\xaa\x01\n\x0fMessageEnvelope\x12\x0f\n\x07type_id\x18\x01 \x01(\x05\x12\x14\n\x0cmessage_data\x18\x02 \x01(\x0c\x12\x0e\n\x06target\x18\x03 \x01(\x05\x12\x1a\n\x06sender\x18\x04 \x01(\x0b\x32\n.actor.PID\x12\x15\n\rserializer_id\x18\x05 \x01(\x05\x12-\n\x0emessage_header\x18\x06 \x01(\x0b\x32\x15.remote.MessageHeader\"~\n\rMessageHeader\x12:\n\x0bheader_data\x18\x01 \x03(\x0b\x32%.remote.MessageHeader.HeaderDataEntry\x1a\x31\n\x0fHeaderDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x0f\x41\x63torPidRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\"@\n\x10\x41\x63torPidResponse\x12\x17\n\x03pid\x18\x01 \x01(\x0b\x32\n.actor.PID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\"\x06\n\x04Unit\"\x10\n\x0e\x43onnectRequest\"0\n\x0f\x43onnectResponse\x12\x1d\n\x15\x64\x65\x66\x61ult_serializer_id\x18\x01 \x01(\x05\x32}\n\x08Remoting\x12<\n\x07\x43onnect\x12\x16.remote.ConnectRequest\x1a\x17.remote.ConnectResponse\"\x00\x12\x33\n\x07Receive\x12\x14.remote.MessageBatch\x1a\x0c.remote.Unit\"\x00(\x01\x30\x01\x42\x0f\xaa\x02\x0cProto.Remoteb\x06proto3')
  ,
  dependencies=[protos__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MESSAGEBATCH = _descriptor.Descriptor(
  name='MessageBatch',
  full_name='remote.MessageBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_names', full_name='remote.MessageBatch.type_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_names', full_name='remote.MessageBatch.target_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='envelopes', full_name='remote.MessageBatch.envelopes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=145,
)


_MESSAGEENVELOPE = _descriptor.Descriptor(
  name='MessageEnvelope',
  full_name='remote.MessageEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_id', full_name='remote.MessageEnvelope.type_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_data', full_name='remote.MessageEnvelope.message_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='remote.MessageEnvelope.target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='remote.MessageEnvelope.sender', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serializer_id', full_name='remote.MessageEnvelope.serializer_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_header', full_name='remote.MessageEnvelope.message_header', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=318,
)


_MESSAGEHEADER_HEADERDATAENTRY = _descriptor.Descriptor(
  name='HeaderDataEntry',
  full_name='remote.MessageHeader.HeaderDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='remote.MessageHeader.HeaderDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='remote.MessageHeader.HeaderDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=446,
)

_MESSAGEHEADER = _descriptor.Descriptor(
  name='MessageHeader',
  full_name='remote.MessageHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_data', full_name='remote.MessageHeader.header_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGEHEADER_HEADERDATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=446,
)


_ACTORPIDREQUEST = _descriptor.Descriptor(
  name='ActorPidRequest',
  full_name='remote.ActorPidRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='remote.ActorPidRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kind', full_name='remote.ActorPidRequest.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=493,
)


_ACTORPIDRESPONSE = _descriptor.Descriptor(
  name='ActorPidResponse',
  full_name='remote.ActorPidResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='remote.ActorPidResponse.pid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='remote.ActorPidResponse.status_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=559,
)


_UNIT = _descriptor.Descriptor(
  name='Unit',
  full_name='remote.Unit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=567,
)


_CONNECTREQUEST = _descriptor.Descriptor(
  name='ConnectRequest',
  full_name='remote.ConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=585,
)


_CONNECTRESPONSE = _descriptor.Descriptor(
  name='ConnectResponse',
  full_name='remote.ConnectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_serializer_id', full_name='remote.ConnectResponse.default_serializer_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=635,
)

_MESSAGEBATCH.fields_by_name['envelopes'].message_type = _MESSAGEENVELOPE
_MESSAGEENVELOPE.fields_by_name['sender'].message_type = protos__pb2._PID
_MESSAGEENVELOPE.fields_by_name['message_header'].message_type = _MESSAGEHEADER
_MESSAGEHEADER_HEADERDATAENTRY.containing_type = _MESSAGEHEADER
_MESSAGEHEADER.fields_by_name['header_data'].message_type = _MESSAGEHEADER_HEADERDATAENTRY
_ACTORPIDRESPONSE.fields_by_name['pid'].message_type = protos__pb2._PID
DESCRIPTOR.message_types_by_name['MessageBatch'] = _MESSAGEBATCH
DESCRIPTOR.message_types_by_name['MessageEnvelope'] = _MESSAGEENVELOPE
DESCRIPTOR.message_types_by_name['MessageHeader'] = _MESSAGEHEADER
DESCRIPTOR.message_types_by_name['ActorPidRequest'] = _ACTORPIDREQUEST
DESCRIPTOR.message_types_by_name['ActorPidResponse'] = _ACTORPIDRESPONSE
DESCRIPTOR.message_types_by_name['Unit'] = _UNIT
DESCRIPTOR.message_types_by_name['ConnectRequest'] = _CONNECTREQUEST
DESCRIPTOR.message_types_by_name['ConnectResponse'] = _CONNECTRESPONSE

MessageBatch = _reflection.GeneratedProtocolMessageType('MessageBatch', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEBATCH,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.MessageBatch)
  ))
_sym_db.RegisterMessage(MessageBatch)

MessageEnvelope = _reflection.GeneratedProtocolMessageType('MessageEnvelope', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEENVELOPE,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.MessageEnvelope)
  ))
_sym_db.RegisterMessage(MessageEnvelope)

MessageHeader = _reflection.GeneratedProtocolMessageType('MessageHeader', (_message.Message,), dict(

  HeaderDataEntry = _reflection.GeneratedProtocolMessageType('HeaderDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGEHEADER_HEADERDATAENTRY,
    __module__ = 'protos_remote_pb2'
    # @@protoc_insertion_point(class_scope:remote.MessageHeader.HeaderDataEntry)
    ))
  ,
  DESCRIPTOR = _MESSAGEHEADER,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.MessageHeader)
  ))
_sym_db.RegisterMessage(MessageHeader)
_sym_db.RegisterMessage(MessageHeader.HeaderDataEntry)

ActorPidRequest = _reflection.GeneratedProtocolMessageType('ActorPidRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACTORPIDREQUEST,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.ActorPidRequest)
  ))
_sym_db.RegisterMessage(ActorPidRequest)

ActorPidResponse = _reflection.GeneratedProtocolMessageType('ActorPidResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACTORPIDRESPONSE,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.ActorPidResponse)
  ))
_sym_db.RegisterMessage(ActorPidResponse)

Unit = _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), dict(
  DESCRIPTOR = _UNIT,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.Unit)
  ))
_sym_db.RegisterMessage(Unit)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREQUEST,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.ConnectRequest)
  ))
_sym_db.RegisterMessage(ConnectRequest)

ConnectResponse = _reflection.GeneratedProtocolMessageType('ConnectResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTRESPONSE,
  __module__ = 'protos_remote_pb2'
  # @@protoc_insertion_point(class_scope:remote.ConnectResponse)
  ))
_sym_db.RegisterMessage(ConnectResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\014Proto.Remote'))
_MESSAGEHEADER_HEADERDATAENTRY.has_options = True
_MESSAGEHEADER_HEADERDATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class RemotingStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Connect = channel.unary_unary(
          '/remote.Remoting/Connect',
          request_serializer=ConnectRequest.SerializeToString,
          response_deserializer=ConnectResponse.FromString,
          )
      self.Receive = channel.stream_stream(
          '/remote.Remoting/Receive',
          request_serializer=MessageBatch.SerializeToString,
          response_deserializer=Unit.FromString,
          )


  class RemotingServicer(object):

    def Connect(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Receive(self, request_iterator, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_RemotingServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Connect': grpc.unary_unary_rpc_method_handler(
            servicer.Connect,
            request_deserializer=ConnectRequest.FromString,
            response_serializer=ConnectResponse.SerializeToString,
        ),
        'Receive': grpc.stream_stream_rpc_method_handler(
            servicer.Receive,
            request_deserializer=MessageBatch.FromString,
            response_serializer=Unit.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'remote.Remoting', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaRemotingServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Connect(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Receive(self, request_iterator, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaRemotingStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Connect(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Connect.future = None
    def Receive(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()


  def beta_create_Remoting_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('remote.Remoting', 'Connect'): ConnectRequest.FromString,
      ('remote.Remoting', 'Receive'): MessageBatch.FromString,
    }
    response_serializers = {
      ('remote.Remoting', 'Connect'): ConnectResponse.SerializeToString,
      ('remote.Remoting', 'Receive'): Unit.SerializeToString,
    }
    method_implementations = {
      ('remote.Remoting', 'Connect'): face_utilities.unary_unary_inline(servicer.Connect),
      ('remote.Remoting', 'Receive'): face_utilities.stream_stream_inline(servicer.Receive),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Remoting_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('remote.Remoting', 'Connect'): ConnectRequest.SerializeToString,
      ('remote.Remoting', 'Receive'): MessageBatch.SerializeToString,
    }
    response_deserializers = {
      ('remote.Remoting', 'Connect'): ConnectResponse.FromString,
      ('remote.Remoting', 'Receive'): Unit.FromString,
    }
    cardinalities = {
      'Connect': cardinality.Cardinality.UNARY_UNARY,
      'Receive': cardinality.Cardinality.STREAM_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'remote.Remoting', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
