from Encrypt import Encrypt
from FField import FField
from util import printBanner

# Print Enums
OFF = 0
GRID = 1
CMODE = 2


def appendixC():
    printBanner()
    print(
        "\n***********************************************\n"
        + "Using Encrypt.py to encrypt the input given\n"
        + "in AppendixC. The state is tested against the\n"
        + "state in AppendixC of FIPS197 for\n"
        + "for validation.\n"
        + "***********************************************"
    )
    demoPlainTxt = "00112233445566778899aabbccddeeff"
    demoKey = "000102030405060708090a0b0c0d0e0f"
    input("Press return to start: ")
    encrypt = Encrypt(demoPlainTxt, demoKey, printMode=CMODE)

    result = encrypt.result
    appendixCResult = "69c4e0d86a7b0430d8cdb78070b4c55a"
    print("***********************************************")
    print(f"Result matches FIPS197: {result == appendixCResult}")
    print("***********************************************")


appendixC()
