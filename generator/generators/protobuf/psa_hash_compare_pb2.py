# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: psa_hash_compare.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import psa_algorithm_pb2 as psa__algorithm__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='psa_hash_compare.proto',
  package='psa_hash_compare',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16psa_hash_compare.proto\x12\x10psa_hash_compare\x1a\x13psa_algorithm.proto\"T\n\tOperation\x12*\n\x03\x61lg\x18\x01 \x01(\x0e\x32\x1d.psa_algorithm.Algorithm.Hash\x12\r\n\x05input\x18\x02 \x01(\x0c\x12\x0c\n\x04hash\x18\x03 \x01(\x0c\"\x08\n\x06Resultb\x06proto3'
  ,
  dependencies=[psa__algorithm__pb2.DESCRIPTOR,])




_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='psa_hash_compare.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alg', full_name='psa_hash_compare.Operation.alg', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input', full_name='psa_hash_compare.Operation.input', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='psa_hash_compare.Operation.hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=65,
  serialized_end=149,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='psa_hash_compare.Result',
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
  serialized_start=151,
  serialized_end=159,
)

_OPERATION.fields_by_name['alg'].enum_type = psa__algorithm__pb2._ALGORITHM_HASH
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'psa_hash_compare_pb2'
  # @@protoc_insertion_point(class_scope:psa_hash_compare.Operation)
  })
_sym_db.RegisterMessage(Operation)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'psa_hash_compare_pb2'
  # @@protoc_insertion_point(class_scope:psa_hash_compare.Result)
  })
_sym_db.RegisterMessage(Result)


# @@protoc_insertion_point(module_scope)
