import socket
import struct

import connection_details
from info import Info


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = Info(info='Hello World! (This time with pydantic 😎)')
    stringified_data = data.json()
    data_size = len(stringified_data.encode())
    data_type = 1
    data_with_details = struct.pack('>B', data_type) + struct.pack('>I', data_size) + stringified_data.encode()
    client_socket.connect((connection_details.HOST, connection_details.PORT))
    client_socket.sendall(data_with_details)


if __name__ == '__main__':
    main()
