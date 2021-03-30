# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
import protobuf.ping_pb2
import protobuf.list_opcodes_pb2


def gen_ping_no_auth():
    op = protobuf.ping_pb2.Operation()
    result = protobuf.ping_pb2.Result()
    result.wire_protocol_version_maj = 1
    result.wire_protocol_version_min = 0

    return (op.SerializeToString(), result.SerializeToString())
