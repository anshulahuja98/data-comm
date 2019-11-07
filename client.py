import socket
from crc import *
from constants import *


def main():
    sock = socket.socket()
    sock.connect(('127.0.0.1', SERVER_PORT))

    inp = input("Enter data you want to send->")
    data = str2bits(inp)
    print("Data sent: " + inp)
    encoded_data = crc_encode(data, CRC_KEY)
    print("Encoded data sent: " + encoded_data)

    sock.sendall(encoded_data.encode())

    response = sock.recv(BUFFER_SIZE)
    response = response.decode()
    print("###### RESPONSE RECIEVED FROM SERVER ######")
    print(response)

    sock.close()


if __name__ == '__main__':
    main()
