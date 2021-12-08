# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from .protobuf import list_authenticators_pb2


def gen():
    operation = list_authenticators_pb2.Operation()

    result = list_authenticators_pb2.Result()
    auth_info = list_authenticators_pb2.AuthenticatorInfo()
    auth_info.description = "direct auth"
    auth_info.version_maj = 12
    auth_info.version_min = 42
    auth_info.id = 1
    result.authenticators.extend([auth_info])
    return (operation.SerializeToString(), result.SerializeToString())
