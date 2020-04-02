from sBox import sBox
from util import xorHexStr


def keyExpansion(key):
    printWordChange = False
    words = [key[:8], key[8:16], key[16:24], key[24:32]]
    # will end up a 44 element array
    i = 4
    if printWordChange:
        for i in range(0, 4):
            print(f"word {i}: {words[i]}")

    rcon = [
        "",
        "01000000",
        "02000000",
        "04000000",
        "08000000",
        "10000000",
        "20000000",
        "40000000",
        "80000000",
        "1b000000",
        "36000000",
    ]
    while i < 44:
        temp = words[i - 1]
        if printWordChange:
            print(f"i: {i}       temp:     {temp}")
        if 4 % 4 == 0:
            rot = rotWord(temp)
            sub = subWord(rot)
            temp = xorHexStr(sub, rcon[i // 4])
            if printWordChange:
                print(f"i: {i} after rot:      {rot}")
                print(f"i: {i} after sub:      {sub}")
                print(f"i: {i} after rcon:     {temp}")
        tempWithFourAgo = xorHexStr(words[i - 4], temp)
        if printWordChange:
            print(f"i: {i} after fourAgo:  {tempWithFourAgo}")
        words.append(tempWithFourAgo)
        i += 1

    roundKeys = wordsToRoundKeys(words)
    return roundKeys


def rotWord(word):
    return word[2:] + word[:2]


def subWord(word):
    first = sBox(word[:2]) + sBox(word[2:4])
    second = sBox(word[4:6]) + sBox(word[6:8])
    return first + second


def wordsToRoundKeys(words):
    roundKeys = []
    i = 0
    while (i < 44):
        roundKeys.append(words[i] + words[i + 1] + words[i + 2] + words[i + 3])
        i += 4
    return roundKeys
