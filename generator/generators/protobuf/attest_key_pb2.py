# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attest_key.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='attest_key.proto',
  package='attest_key',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x61ttest_key.proto\x12\nattest_key\"\xc2\x01\n\x1a\x41ttestationMechanismParams\x12X\n\x13\x61\x63tivate_credential\x18\x01 \x01(\x0b\x32\x39.attest_key.AttestationMechanismParams.ActivateCredentialH\x00\x1a=\n\x12\x41\x63tivateCredential\x12\x17\n\x0f\x63redential_blob\x18\x01 \x01(\x0c\x12\x0e\n\x06secret\x18\x02 \x01(\x0c\x42\x0b\n\tmechanism\"~\n\tOperation\x12\x19\n\x11\x61ttested_key_name\x18\x01 \x01(\t\x12:\n\nparameters\x18\x02 \x01(\x0b\x32&.attest_key.AttestationMechanismParams\x12\x1a\n\x12\x61ttesting_key_name\x18\x03 \x01(\t\"\x9b\x01\n\x11\x41ttestationOutput\x12O\n\x13\x61\x63tivate_credential\x18\x01 \x01(\x0b\x32\x30.attest_key.AttestationOutput.ActivateCredentialH\x00\x1a(\n\x12\x41\x63tivateCredential\x12\x12\n\ncredential\x18\x01 \x01(\x0c\x42\x0b\n\tmechanism\"7\n\x06Result\x12-\n\x06output\x18\x01 \x01(\x0b\x32\x1d.attest_key.AttestationOutputb\x06proto3'
)




_ATTESTATIONMECHANISMPARAMS_ACTIVATECREDENTIAL = _descriptor.Descriptor(
  name='ActivateCredential',
  full_name='attest_key.AttestationMechanismParams.ActivateCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='credential_blob', full_name='attest_key.AttestationMechanismParams.ActivateCredential.credential_blob', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='attest_key.AttestationMechanismParams.ActivateCredential.secret', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=153,
  serialized_end=214,
)

_ATTESTATIONMECHANISMPARAMS = _descriptor.Descriptor(
  name='AttestationMechanismParams',
  full_name='attest_key.AttestationMechanismParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activate_credential', full_name='attest_key.AttestationMechanismParams.activate_credential', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ATTESTATIONMECHANISMPARAMS_ACTIVATECREDENTIAL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='mechanism', full_name='attest_key.AttestationMechanismParams.mechanism',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=33,
  serialized_end=227,
)


_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='attest_key.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attested_key_name', full_name='attest_key.Operation.attested_key_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='attest_key.Operation.parameters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attesting_key_name', full_name='attest_key.Operation.attesting_key_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=229,
  serialized_end=355,
)


_ATTESTATIONOUTPUT_ACTIVATECREDENTIAL = _descriptor.Descriptor(
  name='ActivateCredential',
  full_name='attest_key.AttestationOutput.ActivateCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='credential', full_name='attest_key.AttestationOutput.ActivateCredential.credential', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=460,
  serialized_end=500,
)

_ATTESTATIONOUTPUT = _descriptor.Descriptor(
  name='AttestationOutput',
  full_name='attest_key.AttestationOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activate_credential', full_name='attest_key.AttestationOutput.activate_credential', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ATTESTATIONOUTPUT_ACTIVATECREDENTIAL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='mechanism', full_name='attest_key.AttestationOutput.mechanism',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=358,
  serialized_end=513,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='attest_key.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='attest_key.Result.output', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=515,
  serialized_end=570,
)

_ATTESTATIONMECHANISMPARAMS_ACTIVATECREDENTIAL.containing_type = _ATTESTATIONMECHANISMPARAMS
_ATTESTATIONMECHANISMPARAMS.fields_by_name['activate_credential'].message_type = _ATTESTATIONMECHANISMPARAMS_ACTIVATECREDENTIAL
_ATTESTATIONMECHANISMPARAMS.oneofs_by_name['mechanism'].fields.append(
  _ATTESTATIONMECHANISMPARAMS.fields_by_name['activate_credential'])
_ATTESTATIONMECHANISMPARAMS.fields_by_name['activate_credential'].containing_oneof = _ATTESTATIONMECHANISMPARAMS.oneofs_by_name['mechanism']
_OPERATION.fields_by_name['parameters'].message_type = _ATTESTATIONMECHANISMPARAMS
_ATTESTATIONOUTPUT_ACTIVATECREDENTIAL.containing_type = _ATTESTATIONOUTPUT
_ATTESTATIONOUTPUT.fields_by_name['activate_credential'].message_type = _ATTESTATIONOUTPUT_ACTIVATECREDENTIAL
_ATTESTATIONOUTPUT.oneofs_by_name['mechanism'].fields.append(
  _ATTESTATIONOUTPUT.fields_by_name['activate_credential'])
_ATTESTATIONOUTPUT.fields_by_name['activate_credential'].containing_oneof = _ATTESTATIONOUTPUT.oneofs_by_name['mechanism']
_RESULT.fields_by_name['output'].message_type = _ATTESTATIONOUTPUT
DESCRIPTOR.message_types_by_name['AttestationMechanismParams'] = _ATTESTATIONMECHANISMPARAMS
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['AttestationOutput'] = _ATTESTATIONOUTPUT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttestationMechanismParams = _reflection.GeneratedProtocolMessageType('AttestationMechanismParams', (_message.Message,), {

  'ActivateCredential' : _reflection.GeneratedProtocolMessageType('ActivateCredential', (_message.Message,), {
    'DESCRIPTOR' : _ATTESTATIONMECHANISMPARAMS_ACTIVATECREDENTIAL,
    '__module__' : 'attest_key_pb2'
    # @@protoc_insertion_point(class_scope:attest_key.AttestationMechanismParams.ActivateCredential)
    })
  ,
  'DESCRIPTOR' : _ATTESTATIONMECHANISMPARAMS,
  '__module__' : 'attest_key_pb2'
  # @@protoc_insertion_point(class_scope:attest_key.AttestationMechanismParams)
  })
_sym_db.RegisterMessage(AttestationMechanismParams)
_sym_db.RegisterMessage(AttestationMechanismParams.ActivateCredential)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'attest_key_pb2'
  # @@protoc_insertion_point(class_scope:attest_key.Operation)
  })
_sym_db.RegisterMessage(Operation)

AttestationOutput = _reflection.GeneratedProtocolMessageType('AttestationOutput', (_message.Message,), {

  'ActivateCredential' : _reflection.GeneratedProtocolMessageType('ActivateCredential', (_message.Message,), {
    'DESCRIPTOR' : _ATTESTATIONOUTPUT_ACTIVATECREDENTIAL,
    '__module__' : 'attest_key_pb2'
    # @@protoc_insertion_point(class_scope:attest_key.AttestationOutput.ActivateCredential)
    })
  ,
  'DESCRIPTOR' : _ATTESTATIONOUTPUT,
  '__module__' : 'attest_key_pb2'
  # @@protoc_insertion_point(class_scope:attest_key.AttestationOutput)
  })
_sym_db.RegisterMessage(AttestationOutput)
_sym_db.RegisterMessage(AttestationOutput.ActivateCredential)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'attest_key_pb2'
  # @@protoc_insertion_point(class_scope:attest_key.Result)
  })
_sym_db.RegisterMessage(Result)


# @@protoc_insertion_point(module_scope)
