from random import randrange

def induce_error(bit_string):
    bit_list = list(bit_string)
    rand_index = randrange(0, len(bit_string))
    if bit_list[rand_index] =='0':
        bit_list[rand_index] = '1'
    else:
        bit_list[rand_index] = '0'
    error_string  = "".join(bit_list)
    print(rand_index, error_string)
    return error_string