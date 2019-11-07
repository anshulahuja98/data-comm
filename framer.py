from constants import FRAME_FLAG


def create_frame(data):
    frame = ""
    num_bit_1 = 0
    for bit in data:
        if bit == "1":
            num_bit_1 += 1
        else:
            num_bit_1 = 0

        if num_bit_1 == 5:
            num_bit_1 = 0
            frame += "10"
        else:
            frame += bit
    print(frame)
    print(data)
    return FRAME_FLAG + frame + FRAME_FLAG


def de_frame(bit_stream):
    raw_frames = bit_stream.split(FRAME_FLAG)
    for i in raw_frames:
        if not i:
            continue
        count_1 = 0
        data = ""
        for bit in i:
            if count_1 == 5:
                count_1 = 0
                continue
            if bit == "1":
                count_1 += 1
            else:
                count_1 = 0
            data += bit
        return data
