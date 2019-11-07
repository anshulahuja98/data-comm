import socket
import binascii
from crc import *
from constants import *


def main():
    sock = socket.socket()
    print("Socket successfully created")

    sock.bind(('', SERVER_PORT))
    print("socket binded to %s" % (SERVER_PORT))
    # put the socket into listening mode
    sock.listen(5)
    print("socket is listening")

    while True:
        c, addr = sock.accept()
        print('Got connection from', addr)

        # Get data from client
        data = c.recv(1024)
        print(data)
        # print(data[:-3])
        # print(binascii.b2a_uu(data[:-3]))
        # print(stringData)

        data = data.decode()

        if not data:
            break

        ans = crc_decode(data, CRC_KEY)
        print("Remainder after decoding is->" + ans)

        # If remainder is all zeros then no error occured
        if not is_crc_error(ans):
            msg = "Data Received :" + data + "\nNo error found!"
            c.sendall(msg.encode())
        else:
            c.sendall("Error in data".encode())
        c.close()


if __name__ == '__main__':
    main()
