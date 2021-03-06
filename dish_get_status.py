#!/usr/bin/python3

"""Simple example of get_status request using grpc call directly."""

import grpc

from spacex.api.device import device_pb2
from spacex.api.device import device_pb2_grpc

with grpc.insecure_channel("192.168.100.1:9200") as channel:
    stub = device_pb2_grpc.DeviceStub(channel)
    response = stub.Handle(device_pb2.Request(get_status={}))

print(response.dish_get_status)
