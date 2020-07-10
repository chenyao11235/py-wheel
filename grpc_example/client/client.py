#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client.py
@Time    :   2020/07/10 15:22:04
@Desc    :   None
'''

# here put the import lib
from __future__ import print_function
import logging

import grpc
from grpc_example.protos import helloworld_pb2
from grpc_example.protos import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="chenyao"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig
    run()