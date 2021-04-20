#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2020/07/10 15:05:18
@Desc    :   None
'''

# here put the import lib
from concurrent import futures
import logging
import grpc
import helloworld, helloworld_pb2_grpc

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(helloworld.Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    server()