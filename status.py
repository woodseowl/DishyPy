#!/usr/bin/python3
"""Simple example of get_status request using grpc call directly."""

import grpc

from spacex.api.device import device_pb2
from spacex.api.device import device_pb2_grpc

# Note that if you remove the 'with' clause here, you need to separately
# call channel.close() when you're done with the gRPC connection.
with grpc.insecure_channel("192.168.100.1:9200") as channel:
    stub = device_pb2_grpc.DeviceStub(channel)
    response = stub.Handle(device_pb2.Request(get_status={}))

status = {
    'state': response.dish_get_status.state,
    'down': round(response.dish_get_status.downlink_throughput_bps/1000000, 2),
    'up': round(response.dish_get_status.uplink_throughput_bps/1000000, 2),
    'ping': round(response.dish_get_status.pop_ping_latency_ms),
}

print(status)
