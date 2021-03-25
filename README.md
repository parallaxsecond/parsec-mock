# Parsec Mock

This repository contains a mock service to test clients, and a test data generator to create test data files for the mock service, or to be used in testing of the parsec service, or parsec clients.

See [this issue](https://github.com/parallaxsecond/parsec/issues/350) which describes the
proposal.

# Prerequisites
To run the utilities in this repository, you will need python3 and pip installing.

To install package prerequisites, run the following from this folder:

```bash
pip install -r requirements.txt
```
# Usage
## Run Mock Service
**TBD**

## Generate Test Data
To generate test data from test specs, run 

```
python generator/generator.py
```

This will parse the test specs in generator/testspecs and create test data in testdata/.  

# Test Data
The generator/generator.py script creates test data files in the testdata folder.  These test data files are intended for use, either with the mock service supplied here, or in other mock services that may be developed for the parsec service or parsec clients.  The test data files consist of the [test spec](#test-spec-format) (useful for the writer of a unit test), and test data, which contains base 64 encodes strings for a parsec request and a corresponding result.

The overall test data file format is, therefore:

```yaml
spec:
    # for format see below
test_data:
  request: EKfAXh4AAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAA
  result: EKfAXh4AAQAAAAAAAAAAAAAAAAAAAAIAAAAAAAEAAAAAAAAACAE=
```
## Expected Use Of Test Data
This repository does not dictate how the test data should be used by parsec client developers, but it was developed with the following use case in mind:

A client developer wants to test a parsec request in their client.  
- They select an appropriate test data file that fulfils the needs of their test (or creates a new one in this repository and uses that)
- They write client code that should generate a message to match the request section of the [test spec](#test-spec-format).
- They configure a mock service (the one here or a custom one) to expect the data defined in the test_data.request part of the test data file as well as the data to send if that request is received and what to send if it is not.
- They stimulate their client under test to send the request message to the mock service.
- The mock service will check to see if the request message it received matches the expected value (this is an exact byte match).
  - If the match was successful, then it will return the configured match response
  - Otherwise, it will return the configured non-match response
- The client under test will attempt to decode the response.  The results can be checked by the test code.
- If the spec.response.parse_should_succeed field is set to true, then the test code *should* expect a successful parse of the response data.  Otherwise, it *should* expect the parsing to fail.


## Writing Tests
To write a new test, a developer should create a test spec file in the generator/testspecs folder, using the [format below](#test-spec-format). 

They then need to write a generator function in ```generator/generator_lib.py```.  This generator function takes no arguments, and should output a tuple of python binary strings.  

The first element of the tuple should be the protocol buffer encoded value of the request message that is described in the spec.request.body_description field of the test spec.  The second element of the tuple should be the protocol buffer encoded value of the result message that is described in the spec.result.body_description field of the test spec.

An example generator for a list opcodes test is shown below:

```python
def gen_list_opcodes_auth_direct():
    op = protobuf.list_opcodes_pb2.Operation()
    op.provider_id = 1

    result = protobuf.list_opcodes_pb2.Result()
    result.opcodes.extend([1,3,2])
    return (op.SerializeToString(), result.SerializeToString())
```
The generated protocol buffers python library files are in generator/protobuf.

Finally, the developer should add an entry to the generator dictionary at the bottom of the ```generator/generator_lib.py``` file.  The key must correspond to the value in the test spec's spec.generator field.  The value in the generator dictionary must be the new generator function name.  e.g.:

```python
generators = {
    'ping_no_auth': gen_ping_no_auth,
    'list_opcodes_auth_direct': gen_list_opcodes_auth_direct,
}
```
**NOTE**  A generator function can be used in multiple test specs, if required.

## Test Spec Format

Test specs are defined as YAML.  An example file is shown below:

```yaml
# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
spec:
  name: list_opcodes_auth_direct
  generator: list_opcodes_auth_direct
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
    auth: 
      type: direct
      app_name: jimbob
    expected_parse_result: fail_auth

```
The whole test spec is defined in the spec: object in the file.  In that spec, the fields are:
| Field | Description |
| --- | --- |
| name | The name of the test spec.  Used to name the output test data file |
| generator | The lookup for the request and response generator in the generator library.  See [writing tests](#writing-tests).|
| description | Description of test, not used in generation |
| request | Settings for configuring the request data for the test data file |
| request.header | Field values for the request header.  Meanings of these files and valid values can be found in the [parsec book](https://parallaxsecond.github.io/parsec-book/parsec_client/wire_protocol.html). |
| request.header.content_length | If this field has the value ```auto``` then its value is calculated from the generated request content.  If the value is a number, then that value is used in the field instead. |
| request.header.auth_length | If this field has the value ```auto``` then its value is calculated from the generated auth content.  If the value is a number, then that value is used in the field instead. |
| request.body_description | A free form description of the contents of the request content.  Used for test writers (and generator writers) to understand how to construct the request object.  This field is not used by the test generator. |
| request.auth.type | This can either be ```none```, which will cause the auth section of the message to be empty (equivalent of the No Authentication type of authentication); or it can be ```direct```, which will cause the auth section of the message to contain authentication data corresponding to the format for Direct Authentication.  If ```direct``` is set, then the request.auth.app_name field must be set.  Note that this field does not cause the header auth_type field to be set. |
| request.auth.app_name | Used to populate the auth section of the message when ```direct``` authentication is selected |
| result | Settings for configuration the result data for the test data file |
| result.header | Field values for the result header.  Meanings of these files and valid values can be found in the [parsec book](https://parallaxsecond.github.io/parsec-book/parsec_client/wire_protocol.html). |
| result.header.content_length | If this field has the value ```auto``` then its value is calculated from the generated result content.  If the value is a number, then that value is used in the field instead |
| result.header.auth_length | If this field has the value ```auto``` then its value is calculated from the generated auth content.  If the value is a number, then that value is used in the field instead. |
| result.body_description | A free form description of the contents of the result content.  Used for test writers (and generator writers) to understand how to construct the request object.  This field is not used by the test generator. |
| result.auth.type | This can either be ```none```, which will cause the auth section of the message to be empty (equivalent of the No Authentication type of authentication); or it can be ```direct```, which will cause the auth section of the message to contain authentication data corresponding to the format for Direct Authentication.  If ```direct``` is set, then the result.auth.app_name field must be set.  Note that this field does not cause the header auth_type field to be set.  **NOTE:**  A Parsec client would not send authentication data in a result message, but this spec format allows test authors to create the message as they wish to excersice the parsec client code. |
| result.auth.app_name | Used to populate the auth section of the message when ```direct``` authentication is selected |
| result.expected_parse_result | Used to indicate whether a client being tested with this data should successfully be parsed (even if it is returning a failure status code).  If the message is valid according to the parsec interface specification, this field should have the valid ```succeed```.  If the message is invalid, it should have the values of ```fail_header``` if the header is invalid; ```fail_auth``` if the authentication data is invlid, or ```fail_content``` if the content is invalid.  Further values may be added to this ennum in the future. |



# License

The software is provided under Apache-2.0. Contributions to this project are accepted under the same
license.

# Contributing

Please check the [**Contribution
Guidelines**](https://parallaxsecond.github.io/parsec-book/contributing/index.html) to know more
about the contribution process.

*Copyright 2021 Contributors to the Parsec project.*
