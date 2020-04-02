def hexStrToInt(str):
    return int(str, 16)


def xorHexStr(one, two):
    if len(one) != len(two):
        print("xorHexStr doesn't support mismatch in length")
        print(f'one: {one}')
        print(f'two: {two}')
        exit()
    oneInt = hexStrToInt(one)
    twoInt = hexStrToInt(two)
    res = oneInt ^ twoInt
    hexRes = "{0:#0{1}x}".format(res,len(one) + 2)[2:]
    return hexRes
