# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cloudevent.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63loudevent.proto\x12\x11io.cloudevents.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb0\x04\n\nCloudEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x14\n\x0cspec_version\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x41\n\nattributes\x18\x05 \x03(\x0b\x32-.io.cloudevents.v1.CloudEvent.AttributesEntry\x12\x15\n\x0b\x62inary_data\x18\x06 \x01(\x0cH\x00\x12\x13\n\ttext_data\x18\x07 \x01(\tH\x00\x12*\n\nproto_data\x18\x08 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x1ai\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.io.cloudevents.v1.CloudEvent.CloudEventAttributeValue:\x02\x38\x01\x1a\xd3\x01\n\x18\x43loudEventAttributeValue\x12\x14\n\nce_boolean\x18\x01 \x01(\x08H\x00\x12\x14\n\nce_integer\x18\x02 \x01(\x05H\x00\x12\x13\n\tce_string\x18\x03 \x01(\tH\x00\x12\x12\n\x08\x63\x65_bytes\x18\x04 \x01(\x0cH\x00\x12\x10\n\x06\x63\x65_uri\x18\x05 \x01(\tH\x00\x12\x14\n\nce_uri_ref\x18\x06 \x01(\tH\x00\x12\x32\n\x0c\x63\x65_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x42\x06\n\x04\x61ttrB\x06\n\x04\x64\x61taB\x1e\xaa\x02\x1bMicrosoft.AutoGen.Contractsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cloudevent_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\033Microsoft.AutoGen.Contracts'
  _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._options = None
  _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_CLOUDEVENT']._serialized_start=100
  _globals['_CLOUDEVENT']._serialized_end=660
  _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._serialized_start=333
  _globals['_CLOUDEVENT_ATTRIBUTESENTRY']._serialized_end=438
  _globals['_CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE']._serialized_start=441
  _globals['_CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE']._serialized_end=652
# @@protoc_insertion_point(module_scope)
