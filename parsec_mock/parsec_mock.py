# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
import click

import socket
import os
from os import listdir
from os.path import isfile, join

import base64

from yaml import safe_load


@click.command()
@click.option('--test-folder', default='./generator_output', help='Load all tests from folder')
@click.option('--parsec-socket', default='./parsec.sock', help='Path to parsec unix socket')
def run_test(test_folder, parsec_socket):
    print('Mock parsec service listening on unix://{}.'.format(parsec_socket))

    test_cases = load_tests_from_folder(test_folder)

    print('Serving all {} tests in folder {}'.format(len(test_cases),test_folder))

    # Make sure socket doesn't already exist
    try:
        os.unlink(parsec_socket)
    except OSError:
        if os.path.exists(parsec_socket):
            print('Error removing old parsec socket, exiting')
            return

    # Create a unix socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(parsec_socket)

    sock.listen(1)

    while True:
        connection, client_addr = sock.accept()
        try:
            print('Connection received from {}'.format(client_addr))
            received_data = connection.recv(4096)
            b64_received_data = base64.b64encode(received_data).decode('ascii')
            if b64_received_data in test_cases:
                (name, test_case) = test_cases[b64_received_data]
                print('Received expected request for test case {}'.format(name))
                bin_response = base64.b64decode(test_case.test_data.response)
                connection.sendall(bin_response)
            else:
                print('Received unexpected request {}'.format(b64_received_data))
        finally:
            connection.close()


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

def load_tests_from_folder(test_folder):
    tests = {}
    """Read test specs from a folder"""
    specfiles = [f for f in listdir(test_folder) if isfile(join(test_folder, f))]

    for file in specfiles:
        print(f"Parsing spec file: {file}")
        name = file.split('.')[0]
        with open(os.path.join(test_folder, file), 'r') as f:
            spec = safe_load(f)
            testspec = TestSpec(spec)
            tests[testspec.test_data.request] = (name, testspec)

    return tests


if __name__ == "__main__":
    run_test()
