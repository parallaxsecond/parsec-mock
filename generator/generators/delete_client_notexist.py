# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from .protobuf import delete_client_pb2


def gen():
    operation = delete_client_pb2.Operation()
    operation.client = "not exist"
    result = delete_client_pb2.Result()
    return (operation.SerializeToString(), result.SerializeToString())
