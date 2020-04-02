from FField import FField


def hexStrToInt(str):
    return int(str, 16)


def xorHexStr(one, two):
    if len(one) != len(two):
        print("xorHexStr doesn't support mismatch in length")
        print(f"one: {one}")
        print(f"two: {two}")
        exit()
    oneInt = hexStrToInt(one)
    twoInt = hexStrToInt(two)
    res = oneInt ^ twoInt
    hexRes = "{0:#0{1}x}".format(res, len(one) + 2)[2:]
    return hexRes


def addRoundKey(state, roundKey):
    return FField(xorHexStr(state.getStateAsStr(), roundKey))


def printBanner():
    print(
        "    _    _____ ____        _ ____  ___  \n   / \\  | ____/ ___|      / |___ \\( _ ) \n  / _ \\ |  _| \\___ \\ _____| | __) / _ \\ \n / ___ \\| |___ ___) |_____| |/ __/ (_) |\n/_/   \\_\\_____|____/      |_|_____\\___/ \n                                        \n- By Ben Mitchinson\n\nGitHub: bmitchinson\nhttps://mitchinson.dev"
    )
