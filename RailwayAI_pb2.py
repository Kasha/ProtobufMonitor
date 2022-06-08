# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RailwayAI.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timestamp_pb2 as timestamp__pb2
import Common_pb2 as Common__pb2
import DataStructure_pb2 as DataStructure__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RailwayAI.proto',
  package='Seefar.Interfaces.AI',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fRailwayAI.proto\x12\x14Seefar.Interfaces.AI\x1a\x0ftimestamp.proto\x1a\x0c\x43ommon.proto\x1a\x13\x44\x61taStructure.proto\"{\n\x12\x41iRailwayUpdatedSM\x12\x13\n\x0bupdatedTilt\x18\x01 \x01(\x01\x12\x12\n\nupdatedYaw\x18\x02 \x01(\x01\x12\x1d\n\x15updatedLocationLatDeg\x18\x03 \x01(\x01\x12\x1d\n\x15updatedLocationLonDeg\x18\x04 \x01(\x01\"\x86\x02\n\x19\x41IDetectionInternalReport\x12@\n\x0f\x44\x65tectionReport\x18\x01 \x01(\x0b\x32\'.Seefar.Interfaces.AI.AIDetectionReport\x12\x35\n\x0c\x46rameGpsData\x18\x02 \x01(\x0b\x32\x1f.Seefar.Interfaces.AI.AiGpsData\x12\x33\n\x08Metadata\x18\x03 \x01(\x0b\x32!.Seefar.Interfaces.AI.AiFrameData\x12;\n\tUpdatedSM\x18\x04 \x01(\x0b\x32(.Seefar.Interfaces.AI.AiRailwayUpdatedSM\"F\n\x15\x41iRailRangeEstimation\x12\x0b\n\x03row\x18\x01 \x01(\x02\x12\x0c\n\x04\x64ist\x18\x02 \x01(\x02\x12\x12\n\nresolution\x18\x03 \x01(\x02\"\xda\x02\n\x19\x41iRailwaysDetectorMessage\x12\x33\n\x08metadata\x18\x01 \x01(\x0b\x32!.Seefar.Interfaces.AI.AiFrameData\x12\x17\n\x0fleftRailColBest\x18\x02 \x03(\x02\x12\x18\n\x10rightRailColBest\x18\x03 \x03(\x02\x12\x13\n\x0brailRowBest\x18\x04 \x03(\x02\x12=\n\ncalcMethod\x18\x05 \x01(\x0e\x32).Seefar.Interfaces.AI.AiRailwayCalcMethod\x12\x44\n\x0frangeEstimation\x18\x06 \x03(\x0b\x32+.Seefar.Interfaces.AI.AiRailRangeEstimation\x12;\n\tupdatedSM\x18\x07 \x01(\x0b\x32(.Seefar.Interfaces.AI.AiRailwayUpdatedSM*&\n\x13\x41iRailwayCalcMethod\x12\x06\n\x02\x63v\x10\x00\x12\x07\n\x03gis\x10\x01\x62\x06proto3'
  ,
  dependencies=[timestamp__pb2.DESCRIPTOR,Common__pb2.DESCRIPTOR,DataStructure__pb2.DESCRIPTOR,])

_AIRAILWAYCALCMETHOD = _descriptor.EnumDescriptor(
  name='AiRailwayCalcMethod',
  full_name='Seefar.Interfaces.AI.AiRailwayCalcMethod',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='cv', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='gis', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=904,
  serialized_end=942,
)
_sym_db.RegisterEnumDescriptor(_AIRAILWAYCALCMETHOD)

AiRailwayCalcMethod = enum_type_wrapper.EnumTypeWrapper(_AIRAILWAYCALCMETHOD)
cv = 0
gis = 1



_AIRAILWAYUPDATEDSM = _descriptor.Descriptor(
  name='AiRailwayUpdatedSM',
  full_name='Seefar.Interfaces.AI.AiRailwayUpdatedSM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='updatedTilt', full_name='Seefar.Interfaces.AI.AiRailwayUpdatedSM.updatedTilt', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updatedYaw', full_name='Seefar.Interfaces.AI.AiRailwayUpdatedSM.updatedYaw', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updatedLocationLatDeg', full_name='Seefar.Interfaces.AI.AiRailwayUpdatedSM.updatedLocationLatDeg', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updatedLocationLonDeg', full_name='Seefar.Interfaces.AI.AiRailwayUpdatedSM.updatedLocationLonDeg', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=216,
)


_AIDETECTIONINTERNALREPORT = _descriptor.Descriptor(
  name='AIDetectionInternalReport',
  full_name='Seefar.Interfaces.AI.AIDetectionInternalReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DetectionReport', full_name='Seefar.Interfaces.AI.AIDetectionInternalReport.DetectionReport', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FrameGpsData', full_name='Seefar.Interfaces.AI.AIDetectionInternalReport.FrameGpsData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Metadata', full_name='Seefar.Interfaces.AI.AIDetectionInternalReport.Metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='UpdatedSM', full_name='Seefar.Interfaces.AI.AIDetectionInternalReport.UpdatedSM', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=481,
)


_AIRAILRANGEESTIMATION = _descriptor.Descriptor(
  name='AiRailRangeEstimation',
  full_name='Seefar.Interfaces.AI.AiRailRangeEstimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='Seefar.Interfaces.AI.AiRailRangeEstimation.row', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dist', full_name='Seefar.Interfaces.AI.AiRailRangeEstimation.dist', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='Seefar.Interfaces.AI.AiRailRangeEstimation.resolution', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=553,
)


_AIRAILWAYSDETECTORMESSAGE = _descriptor.Descriptor(
  name='AiRailwaysDetectorMessage',
  full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leftRailColBest', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.leftRailColBest', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rightRailColBest', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.rightRailColBest', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='railRowBest', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.railRowBest', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='calcMethod', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.calcMethod', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rangeEstimation', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.rangeEstimation', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updatedSM', full_name='Seefar.Interfaces.AI.AiRailwaysDetectorMessage.updatedSM', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=902,
)

_AIDETECTIONINTERNALREPORT.fields_by_name['DetectionReport'].message_type = DataStructure__pb2._AIDETECTIONREPORT
_AIDETECTIONINTERNALREPORT.fields_by_name['FrameGpsData'].message_type = DataStructure__pb2._AIGPSDATA
_AIDETECTIONINTERNALREPORT.fields_by_name['Metadata'].message_type = DataStructure__pb2._AIFRAMEDATA
_AIDETECTIONINTERNALREPORT.fields_by_name['UpdatedSM'].message_type = _AIRAILWAYUPDATEDSM
_AIRAILWAYSDETECTORMESSAGE.fields_by_name['metadata'].message_type = DataStructure__pb2._AIFRAMEDATA
_AIRAILWAYSDETECTORMESSAGE.fields_by_name['calcMethod'].enum_type = _AIRAILWAYCALCMETHOD
_AIRAILWAYSDETECTORMESSAGE.fields_by_name['rangeEstimation'].message_type = _AIRAILRANGEESTIMATION
_AIRAILWAYSDETECTORMESSAGE.fields_by_name['updatedSM'].message_type = _AIRAILWAYUPDATEDSM
DESCRIPTOR.message_types_by_name['AiRailwayUpdatedSM'] = _AIRAILWAYUPDATEDSM
DESCRIPTOR.message_types_by_name['AIDetectionInternalReport'] = _AIDETECTIONINTERNALREPORT
DESCRIPTOR.message_types_by_name['AiRailRangeEstimation'] = _AIRAILRANGEESTIMATION
DESCRIPTOR.message_types_by_name['AiRailwaysDetectorMessage'] = _AIRAILWAYSDETECTORMESSAGE
DESCRIPTOR.enum_types_by_name['AiRailwayCalcMethod'] = _AIRAILWAYCALCMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AiRailwayUpdatedSM = _reflection.GeneratedProtocolMessageType('AiRailwayUpdatedSM', (_message.Message,), {
  'DESCRIPTOR' : _AIRAILWAYUPDATEDSM,
  '__module__' : 'RailwayAI_pb2'
  # @@protoc_insertion_point(class_scope:Seefar.Interfaces.AI.AiRailwayUpdatedSM)
  })
_sym_db.RegisterMessage(AiRailwayUpdatedSM)

AIDetectionInternalReport = _reflection.GeneratedProtocolMessageType('AIDetectionInternalReport', (_message.Message,), {
  'DESCRIPTOR' : _AIDETECTIONINTERNALREPORT,
  '__module__' : 'RailwayAI_pb2'
  # @@protoc_insertion_point(class_scope:Seefar.Interfaces.AI.AIDetectionInternalReport)
  })
_sym_db.RegisterMessage(AIDetectionInternalReport)

AiRailRangeEstimation = _reflection.GeneratedProtocolMessageType('AiRailRangeEstimation', (_message.Message,), {
  'DESCRIPTOR' : _AIRAILRANGEESTIMATION,
  '__module__' : 'RailwayAI_pb2'
  # @@protoc_insertion_point(class_scope:Seefar.Interfaces.AI.AiRailRangeEstimation)
  })
_sym_db.RegisterMessage(AiRailRangeEstimation)

AiRailwaysDetectorMessage = _reflection.GeneratedProtocolMessageType('AiRailwaysDetectorMessage', (_message.Message,), {
  'DESCRIPTOR' : _AIRAILWAYSDETECTORMESSAGE,
  '__module__' : 'RailwayAI_pb2'
  # @@protoc_insertion_point(class_scope:Seefar.Interfaces.AI.AiRailwaysDetectorMessage)
  })
_sym_db.RegisterMessage(AiRailwaysDetectorMessage)


# @@protoc_insertion_point(module_scope)
