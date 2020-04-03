from Encrypt import Encrypt
from util import printBanner

# Print Enums
OFF = 0
GRID = 1
CMODE = 2


def customEncrypt():
    printBanner()
    print(
        "\n***********************************************\n"
        + "Using Encrypt.py to encrypt your input\n"
        + "***********************************************"
    )
    demoPlainTxt = input("Enter PlainTxt:")
    demoKey = input("     Enter Key:")
    while len(demoPlainTxt) != 32 or len(demoKey) != 32:
        print("please make sure both inputs are 16 bytes of hex")
        demoPlainTxt = input("Enter PlainTxt:")
        demoKey = input("     Enter Key:")
    encrypt = Encrypt(demoPlainTxt, demoKey, printMode=CMODE)

    result = encrypt.result
    print("***********************************************")
    print(f"Result: {result}")
    print("***********************************************")


customEncrypt()
