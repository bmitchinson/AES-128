from Encrypt import Encrypt
from FField import FField


def appendixB():
    demoPlainTxt = "3243f6a8885a308d313198a2e0370734"
    demoKey = "2b7e151628aed2a6abf7158809cf4f3c"
    Encrypt(demoPlainTxt, demoKey, printStateChanges=True)


appendixB()
