#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   helloworld.py
@Time    :   2020/07/10 15:06:25
@Desc    :   None
'''

# here put the import lib
from grpc_example.protos import helloworld_pb2
from grpc_example.protos import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterGreeterServicer):
    
    def SayHello(self, request, context):
        return helloworld_pb2.HelloResponse(message="Hello, %s!" % request.name)



