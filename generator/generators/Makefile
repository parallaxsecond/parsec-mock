# Copyright 2021 Contributors to the Parsec project.
# SPDX-License-Identifier: Apache-2.0
PROTOC_OUTPUT_FILES=$(shell find parsec-operations/protobuf/ -name "*.proto" -exec basename {} .proto \; | awk '{print "protobuf/"$$1"_pb2.py"}')
.PHONY: protobuf all

all: protobuf

protobuf: ${PROTOC_OUTPUT_FILES}

protobuf/%_pb2.py: parsec-operations/protobuf/%.proto
	@protoc -I=parsec-operations/protobuf --python_out=protobuf $< > /dev/null
