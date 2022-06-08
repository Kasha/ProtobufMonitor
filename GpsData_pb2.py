# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GpsData.proto
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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GpsData.proto',
  package='Seefar.Interfaces.Gps',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rGpsData.proto\x12\x15Seefar.Interfaces.Gps\x1a\x0ftimestamp.proto\x1a\x0c\x43ommon.proto\"\xc7\x06\n\x0cPositionData\x12-\n\x07gpsTime\x18\x01 \x01(\x0b\x32\x1c.Seefar.Interfaces.Timestamp\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08latitude\x18\x03 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x02\x12\x0f\n\x07heading\x18\x05 \x01(\x02\x12\x0b\n\x03yaw\x18\x06 \x01(\x02\x12\r\n\x05pitch\x18\x07 \x01(\x02\x12\x0c\n\x04roll\x18\x08 \x01(\x02\x12\x10\n\x08velocity\x18\t \x01(\x02\x12\x1a\n\x12numberOfSatellites\x18\n \x01(\x05\x12,\n\x04mode\x18\x0b \x01(\x0e\x32\x1e.Seefar.Interfaces.Gps.GpsMode\x12\x11\n\tgpsStatus\x18\x0c \x01(\x05\x12:\n\tmsgHeader\x18\r \x01(\x0b\x32\'.Seefar.Interfaces.Common.MessageHeader\x12\x16\n\x0esigmaLongitude\x18\x0e \x01(\x02\x12\x15\n\rsigmaLatitude\x18\x0f \x01(\x02\x12\x15\n\rsigmaAltitude\x18\x10 \x01(\x02\x12\x15\n\rvelocityNorth\x18\x11 \x01(\x02\x12\x14\n\x0cvelocityEast\x18\x12 \x01(\x02\x12\x12\n\nvelocityUp\x18\x13 \x01(\x02\x12\x1a\n\x12sigmaVelocityNorth\x18\x14 \x01(\x02\x12\x19\n\x11sigmaVelocityEast\x18\x15 \x01(\x02\x12\x17\n\x0fsigmaVelocityUp\x18\x16 \x01(\x02\x12\x14\n\x0csigmaHeading\x18\x17 \x01(\x02\x12\x12\n\nsigmaPitch\x18\x18 \x01(\x02\x12\x11\n\tsigmaRoll\x18\x19 \x01(\x02\x12\x1a\n\x12\x61ltitudeLockStatus\x18\x1a \x01(\x05\x12;\n\rheadingStatus\x18\x1b \x01(\x0e\x32$.Seefar.Interfaces.Gps.HeadingStatus\x12?\n\x0fpositionQuality\x18\x1c \x01(\x0e\x32&.Seefar.Interfaces.Gps.PositionQuality\x12=\n\x11operabilityStatus\x18\x1d \x01(\x0e\x32\".Seefar.Interfaces.Gps.Operability*K\n\rHeadingStatus\x12\x16\n\x12IneffectiveHeading\x10\x00\x12\x0f\n\x0b\x46ixSolution\x10\x04\x12\x11\n\rFloatSolution\x10\x05*L\n\x0fPositionQuality\x12\x17\n\x13IneffectivePosition\x10\x00\x12\x0f\n\x0bSinglePoint\x10\x01\x12\x0f\n\x0bPseudoRange\x10\x02*/\n\x0bOperability\x12\x08\n\x04\x46ull\x10\x00\x12\x0c\n\x08\x44\x65graded\x10\x01\x12\x08\n\x04\x46\x61il\x10\x02*S\n\x07GpsMode\x12\x0b\n\x07Unknown\x10\x00\x12\x0c\n\x08Manual2D\x10\x01\x12\x0c\n\x08Manual3D\x10\x02\x12\n\n\x06\x41uto2D\x10\x03\x12\n\n\x06\x41uto3D\x10\x04\x12\x07\n\x03\x46ix\x10\x05\x62\x06proto3'
  ,
  dependencies=[timestamp__pb2.DESCRIPTOR,Common__pb2.DESCRIPTOR,])

_HEADINGSTATUS = _descriptor.EnumDescriptor(
  name='HeadingStatus',
  full_name='Seefar.Interfaces.Gps.HeadingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IneffectiveHeading', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FixSolution', index=1, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FloatSolution', index=2, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=913,
  serialized_end=988,
)
_sym_db.RegisterEnumDescriptor(_HEADINGSTATUS)

HeadingStatus = enum_type_wrapper.EnumTypeWrapper(_HEADINGSTATUS)
_POSITIONQUALITY = _descriptor.EnumDescriptor(
  name='PositionQuality',
  full_name='Seefar.Interfaces.Gps.PositionQuality',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IneffectivePosition', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SinglePoint', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PseudoRange', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=990,
  serialized_end=1066,
)
_sym_db.RegisterEnumDescriptor(_POSITIONQUALITY)

PositionQuality = enum_type_wrapper.EnumTypeWrapper(_POSITIONQUALITY)
_OPERABILITY = _descriptor.EnumDescriptor(
  name='Operability',
  full_name='Seefar.Interfaces.Gps.Operability',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Full', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Degraded', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Fail', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1068,
  serialized_end=1115,
)
_sym_db.RegisterEnumDescriptor(_OPERABILITY)

Operability = enum_type_wrapper.EnumTypeWrapper(_OPERABILITY)
_GPSMODE = _descriptor.EnumDescriptor(
  name='GpsMode',
  full_name='Seefar.Interfaces.Gps.GpsMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Manual2D', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Manual3D', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Auto2D', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Auto3D', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Fix', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1117,
  serialized_end=1200,
)
_sym_db.RegisterEnumDescriptor(_GPSMODE)

GpsMode = enum_type_wrapper.EnumTypeWrapper(_GPSMODE)
IneffectiveHeading = 0
FixSolution = 4
FloatSolution = 5
IneffectivePosition = 0
SinglePoint = 1
PseudoRange = 2
Full = 0
Degraded = 1
Fail = 2
Unknown = 0
Manual2D = 1
Manual3D = 2
Auto2D = 3
Auto3D = 4
Fix = 5



_POSITIONDATA = _descriptor.Descriptor(
  name='PositionData',
  full_name='Seefar.Interfaces.Gps.PositionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpsTime', full_name='Seefar.Interfaces.Gps.PositionData.gpsTime', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Seefar.Interfaces.Gps.PositionData.longitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Seefar.Interfaces.Gps.PositionData.latitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='Seefar.Interfaces.Gps.PositionData.altitude', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='Seefar.Interfaces.Gps.PositionData.heading', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='Seefar.Interfaces.Gps.PositionData.yaw', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='Seefar.Interfaces.Gps.PositionData.pitch', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roll', full_name='Seefar.Interfaces.Gps.PositionData.roll', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='Seefar.Interfaces.Gps.PositionData.velocity', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numberOfSatellites', full_name='Seefar.Interfaces.Gps.PositionData.numberOfSatellites', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='Seefar.Interfaces.Gps.PositionData.mode', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gpsStatus', full_name='Seefar.Interfaces.Gps.PositionData.gpsStatus', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgHeader', full_name='Seefar.Interfaces.Gps.PositionData.msgHeader', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaLongitude', full_name='Seefar.Interfaces.Gps.PositionData.sigmaLongitude', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaLatitude', full_name='Seefar.Interfaces.Gps.PositionData.sigmaLatitude', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaAltitude', full_name='Seefar.Interfaces.Gps.PositionData.sigmaAltitude', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocityNorth', full_name='Seefar.Interfaces.Gps.PositionData.velocityNorth', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocityEast', full_name='Seefar.Interfaces.Gps.PositionData.velocityEast', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocityUp', full_name='Seefar.Interfaces.Gps.PositionData.velocityUp', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaVelocityNorth', full_name='Seefar.Interfaces.Gps.PositionData.sigmaVelocityNorth', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaVelocityEast', full_name='Seefar.Interfaces.Gps.PositionData.sigmaVelocityEast', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaVelocityUp', full_name='Seefar.Interfaces.Gps.PositionData.sigmaVelocityUp', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaHeading', full_name='Seefar.Interfaces.Gps.PositionData.sigmaHeading', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaPitch', full_name='Seefar.Interfaces.Gps.PositionData.sigmaPitch', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmaRoll', full_name='Seefar.Interfaces.Gps.PositionData.sigmaRoll', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitudeLockStatus', full_name='Seefar.Interfaces.Gps.PositionData.altitudeLockStatus', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headingStatus', full_name='Seefar.Interfaces.Gps.PositionData.headingStatus', index=26,
      number=27, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='positionQuality', full_name='Seefar.Interfaces.Gps.PositionData.positionQuality', index=27,
      number=28, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operabilityStatus', full_name='Seefar.Interfaces.Gps.PositionData.operabilityStatus', index=28,
      number=29, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=72,
  serialized_end=911,
)

_POSITIONDATA.fields_by_name['gpsTime'].message_type = timestamp__pb2._TIMESTAMP
_POSITIONDATA.fields_by_name['mode'].enum_type = _GPSMODE
_POSITIONDATA.fields_by_name['msgHeader'].message_type = Common__pb2._MESSAGEHEADER
_POSITIONDATA.fields_by_name['headingStatus'].enum_type = _HEADINGSTATUS
_POSITIONDATA.fields_by_name['positionQuality'].enum_type = _POSITIONQUALITY
_POSITIONDATA.fields_by_name['operabilityStatus'].enum_type = _OPERABILITY
DESCRIPTOR.message_types_by_name['PositionData'] = _POSITIONDATA
DESCRIPTOR.enum_types_by_name['HeadingStatus'] = _HEADINGSTATUS
DESCRIPTOR.enum_types_by_name['PositionQuality'] = _POSITIONQUALITY
DESCRIPTOR.enum_types_by_name['Operability'] = _OPERABILITY
DESCRIPTOR.enum_types_by_name['GpsMode'] = _GPSMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PositionData = _reflection.GeneratedProtocolMessageType('PositionData', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONDATA,
  '__module__' : 'GpsData_pb2'
  # @@protoc_insertion_point(class_scope:Seefar.Interfaces.Gps.PositionData)
  })
_sym_db.RegisterMessage(PositionData)


# @@protoc_insertion_point(module_scope)