# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacex/api/device/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spacex/api/device/common.proto',
  package='SpaceX.API.Device',
  syntax='proto3',
  serialized_options=b'Z\025spacex.com/api/device',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1espacex/api/device/common.proto\x12\x11SpaceX.API.Device\"\x95\x01\n\nDeviceInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12)\n\x10hardware_version\x18\x02 \x01(\tR\x0fhardwareVersion\x12)\n\x10software_version\x18\x03 \x01(\tR\x0fsoftwareVersion\x12!\n\x0c\x63ountry_code\x18\x04 \x01(\tR\x0b\x63ountryCode\"(\n\x0b\x44\x65viceState\x12\x19\n\x08uptime_s\x18\x01 \x01(\x04R\x07uptimeS\">\n\nSignedData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\x12\x1c\n\tsignature\x18\x02 \x01(\x0cR\tsignature\"\x12\n\x10GetNextIdRequest\">\n\x11GetNextIdResponse\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12\x19\n\x08\x65poch_id\x18\x02 \x01(\x04R\x07\x65pochId\"\\\n\nPingTarget\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location\x12\x18\n\x07\x61\x64\x64ress\x18\x03 \x01(\tR\x07\x61\x64\x64ress\"}\n\nPingResult\x12\x35\n\x06target\x18\x03 \x01(\x0b\x32\x1d.SpaceX.API.Device.PingTargetR\x06target\x12\x1a\n\x08\x64ropRate\x18\x01 \x01(\x02R\x08\x64ropRate\x12\x1c\n\tlatencyMs\x18\x02 \x01(\x02R\tlatencyMs\"Z\n\x10\x42ondingChallenge\x12\x17\n\x07\x64ish_id\x18\x01 \x01(\tR\x06\x64ishId\x12\x17\n\x07wifi_id\x18\x02 \x01(\tR\x06wifiId\x12\x14\n\x05nonce\x18\x03 \x01(\x0cR\x05nonce\"R\n\x13\x41uthenticateRequest\x12;\n\tchallenge\x18\x01 \x01(\x0b\x32\x1d.SpaceX.API.Device.SignedDataR\tchallenge\"^\n\x11\x43hallengeResponse\x12\x1c\n\tsignature\x18\x01 \x01(\x0cR\tsignature\x12+\n\x11\x63\x65rtificate_chain\x18\x02 \x01(\x0cR\x10\x63\x65rtificateChain\"\xa8\x03\n\x10NetworkInterface\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x46\n\x08rx_stats\x18\x02 \x01(\x0b\x32+.SpaceX.API.Device.NetworkInterface.RxStatsR\x07rxStats\x12\x46\n\x08tx_stats\x18\x03 \x01(\x0b\x32+.SpaceX.API.Device.NetworkInterface.TxStatsR\x07txStats\x12J\n\x08\x65thernet\x18\xe8\x07 \x01(\x0b\x32+.SpaceX.API.Device.EthernetNetworkInterfaceH\x00R\x08\x65thernet\x1a\\\n\x07RxStats\x12\x14\n\x05\x62ytes\x18\x01 \x01(\x04R\x05\x62ytes\x12\x18\n\x07packets\x18\x02 \x01(\x04R\x07packets\x12!\n\x0c\x66rame_errors\x18\x03 \x01(\x04R\x0b\x66rameErrors\x1a\x39\n\x07TxStats\x12\x14\n\x05\x62ytes\x18\x01 \x01(\x04R\x05\x62ytes\x12\x18\n\x07packets\x18\x02 \x01(\x04R\x07packetsB\x0b\n\tinterface\"\x84\x02\n\x18\x45thernetNetworkInterface\x12#\n\rlink_detected\x18\x01 \x01(\x08R\x0clinkDetected\x12\x1d\n\nspeed_mbps\x18\x02 \x01(\rR\tspeedMbps\x12-\n\x12\x61utonegotiation_on\x18\x03 \x01(\x08R\x11\x61utonegotiationOn\x12J\n\x06\x64uplex\x18\x04 \x01(\x0e\x32\x32.SpaceX.API.Device.EthernetNetworkInterface.DuplexR\x06\x64uplex\")\n\x06\x44uplex\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HALF\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\x42\x17Z\x15spacex.com/api/deviceb\x06proto3'
)



_ETHERNETNETWORKINTERFACE_DUPLEX = _descriptor.EnumDescriptor(
  name='Duplex',
  full_name='SpaceX.API.Device.EthernetNetworkInterface.Duplex',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HALF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1535,
  serialized_end=1576,
)
_sym_db.RegisterEnumDescriptor(_ETHERNETNETWORKINTERFACE_DUPLEX)


_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='SpaceX.API.Device.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SpaceX.API.Device.DeviceInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hardware_version', full_name='SpaceX.API.Device.DeviceInfo.hardware_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hardwareVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='software_version', full_name='SpaceX.API.Device.DeviceInfo.software_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='softwareVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='SpaceX.API.Device.DeviceInfo.country_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='countryCode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=203,
)


_DEVICESTATE = _descriptor.Descriptor(
  name='DeviceState',
  full_name='SpaceX.API.Device.DeviceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uptime_s', full_name='SpaceX.API.Device.DeviceState.uptime_s', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uptimeS', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=205,
  serialized_end=245,
)


_SIGNEDDATA = _descriptor.Descriptor(
  name='SignedData',
  full_name='SpaceX.API.Device.SignedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='SpaceX.API.Device.SignedData.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='SpaceX.API.Device.SignedData.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signature', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=247,
  serialized_end=309,
)


_GETNEXTIDREQUEST = _descriptor.Descriptor(
  name='GetNextIdRequest',
  full_name='SpaceX.API.Device.GetNextIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=311,
  serialized_end=329,
)


_GETNEXTIDRESPONSE = _descriptor.Descriptor(
  name='GetNextIdResponse',
  full_name='SpaceX.API.Device.GetNextIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SpaceX.API.Device.GetNextIdResponse.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epoch_id', full_name='SpaceX.API.Device.GetNextIdResponse.epoch_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='epochId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=331,
  serialized_end=393,
)


_PINGTARGET = _descriptor.Descriptor(
  name='PingTarget',
  full_name='SpaceX.API.Device.PingTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='SpaceX.API.Device.PingTarget.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='service', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='SpaceX.API.Device.PingTarget.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='location', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='SpaceX.API.Device.PingTarget.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=395,
  serialized_end=487,
)


_PINGRESULT = _descriptor.Descriptor(
  name='PingResult',
  full_name='SpaceX.API.Device.PingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='SpaceX.API.Device.PingResult.target', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='target', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropRate', full_name='SpaceX.API.Device.PingResult.dropRate', index=1,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dropRate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latencyMs', full_name='SpaceX.API.Device.PingResult.latencyMs', index=2,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='latencyMs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=489,
  serialized_end=614,
)


_BONDINGCHALLENGE = _descriptor.Descriptor(
  name='BondingChallenge',
  full_name='SpaceX.API.Device.BondingChallenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dish_id', full_name='SpaceX.API.Device.BondingChallenge.dish_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dishId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wifi_id', full_name='SpaceX.API.Device.BondingChallenge.wifi_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='wifiId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='SpaceX.API.Device.BondingChallenge.nonce', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nonce', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=616,
  serialized_end=706,
)


_AUTHENTICATEREQUEST = _descriptor.Descriptor(
  name='AuthenticateRequest',
  full_name='SpaceX.API.Device.AuthenticateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='SpaceX.API.Device.AuthenticateRequest.challenge', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='challenge', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=708,
  serialized_end=790,
)


_CHALLENGERESPONSE = _descriptor.Descriptor(
  name='ChallengeResponse',
  full_name='SpaceX.API.Device.ChallengeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='SpaceX.API.Device.ChallengeResponse.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signature', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='certificate_chain', full_name='SpaceX.API.Device.ChallengeResponse.certificate_chain', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='certificateChain', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=792,
  serialized_end=886,
)


_NETWORKINTERFACE_RXSTATS = _descriptor.Descriptor(
  name='RxStats',
  full_name='SpaceX.API.Device.NetworkInterface.RxStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='SpaceX.API.Device.NetworkInterface.RxStats.bytes', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bytes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packets', full_name='SpaceX.API.Device.NetworkInterface.RxStats.packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='packets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_errors', full_name='SpaceX.API.Device.NetworkInterface.RxStats.frame_errors', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='frameErrors', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1149,
  serialized_end=1241,
)

_NETWORKINTERFACE_TXSTATS = _descriptor.Descriptor(
  name='TxStats',
  full_name='SpaceX.API.Device.NetworkInterface.TxStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='SpaceX.API.Device.NetworkInterface.TxStats.bytes', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bytes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packets', full_name='SpaceX.API.Device.NetworkInterface.TxStats.packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='packets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1243,
  serialized_end=1300,
)

_NETWORKINTERFACE = _descriptor.Descriptor(
  name='NetworkInterface',
  full_name='SpaceX.API.Device.NetworkInterface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SpaceX.API.Device.NetworkInterface.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_stats', full_name='SpaceX.API.Device.NetworkInterface.rx_stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rxStats', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_stats', full_name='SpaceX.API.Device.NetworkInterface.tx_stats', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='txStats', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ethernet', full_name='SpaceX.API.Device.NetworkInterface.ethernet', index=3,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ethernet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NETWORKINTERFACE_RXSTATS, _NETWORKINTERFACE_TXSTATS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='interface', full_name='SpaceX.API.Device.NetworkInterface.interface',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=889,
  serialized_end=1313,
)


_ETHERNETNETWORKINTERFACE = _descriptor.Descriptor(
  name='EthernetNetworkInterface',
  full_name='SpaceX.API.Device.EthernetNetworkInterface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_detected', full_name='SpaceX.API.Device.EthernetNetworkInterface.link_detected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='linkDetected', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed_mbps', full_name='SpaceX.API.Device.EthernetNetworkInterface.speed_mbps', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='speedMbps', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autonegotiation_on', full_name='SpaceX.API.Device.EthernetNetworkInterface.autonegotiation_on', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='autonegotiationOn', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duplex', full_name='SpaceX.API.Device.EthernetNetworkInterface.duplex', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='duplex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ETHERNETNETWORKINTERFACE_DUPLEX,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1316,
  serialized_end=1576,
)

_PINGRESULT.fields_by_name['target'].message_type = _PINGTARGET
_AUTHENTICATEREQUEST.fields_by_name['challenge'].message_type = _SIGNEDDATA
_NETWORKINTERFACE_RXSTATS.containing_type = _NETWORKINTERFACE
_NETWORKINTERFACE_TXSTATS.containing_type = _NETWORKINTERFACE
_NETWORKINTERFACE.fields_by_name['rx_stats'].message_type = _NETWORKINTERFACE_RXSTATS
_NETWORKINTERFACE.fields_by_name['tx_stats'].message_type = _NETWORKINTERFACE_TXSTATS
_NETWORKINTERFACE.fields_by_name['ethernet'].message_type = _ETHERNETNETWORKINTERFACE
_NETWORKINTERFACE.oneofs_by_name['interface'].fields.append(
  _NETWORKINTERFACE.fields_by_name['ethernet'])
_NETWORKINTERFACE.fields_by_name['ethernet'].containing_oneof = _NETWORKINTERFACE.oneofs_by_name['interface']
_ETHERNETNETWORKINTERFACE.fields_by_name['duplex'].enum_type = _ETHERNETNETWORKINTERFACE_DUPLEX
_ETHERNETNETWORKINTERFACE_DUPLEX.containing_type = _ETHERNETNETWORKINTERFACE
DESCRIPTOR.message_types_by_name['DeviceInfo'] = _DEVICEINFO
DESCRIPTOR.message_types_by_name['DeviceState'] = _DEVICESTATE
DESCRIPTOR.message_types_by_name['SignedData'] = _SIGNEDDATA
DESCRIPTOR.message_types_by_name['GetNextIdRequest'] = _GETNEXTIDREQUEST
DESCRIPTOR.message_types_by_name['GetNextIdResponse'] = _GETNEXTIDRESPONSE
DESCRIPTOR.message_types_by_name['PingTarget'] = _PINGTARGET
DESCRIPTOR.message_types_by_name['PingResult'] = _PINGRESULT
DESCRIPTOR.message_types_by_name['BondingChallenge'] = _BONDINGCHALLENGE
DESCRIPTOR.message_types_by_name['AuthenticateRequest'] = _AUTHENTICATEREQUEST
DESCRIPTOR.message_types_by_name['ChallengeResponse'] = _CHALLENGERESPONSE
DESCRIPTOR.message_types_by_name['NetworkInterface'] = _NETWORKINTERFACE
DESCRIPTOR.message_types_by_name['EthernetNetworkInterface'] = _ETHERNETNETWORKINTERFACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFO,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DeviceInfo)
  })
_sym_db.RegisterMessage(DeviceInfo)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

SignedData = _reflection.GeneratedProtocolMessageType('SignedData', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDDATA,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.SignedData)
  })
_sym_db.RegisterMessage(SignedData)

GetNextIdRequest = _reflection.GeneratedProtocolMessageType('GetNextIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNEXTIDREQUEST,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.GetNextIdRequest)
  })
_sym_db.RegisterMessage(GetNextIdRequest)

GetNextIdResponse = _reflection.GeneratedProtocolMessageType('GetNextIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNEXTIDRESPONSE,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.GetNextIdResponse)
  })
_sym_db.RegisterMessage(GetNextIdResponse)

PingTarget = _reflection.GeneratedProtocolMessageType('PingTarget', (_message.Message,), {
  'DESCRIPTOR' : _PINGTARGET,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.PingTarget)
  })
_sym_db.RegisterMessage(PingTarget)

PingResult = _reflection.GeneratedProtocolMessageType('PingResult', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESULT,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.PingResult)
  })
_sym_db.RegisterMessage(PingResult)

BondingChallenge = _reflection.GeneratedProtocolMessageType('BondingChallenge', (_message.Message,), {
  'DESCRIPTOR' : _BONDINGCHALLENGE,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.BondingChallenge)
  })
_sym_db.RegisterMessage(BondingChallenge)

AuthenticateRequest = _reflection.GeneratedProtocolMessageType('AuthenticateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATEREQUEST,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.AuthenticateRequest)
  })
_sym_db.RegisterMessage(AuthenticateRequest)

ChallengeResponse = _reflection.GeneratedProtocolMessageType('ChallengeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGERESPONSE,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.ChallengeResponse)
  })
_sym_db.RegisterMessage(ChallengeResponse)

NetworkInterface = _reflection.GeneratedProtocolMessageType('NetworkInterface', (_message.Message,), {

  'RxStats' : _reflection.GeneratedProtocolMessageType('RxStats', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKINTERFACE_RXSTATS,
    '__module__' : 'spacex.api.device.common_pb2'
    # @@protoc_insertion_point(class_scope:SpaceX.API.Device.NetworkInterface.RxStats)
    })
  ,

  'TxStats' : _reflection.GeneratedProtocolMessageType('TxStats', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKINTERFACE_TXSTATS,
    '__module__' : 'spacex.api.device.common_pb2'
    # @@protoc_insertion_point(class_scope:SpaceX.API.Device.NetworkInterface.TxStats)
    })
  ,
  'DESCRIPTOR' : _NETWORKINTERFACE,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.NetworkInterface)
  })
_sym_db.RegisterMessage(NetworkInterface)
_sym_db.RegisterMessage(NetworkInterface.RxStats)
_sym_db.RegisterMessage(NetworkInterface.TxStats)

EthernetNetworkInterface = _reflection.GeneratedProtocolMessageType('EthernetNetworkInterface', (_message.Message,), {
  'DESCRIPTOR' : _ETHERNETNETWORKINTERFACE,
  '__module__' : 'spacex.api.device.common_pb2'
  # @@protoc_insertion_point(class_scope:SpaceX.API.Device.EthernetNetworkInterface)
  })
_sym_db.RegisterMessage(EthernetNetworkInterface)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
