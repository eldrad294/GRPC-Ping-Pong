from google.protobuf import message
import pp_pb2, pp_pb2_grpc
import grpc
import time

def run():
    with grpc.insecure_channel("localhost:80") as channel:
        stub = pp_pb2_grpc.PPServiceStub(channel)
        while True:
            print("Sending Ping, Receiving Pong")
            stub.ping(pp_pb2.Ping(message="Ping"))
            time.sleep(1)

if __name__ == "__main__":
    run()