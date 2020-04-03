from keyExpansion import keyExpansion
from util import printBanner


def appendixA():
    printBanner()
    passing = True
    print(
        "\n***********************************************\n"
        + "Generating 44 words through keyExpansion.py\n\n"
        + "Each will be compared to the word generated\n"
        + "in AppendixA of FIPS 197 for validation.        \n"
        + "***********************************************\n"
    )
    cipherKey = "2b7e151628aed2a6abf7158809cf4f3c"
    words = keyExpansion(cipherKey)
    appendixAWords = [
        "2b7e1516",
        "28aed2a6",
        "abf71588",
        "09cf4f3c",
        "a0fafe17",
        "88542cb1",
        "23a33939",
        "2a6c7605",
        "f2c295f2",
        "7a96b943",
        "5935807a",
        "7359f67f",
        "3d80477d",
        "4716fe3e",
        "1e237e44",
        "6d7a883b",
        "ef44a541",
        "a8525b7f",
        "b671253b",
        "db0bad00",
        "d4d1c6f8",
        "7c839d87",
        "caf2b8bc",
        "11f915bc",
        "6d88a37a",
        "110b3efd",
        "dbf98641",
        "ca0093fd",
        "4e54f70e",
        "5f5fc9f3",
        "84a64fb2",
        "4ea6dc4f",
        "ead27321",
        "b58dbad2",
        "312bf560",
        "7f8d292f",
        "ac7766f3",
        "19fadc21",
        "28d12941",
        "575c006e",
        "d014f9a8",
        "c9ee2589",
        "e13f0cc8",
        "b6630ca6",
    ]
    i = 0
    for word in words:
        if word is words[43]:
            print(f"Round {str(i)} word: {word}")
        else:
            print(f"Round {str(i)}  word: {word}")
        print(f"Matches Appendix A: {word == appendixAWords[i]}")
        if word != appendixAWords[i]:
            passing = False
        i += 1

    print(
        "\n***********************************************\n"
        + f"Appendix A Complete Match (Tests Pass): {passing}\n"
        + "***********************************************\n"
    )
    return passing


appendixA()
