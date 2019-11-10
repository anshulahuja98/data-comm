def manchester_encode(data):
    encrypted_data = ""
    for bit in data:
        if bit == "0":
            encrypted_data += "1-1"
        else:
            encrypted_data += "-11"
    return encrypted_data


def manchester_decode(data):
    bit_data = ""
    for i in range(0, len(data), 3):
        j = i + 3
        bit = data[i:j]
        if bit == "1-1":
            bit_data += "0"
        elif bit == "-11":
            bit_data += "1"
    return bit_data
