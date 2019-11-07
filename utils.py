def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


# Modulo-2 division
def mod2div(divident, divisor):
    pick = len(divisor)

    tmp = divident[0: pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def str2bits(string):
    res = ""
    for x in string:
        bits = ''.join(format(ord(x), 'b'))
        while len(bits) != 8:
            bits = '0' + bits
        res += str(bits)
    return res


def bits2str(string):
    data = ""
    for i in range(0, len(string), 8):
        j = min(i + 8, len(string))
        char = chr(int(string[i:j], 2))
        data += char
    return data
