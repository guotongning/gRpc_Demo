from __future__ import print_function

import logging
import grpc
import sys

sys.path.append("/Users/guotongning/my_project/gRpc_Demo/rpc_package")
from rpc_package.hello_world_pb2 import HelloRequest, HelloReply
from rpc_package.hello_world_pb2_grpc import HelloWorldServiceStub


def run():
    with grpc.insecure_channel('localhost:50000') as channel:
        stub = HelloWorldServiceStub(channel)
        response = stub.SayHello(HelloRequest(name='陈虹繁'))
    print("hello client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
