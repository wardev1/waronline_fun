# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ClusterProp.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ClusterProp.proto',
  package='login.proto',
  serialized_pb='\n\x11\x43lusterProp.proto\x12\x0blogin.proto\"4\n\x0b\x43lusterProp\x12\x11\n\tprop_name\x18\x01 \x02(\t\x12\x12\n\nprop_value\x18\x02 \x02(\t')




_CLUSTERPROP = _descriptor.Descriptor(
  name='ClusterProp',
  full_name='login.proto.ClusterProp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prop_name', full_name='login.proto.ClusterProp.prop_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prop_value', full_name='login.proto.ClusterProp.prop_value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=34,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['ClusterProp'] = _CLUSTERPROP

class ClusterProp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUSTERPROP

  # @@protoc_insertion_point(class_scope:login.proto.ClusterProp)


# @@protoc_insertion_point(module_scope)
