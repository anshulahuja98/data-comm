from utils import *
from constants import *


def crc_decode(data, key):
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    text = bits2str(data[:-len(CRC_KEY)+1])
    return remainder, text


def crc_encode(data, key):
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    # Append remainder in the original data
    codeword = data + remainder
    return codeword


def is_crc_error(ans):
    temp = "0" * (len(CRC_KEY) - 1)
    if ans == temp:
        return False
    else:
        return True
