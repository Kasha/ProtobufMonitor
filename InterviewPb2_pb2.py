# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InterviewPb2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='InterviewPb2.proto',
  package='interview',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12InterviewPb2.proto\x12\tinterview\"7\n\tDetection\x12\x0b\n\x03lat\x18\x01 \x02(\x02\x12\x0b\n\x03lon\x18\x02 \x02(\x02\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02'
)




_DETECTION = _descriptor.Descriptor(
  name='Detection',
  full_name='interview.Detection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='interview.Detection.lat', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lon', full_name='interview.Detection.lon', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='interview.Detection.distance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['Detection'] = _DETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Detection = _reflection.GeneratedProtocolMessageType('Detection', (_message.Message,), {
  'DESCRIPTOR' : _DETECTION,
  '__module__' : 'InterviewPb2_pb2'
  # @@protoc_insertion_point(class_scope:interview.Detection)
  })
_sym_db.RegisterMessage(Detection)


# @@protoc_insertion_point(module_scope)
