from Decrypt import Decrypt
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
        + "Using Decrypt.py to decrypt the input given\n"
        + "in AppendixC. The state is tested against the\n"
        + "state in AppendixC of FIPS197 for\n"
        + "for validation.\n"
        + "***********************************************"
    )
    demoPlainTxt = "69c4e0d86a7b0430d8cdb78070b4c55a"
    demoKey = "000102030405060708090a0b0c0d0e0f"
    input("Press return to start: ")
    decrypt = Decrypt(demoPlainTxt, demoKey, printMode=CMODE)

    result = decrypt.result
    appendixCResult = "00112233445566778899aabbccddeeff"
    print("***********************************************")
    print(f"Result matches FIPS197: {result == appendixCResult}")
    print("***********************************************")


appendixC()
