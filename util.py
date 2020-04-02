def hexStrToInt(str):
    return int(str, 16)


def xorHexStr(one, two):
    res = int(one, 16) ^ int(two, 16)
    return hex(res)[2:]
