from concurrent import futures
import logging
import os
import sys

import grpc

sys.path.append(os.path.abspath(f'{os.path.dirname(os.path.abspath(__file__))}/../pb'))

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloResponse(message=f'Hello, {request.name}')


def serve():
    auth_interceptor = AuthServerInterceptor('Password01!')
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=(auth_interceptor,)
    )
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gPRC server stated.')
    server.wait_for_termination()


class AuthServerInterceptor(grpc.ServerInterceptor):
    def __init__(self, token):
        self._valid_metadata = ('authorization', f'Bearer {token}')

    def intercept_service(self, continuition, handler_call_details):
        metadata = handler_call_details.invocation_metadata
        if metadata and metadata[0] == self._valid_metadata:
            return continuition(handler_call_details)
        else:
            return grpc.unary_unary_rpc_method_handler(unauthenticated_process)


def unauthenticated_process(ignored_request, context):
    context.abort(grpc.StatusCode.UNAUTHENTICATED, 'authentication failed.')


if __name__ == '__main__':
    logging.basicConfig()
    serve()
