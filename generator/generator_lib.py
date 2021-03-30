# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
from gen_list_operations import gen_list_opcodes_auth_direct
from gen_ping_operations import gen_ping_no_auth


# Dictionary for generators.  The values in this dictionary must be functions to produce a tuple
# (operation, result) of binary strings.
generators = {
    'ping_no_auth': gen_ping_no_auth,
    'list_opcodes_auth_direct': gen_list_opcodes_auth_direct,
}
