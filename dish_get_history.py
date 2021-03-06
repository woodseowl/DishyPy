#!/usr/bin/python3

"""Simple example of get_history request using grpc call directly."""

# NOTE: The response can be large. Be patient.

import grpc

from spacex.api.device import device_pb2
from spacex.api.device import device_pb2_grpc

with grpc.insecure_channel("192.168.100.1:9200") as channel:
    stub = device_pb2_grpc.DeviceStub(channel)
    response = stub.Handle(device_pb2.Request(get_history={}))

print(response.dish_get_history)
