from Encrypt import Encrypt
from FField import FField
from util import printBanner


def appendixB():
    printBanner()
    print(
        "\n***********************************************\n"
        + "Using Encrypt.py to encrypt the input given\n"
        + "in AppendixB. The result is tested against the\n"
        + "desired result listed in AppendixB of FIPS197\n"
        + "for validation.\n\n"
        + "Would you like to see the datapath between\n"
        + "rounds? You may compare state as desired\n"
        + "this way to what is listed in AppendixB.\n"
        + "***********************************************"
    )
    demoPlainTxt = "3243f6a8885a308d313198a2e0370734"
    demoKey = "2b7e151628aed2a6abf7158809cf4f3c"
    ans = input("Enter Y to see state changes,\nor return to just see the result: ")
    if ans.lower() == "y":
        encrypt = Encrypt(demoPlainTxt, demoKey, printAllStateChanges=True)
    else:
        encrypt = Encrypt(demoPlainTxt, demoKey, printAllStateChanges=False)

    result = encrypt.result
    appendixBResult = "3925841d02dc09fbdc118597196a0b32"
    print("***********************************************")
    print(f"Result matches FIPS197: {result == appendixBResult}")
    print("***********************************************")


appendixB()
