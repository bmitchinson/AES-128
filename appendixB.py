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
        + "You will be asked to press enter between\n"
        + "rounds. You may compare state as desired\n"
        + "to what is listed in AppendixB.\n"
        + "***********************************************"
    )
    demoPlainTxt = "3243f6a8885a308d313198a2e0370734"
    demoKey = "2b7e151628aed2a6abf7158809cf4f3c"
    input("Press return to begin...")
    result = Encrypt(demoPlainTxt, demoKey, printAllStateChanges=True)
    # TODO: Compair result


appendixB()
