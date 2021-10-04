# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from .protobuf import list_providers_pb2


def gen():
    operation = list_providers_pb2.Operation()

    result = list_providers_pb2.Result()
    provider_info = list_providers_pb2.ProviderInfo()
    provider_info.uuid = "ee870e5a-ce4a-417f-8543-8fbd84b49cbe"
    provider_info.description = "Some empty provider"
    provider_info.vendor = "Arm Ltd."
    provider_info.version_maj = 9
    provider_info.version_min = 8
    provider_info.version_rev = 7
    provider_info.id = 2
    result.providers.extend([provider_info])
    return (operation.SerializeToString(), result.SerializeToString())
