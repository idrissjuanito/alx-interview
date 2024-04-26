#!/usr/bin/python3
""" UTF-8 Validation Module """


def validUTF8(data):
    """ Validates utf-8 encoded chars """
    count = 0
    for i in range(len(data)):
        if not 0 <= data[i] <= 255:
            return False
        if count == 0:
            if (data[i] >> 7) == 0b0:
                continue
            elif (data[i] >> 5) == 0b110:
                count = 1
            elif (data[i] >> 4) == 0b1110:
                count = 2
            elif (data[i] >> 3) == 0b11110:
                count = 3
            else:
                return False
        else:
            if data[i] >> 6 != '0b10':
                return False
            count -= 1
    return (count == 0)
