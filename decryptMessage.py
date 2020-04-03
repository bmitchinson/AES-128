
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
        + "Using Decrypt.py to decrypt the your input\n"
        + "***********************************************"
    )
    print("Enter Ciphertext:F4351503AA781C520267D690C42D1F43")
    print("       Enter Key:303132333435363738393A3B3C3D3E3F")
    demoPlainTxt = "F4351503AA781C520267D690C42D1F43"
    demoKey = "303132333435363738393A3B3C3D3E3F"
    decrypt = Decrypt(demoPlainTxt, demoKey, printMode=CMODE)

    result = decrypt.result
    print("***********************************************")
    print(f"Result: {result}")
    print("***********************************************")


customDecrypt()