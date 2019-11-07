import socket
from crc import *
from constants import *
from framer import *


def main():
    sock = socket.socket()
    print("Socket successfully created")

    sock.bind(('', SERVER_PORT))
    print("Server socket binded to %s" % (SERVER_PORT))
    sock.listen(10)
    print("Server is listening for requests on %s" % (SERVER_PORT))

    while True:
        request_socket, request_address = sock.accept()
        print("Incoming connection from ", request_address)
        encoded_frame_received = request_socket.recv(BUFFER_SIZE)

        if not encoded_frame_received:
            break

        frame_received = encoded_frame_received.decode()
        data = de_frame(frame_received)

        remainder, text = crc_decode(data, CRC_KEY)
        print("Data Received :" + data + "\nString data: " + text + "\nNo error found!")
        print("Remainder after decoding is->" + remainder)

        if not is_crc_error(remainder):
            msg = "Data Received :" + data + "\nString data: " + text + "\nNo error found!"
            request_socket.sendall(msg.encode())
        else:
            request_socket.sendall("Error in data".encode())
        request_socket.close()


if __name__ == '__main__':
    main()
