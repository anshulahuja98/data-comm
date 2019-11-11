import socket
from crc import *
from constants import *
from framer import *
from manchester import *
from error import induce_error


def main():
    inp = ""
    while inp != 'qq':
        sock = socket.socket()
        sock.connect(('127.0.0.1', SERVER_PORT))
        inp = input("Enter data to send: ")
        data = str2bits(inp)
        print("Data : " + inp)
        encoded_data = crc_encode(data, CRC_KEY)
        print("Encoded data: " + encoded_data)
        op = input("Induce error in data to be sent? (y/n) ")
        if op == "y":
            encoded_data = induce_error(encoded_data)
        frame = create_frame(encoded_data)
        print("Frame sent: " + frame)
        physical_enc_data = manchester_encode(frame)
        print("Manchester encoded frame: " + physical_enc_data)

        sock.sendall(physical_enc_data.encode())

        response = sock.recv(BUFFER_SIZE)
        response = response.decode()
        print("###### RESPONSE RECIEVED FROM SERVER ######")
        print(response)

        sock.close()


if __name__ == '__main__':
    main()
