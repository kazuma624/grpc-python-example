import logging
import os
import sys

import grpc

sys.path.append(os.path.abspath(f'{os.path.dirname(os.path.abspath(__file__))}/../pb'))

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    token = 'Password01!'
    metadata = [('authorization', f'Bearer {token}')]

    response = stub.SayHello(
        helloworld_pb2.HelloRequest(name='you'),
        metadata=metadata
    )
    print(f'Greeter client received: {response.message}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
