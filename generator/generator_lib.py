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

def gen_list_opcodes_auth_direct():
    op = protobuf.list_opcodes_pb2.Operation()
    op.provider_id = 1

    result = protobuf.list_opcodes_pb2.Result()
    result.opcodes.extend([1,3,2])
    return (op.SerializeToString(), result.SerializeToString())

generators = {
    'ping_no_auth': gen_ping_no_auth,
    'list_opcodes_auth_direct': gen_list_opcodes_auth_direct,
}
