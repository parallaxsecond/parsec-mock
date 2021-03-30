# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
import os
from os import listdir
from os.path import isfile, join

from yaml import safe_load, dump

from struct import pack
import base64

from generator_lib import generators


class TestSpec(object):
    """Class to represent a test specification.  Used to convert
    dictionary created by pyaml to object format, making code easier to read."""

    def __init__(self, dictionary):
        def _traverse(key, element):
            if isinstance(element, dict):
                return key, TestSpec(element)
            else:
                return key, element

        objd = dict(_traverse(k, v) for k, v in dictionary.items())
        self.__dict__.update(objd)
        self.basedict = dictionary

    def is_valid(self):
        return True


def read_specs(folder):
    """Read test specs from a folder"""
    specfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    specs = []
    for file in specfiles:
        print(f"Parsing spec file: {file}")
        with open(os.path.join(folder, file), 'r') as f:
            spec = safe_load(f)
            testspec = TestSpec(spec["spec"])
            if testspec.is_valid():
                specs.append(testspec)
            else:
                print(f"Error loading test spec from {file}")
    return specs


def generate_data(specs, output_folder):
    """Generate test data for a list of specs"""
    for spec in specs:
        if spec.generator in generators:
            print(f"Generating test {spec.name}")
            generate_spec_data(output_folder, spec, generators[spec.generator])
        else:
            print(f"No generator function found for spec {spec.name}, skipping...")


def generate_spec_data(output_folder, spec, generator_fn):
    """Generates data for a single spec and outputs it into the specified output folder."""
    (operation, result) = generator_fn()

    request_auth = create_auth(spec.request.auth)
    request_content_len = spec.request.header.content_length
    if request_content_len == 'auto':
        request_content_len = len(operation)

    request_auth_len = spec.request.header.auth_length
    if request_auth_len == 'auto':
        request_auth_len = len(request_auth)
    request_header = pack_header(spec.request.header, request_auth_len, request_content_len)

    response_content_len = spec.response.header.content_length
    if response_content_len == 'auto':
        response_content_len = len(result)

    response_auth_len = spec.response.header.auth_length

    response_header = pack_header(spec.response.header, response_auth_len, response_content_len)

    request_buf = request_header + operation + request_auth
    response_buf = response_header + result

    out_data = {
        "spec": spec.basedict,
        "test_data": {
            "request": base64.b64encode(request_buf).decode('ascii'),
            "response": base64.b64encode(response_buf).decode('ascii'),
        }
    }
    out_path = os.path.join(output_folder, spec.name + ".test.yaml")
    print(f"Writing spec {spec.name} test data to {out_path}")
    with open(out_path, 'w') as f:
        dump(out_data, f, sort_keys=False)


def pack_header(header, auth_len, body_len):
    """Take a header data structure and convert it into binary representation."""
    # pack function converts arguments into binary string, based on format string.
    # < means integers are little endian.  Rest of format string is one character per input to indicate
    # packed field interpretation.  See struct.pack docs for details.
    return pack('<IHBBHBQBBBIHIHH',
                header.magic_number,
                header.header_size,
                header.major_version_number,
                header.minor_version_number,
                header.flags,
                header.provider,
                header.session_handle,
                header.content_type,
                header.accept_type,
                header.auth_type,
                body_len,
                auth_len,
                header.opcode,
                header.status,
                0
                )


def create_auth(auth_spec):
    """Creates auth body of message"""
    if auth_spec.type == 'none':
        return b''
    if auth_spec.type == 'direct':
        return auth_spec.app_name.encode('utf-8')
    return b''


def main():
    specdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testspecs'))
    datadir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testdata'))
    print("Generating test data.")
    print(f"Reading test specs from {specdir}")
    print(f"Generating test data to {datadir}")
    specs = read_specs(specdir)

    generate_data(specs, datadir)


if __name__ == "__main__":
    main()
