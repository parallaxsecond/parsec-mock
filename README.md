# Parsec Mock

This repository contains a mock service to test Parsec clients and a test data generator to create
test data files for the mock service.

See [this issue](https://github.com/parallaxsecond/parsec/issues/350) which describes the proposal.

# Prerequisites

To run the utilities in this repository, you will need python3 and pip installing.

To install package prerequisites, run the following from this folder:

```
pip install -r requirements.txt
```

# Usage

## Run the Mock Service

Currently the mock service only supports running test cases from a folder in a request matching
mode. To run the service:

```
# To get help
python parsec_mock/parsec_mock.py --help
# To define test case folder (defaults to ./generator_output)
python parsec_mock/parsec_mock.py --test-folder FOLDER_NAME
# To define the unix socket address to listen to.  Defaults to ./parsec.sock
python parsec_mock/parsec_mock.py --parsec-socket SOCKET_ADDRESS
```

The mock service loads all the test cases from the folder and, if it receives a request that matches
the (base64 encoded) `test_data.request` field in the test case file, it will repond with the base64
encoded data in the `test_data.response` field.

If more than one test case shares the same `test_data.request` value, then the last one to be loaded
will be used.

## Generate Test Data

To generate test data from test specs, run

```
python generator/generator.py
```

This will parse the test specs in `generator/test_specs` and create test data in
`generator_output/`.

# Test Data

The `generator/generator.py` script creates test data files in the `generator_output` folder. These
test data files are intended for use, either with the mock service supplied here, or in other mock
services that may be developed for the parsec service or parsec clients. The test data files consist
of the [test spec](#test-spec-format) (useful for the writer of a unit test), and test data, which
contains base64 encoded strings for a parsec request and a corresponding result.

The overall test data file format is, therefore:

```
spec:
    # for format see below
test_data:
  request: EKfAXh4AAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAA
  result: EKfAXh4AAQAAAAAAAAAAAAAAAAAAAAIAAAAAAAEAAAAAAAAACAE=
```

## Expected Use Of Test Data

A client developer wants to test a parsec request in their client.

- They select an appropriate test data file that fulfils the needs of their test (or [creates a new
   one](#writing-tests) in this repository and uses that)
- They write client code that should generate a message to match the request section of the [test
   spec](#test-spec-format).
- They start the mock service
- They stimulate their client under test to send the request message to the mock service.
- The mock service will check to see if the request message it received matches the expected value
   (this is an exact byte match).
   - If the match was successful, then it will return the configured match response
   - Otherwise, it will not return anything and close the connection
- The client under test will attempt to decode the response. The results can be checked by the test
   code.

## Writing Tests

To write a new test, a developer should create a test spec file in the `generator/test_specs`
folder, using the [format below](#test-spec-format).

They then need to write a generator function in `generator/generators`. This generator function
takes no arguments, and should output a tuple of python binary strings.

The first element of the tuple should be the protocol buffer encoded value of the request's
*operation* message that is described in the `spec.request.body_description` field of the test spec.
The second element of the tuple should be the protocol buffer encoded *result* value of the response
message that is described in the `spec.result.body_description` field of the test spec.

The generated protocol buffers python library files are in `generator/generators/protobuf`.

## Test Spec Format

Test specs are defined as YAML. An example file is shown below:

```
# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
spec:
  description: List opcodes using direct authentication
  request:
    header:
      magic_number: 0x5EC0A710
      header_size: 0x1E
      major_version_number: 0x01
      minor_version_number: 0x00
      flags: 0x0000
      provider: 0x00
      session_handle: 0x0000000000000000
      content_type: 0x00
      accept_type: 0x00
      auth_type: 0x00
      content_length: auto
      auth_length: auto
      opcode: 0x00000009
      status: 0x0000
    body_description: provider id 0x01
    auth: 
      type: direct
      app_name: jimbob
  result:
    header:
      magic_number: 0x5EC0A710
      header_size: 0x1E
      major_version_number: 0x01
      minor_version_number: 0x00
      flags: 0x0000
      provider: 0x00
      session_handle: 0x0000000000000000
      content_type: 0x00
      accept_type: 0x00
      auth_type: 0x00
      content_length: auto
      auth_length: auto
      opcode: 0x00000009
      status: 0x0000
    body_description: list opcodes result [1,3,2]
```

The whole test spec is defined in the spec: object in the file. In that spec, the fields are:

| Field                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `description`                    | Description of test, not used in generation                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `request`                        | Settings for configuring the request data for the test data file                                                                                                                                                                                                                                                                                                                                                                                                          |
| `request.header`                 | Field values for the request header.  Meanings of these files and valid values can be found in the [parsec book](https://parallaxsecond.github.io/parsec-book/parsec_client/wire_protocol.html).                                                                                                                                                                                                                                                                          |
| `request.header.content_length`  | If this field has the value `auto` then its value is calculated from the generated request content.  If the value is a number, then that value is used in the field instead.                                                                                                                                                                                                                                                                                              |
| `request.header.auth_length`     | If this field has the value `auto` then its value is calculated from the generated auth content.  If the value is a number, then that value is used in the field instead.                                                                                                                                                                                                                                                                                                 |
| `request.body_description`       | A free form description of the contents of the request content.  Used for test writers (and generator writers) to understand how to construct the request object.  This field is not used by the test generator.                                                                                                                                                                                                                                                          |
| `request.auth.type`              | This can either be `none`, which will cause the auth section of the message to be empty (equivalent of the No Authentication type of authentication); or it can be `direct`, which will cause the auth section of the message to contain authentication data corresponding to the format for Direct Authentication.  If `direct` is set, then the `request.auth.app_name` field must be set.  Note that this field does not cause the header `auth_type` field to be set. |
| `request.auth.app_name`          | Used to populate the auth section of the message when `direct` authentication is selected                                                                                                                                                                                                                                                                                                                                                                                 |
| `response`                       | Settings for configuration the response data for the test data file                                                                                                                                                                                                                                                                                                                                                                                                       |
| `response.header`                | Field values for the response header.  Meanings of these files and valid values can be found in the [parsec book](https://parallaxsecond.github.io/parsec-book/parsec_client/wire_protocol.html).                                                                                                                                                                                                                                                                         |
| `response.header.content_length` | If this field has the value `auto` then its value is calculated from the generated response content.  If the value is a number, then that value is used in the field instead                                                                                                                                                                                                                                                                                              |
| `response.header.auth_length`    | If this field has the value `auto` then its value is calculated from the generated auth content.  If the value is a number, then that value is used in the field instead.                                                                                                                                                                                                                                                                                                 |
| `response.body_description`      | A free form description of the contents of the response content.  Used for test writers (and generator writers) to understand how to construct the result object.  This field is not used by the test generator.                                                                                                                                                                                                                                                          |

# Mock service testing

There is a very simple test for the mock service in the test folder. Run this from the current
folder:

```
python ./tests/mock_test.py
```

This expects the mock service to be listening on `./parsec.sock` and to have the
`generator_output/ping_no_auth.test.yaml` test spec loaded.

# License

The software is provided under Apache-2.0. Contributions to this project are accepted under the same
license.

# Contributing

Please check the [**Contribution
Guidelines**](https://parallaxsecond.github.io/parsec-book/contributing/index.html) to know more
about the contribution process.

*Copyright 2021 Contributors to the Parsec project.*
