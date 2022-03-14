from concurrent import futures

import grpc
import logging
import time
import sys

sys.path.append("/Users/guotongning/my_project/gRpc_Demo/rpc_package")

from rpc_package.hello_world_pb2_grpc import add_HelloWorldServiceServicer_to_server, HelloWorldServiceServicer

from rpc_package.hello_world_pb2 import HelloReply


class Hello(HelloWorldServiceServicer):
    # 在这里实现定义好的接口
    def SayHello(self, request, context):
        return HelloReply(message='Hello, %s' % request.name)


def server_start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_HelloWorldServiceServicer_to_server(Hello(), server)

    # 这里使用的非安全接口，实际上gRPC支持TLS/SSL安全连接，以及各种鉴权机制
    server.add_insecure_port('[::]:50000')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    server_start()
