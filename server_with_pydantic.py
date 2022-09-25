import json
import struct
import socket
from typing import Dict, Callable
import connection_details
from info import Info


def __connect(info: Info):
    print(f'Connected, info: {info.info}')


def __server(info: Info):
    print(f'Serving..., info: {info.info}')


def __close(info: Info):
    print(f'Closing, info: {info.info}')


def serve() -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((connection_details.HOST, connection_details.PORT))
    server_socket.listen(1)
    return server_socket


def main():
    connection_handlers: Dict[int, Callable] = {
        1: __connect,
        2: __server,
        3: __close
    }
    server_socket = serve()
    client_socket, address = server_socket.accept()
    connection_type, *_ = struct.unpack('>B', client_socket.recv(1))  # the .unpack function returns a tuple of matches, in our case we only have one value so we ignore the other values.
    connection_handler = connection_handlers.get(connection_type)
    data_size, *_ = struct.unpack('>I', client_socket.recv(4))
    raw_data = client_socket.recv(data_size).decode()
    connection_handler(Info(**json.loads(raw_data)))
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
