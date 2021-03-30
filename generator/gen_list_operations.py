# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
import protobuf.ping_pb2
import protobuf.list_opcodes_pb2


def gen_list_opcodes_auth_direct():
    operation = protobuf.list_opcodes_pb2.Operation()
    operation.provider_id = 1

    result = protobuf.list_opcodes_pb2.Result()
    result.opcodes.extend([1, 3, 2])
    return (operation.SerializeToString(), result.SerializeToString())
