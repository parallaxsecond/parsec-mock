# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
import os
from os import listdir
from os.path import isfile, join

from yaml import safe_load, dump

from struct import pack
import base64

# Generator functions
# Add your new generator function here
# TODO: with some import syntax or clever moduling, it might be possible not
# to have to do anything here?
# F401 ignored for flake8 as those methods are called through eval
from generators.ping import gen as ping  # noqa: F401
from generators.list_opcodes_bad1 import gen as list_opcodes_bad1  # noqa: F401
from generators.list_opcodes_directauth import (  # noqa: F401
    gen as list_opcodes_directauth,
)
from generators.list_providers import gen as list_providers  # noqa: F401
from generators.list_clients import gen as list_clients  # noqa: F401
from generators.list_clients_admin_err import (
    gen as list_clients_admin_err,
)  # noqa: F401
from generators.delete_client import gen as delete_client  # noqa: F401
from generators.list_authenticators import gen as list_authenticators  # noqa: F401
from generators.delete_client_admin_err import (
    gen as delete_client_admin_err,
)  # noqa: F401
from generators.delete_client_notexist import (
    gen as delete_client_notexist,
)  # noqa: F401


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


def read_specs(folder):
    """Read test specs from a folder"""
    specfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    specs = []
    for file in specfiles:
        if file.startswith("."):
            continue
        print(f"Parsing spec file: {file}")
        # Only use the first part of the filename as spec name
        name = file.split(".")[0]
        with open(os.path.join(folder, file), "r") as f:
            spec = safe_load(f)
            testspec = TestSpec(spec["spec"])
            specs.append((name, testspec))
    return specs


def generate_data(specs, output_folder):
    """Generate test data for a list of specs"""
    for (name, spec) in specs:
        generate_spec_data(output_folder, spec, name)


def generate_spec_data(output_folder, spec, name):
    """Generates data for a single spec and outputs it into the specified output folder."""
    # The generator function has the same name as the test specification
    (operation, result) = eval(name)()

    request_auth = create_auth(spec.request.auth)
    request_content_len = spec.request.header.content_length
    if request_content_len == "auto":
        request_content_len = len(operation)

    request_auth_len = spec.request.header.auth_length
    if request_auth_len == "auto":
        request_auth_len = len(request_auth)
    request_header = pack_header(
        spec.request.header, request_auth_len, request_content_len
    )

    response_content_len = spec.response.header.content_length
    if response_content_len == "auto":
        response_content_len = len(result)

    response_auth_len = spec.response.header.auth_length
    response_header = pack_header(
        spec.response.header, response_auth_len, response_content_len
    )

    request_buf = request_header + operation + request_auth
    response_buf = response_header + result

    # The generator appends the base64 data at the end of the spec file
    out_data = {
        "spec": spec.basedict,
        "test_data": {
            "request": base64.b64encode(request_buf).decode("ascii"),
            "response": base64.b64encode(response_buf).decode("ascii"),
            "request_hex": "".join("{:02x}".format(x) for x in request_buf),
            "response_hex": "".join("{:02x}".format(x) for x in response_buf),
        },
    }
    out_path = os.path.join(output_folder, name + ".test.yaml")
    print(f"Writing spec {name} test data to {out_path}")
    with open(out_path, "w") as f:
        dump(out_data, f, sort_keys=False)


def pack_header(header, auth_len, body_len):
    """Take a header data structure and convert it into binary representation."""
    # pack function converts arguments into binary string, based on format string.
    # < means integers are little endian.  Rest of format string is one character per input to indicate
    # packed field interpretation.  See struct.pack docs for details.
    # This should map to the Fixed Common Header defined here:
    # https://parallaxsecond.github.io/parsec-book/parsec_client/wire_protocol.html#the-fixed-common-header
    return pack(
        "<IHBBHBQBBBIHIHH",
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
        0,
    )


def create_auth(auth_spec):
    """Creates auth body of message"""
    if auth_spec.type == "none":
        return b""
    if auth_spec.type == "direct":
        return auth_spec.app_name.encode("utf-8")
    return b""


def main():
    print("Generating test data.")

    specdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_specs"))
    print(f"Reading test specs from {specdir}")
    specs = read_specs(specdir)

    datadir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../generator_output")
    )
    print(f"Generating test data to {datadir}")
    generate_data(specs, datadir)


if __name__ == "__main__":
    main()
