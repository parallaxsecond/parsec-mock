# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from .protobuf import ping_pb2


def gen():
    op = ping_pb2.Operation()
    result = ping_pb2.Result()
    result.wire_protocol_version_maj = 1
    result.wire_protocol_version_min = 0

    return (op.SerializeToString(), result.SerializeToString())
