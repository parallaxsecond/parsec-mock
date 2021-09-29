# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from .protobuf import list_opcodes_pb2

def gen():
    operation = list_opcodes_pb2.Operation()
    operation.provider_id = 1

    result = list_opcodes_pb2.Result()
    result.opcodes.extend([1, 3, 2])
    return (operation.SerializeToString(), result.SerializeToString())
