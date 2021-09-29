import grpc
import pp_pb2, pp_pb2_grpc
from concurrent import futures
import time


class Listener(pp_pb2_grpc.PPServiceServicer):

    def __init__(self):
        pass

    def ping(self, request, context):
        print("Received Ping, Sending Pong")
        return pp_pb2.Pong(message="Pong")

def serve():
    """Main server function. Opens socket and listens for incoming grpc packets"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pp_pb2_grpc.add_PPServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:80")
    server.start()
    try:
        while True:
            print("Running...")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Encountered KeyboardInterrupt, terminating.")
        server.stop()

if __name__ == "__main__":
    serve()
