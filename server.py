import socket
from crc import *
from constants import *
from framer import *
from manchester import *


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
        physical_enc_data_received = request_socket.recv(BUFFER_SIZE)

        if not physical_enc_data_received:
            break
        print("Manchester encoded frame:", physical_enc_data_received.decode())
        frame_received = manchester_decode(physical_enc_data_received.decode())
        data = de_frame(frame_received)
        print("Frame Received :" + frame_received)
        remainder, text = crc_decode(data, CRC_KEY)
        print("Remainder after decoding is->" + remainder)

        if not is_crc_error(remainder):
            msg = "Data Received :" + data + "\nString data: " + text + "\nNo error found!"
            request_socket.sendall(msg.encode())
            print(msg)
        else:
            msg = "Error in data"
            request_socket.sendall(msg.encode())
            print(msg)
        request_socket.close()


if __name__ == '__main__':
    main()
