from Decrypt import Decrypt
from util import printBanner

# Print Enums
OFF = 0
GRID = 1
CMODE = 2


def customDecrypt():
    printBanner()
    print(
        "\n***********************************************\n"
        + "Using Decrypt.py to decrypt your input\n"
        + "***********************************************"
    )
    demoPlainTxt = input("Enter Ciphertext:")
    demoKey = input("       Enter Key:")
    while len(demoPlainTxt) != 32 or len(demoKey) != 32:
        print("please make sure both inputs are 16 bytes of hex")
        demoPlainTxt = input("Enter PlainTxt:")
        demoKey = input("     Enter Key:")
    decrypt = Decrypt(demoPlainTxt, demoKey, printMode=CMODE)

    result = decrypt.result
    print("***********************************************")
    print(f"Result: {result}")
    print("***********************************************")


customDecrypt()
