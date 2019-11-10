from constants import *


def manchester_encode(data):
    encrypted_data = ""
    for bit in data:
        if bit == "0":
            encrypted_data += MANCHESTER_0
        else:
            encrypted_data += MANCHESTER_1
    return encrypted_data


def manchester_decode(data):
    bit_data = ""
    for i in range(0, len(data), 3):
        j = i + 3
        bit = data[i:j]
        if bit == MANCHESTER_0:
            bit_data += "0"
        elif bit == MANCHESTER_1:
            bit_data += "1"
    return bit_data
