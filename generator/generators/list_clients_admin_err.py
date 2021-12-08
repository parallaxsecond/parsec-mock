# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from .protobuf import list_clients_pb2


def gen():
    operation = list_clients_pb2.Operation()

    result = list_clients_pb2.Result()
    return (operation.SerializeToString(), result.SerializeToString())
