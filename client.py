import socket
from crc import *
from constants import *


def main():
    sock = socket.socket()
    sock.connect(('127.0.0.1', SERVER_PORT))

    input_string = input("Enter data you want to send->")
    # s.sendall(input_string)
    data = (''.join(format(ord(x), 'b') for x in input_string))
    print(data)
    ans = crc_encode(data, CRC_KEY)
    print(ans)
    sock.sendall(ans.encode())

    # receive data from the server
    # print
    l = sock.recv(1024)
    l = l.decode()
    print(l)

    sock.close()


if __name__ == '__main__':
    main()
