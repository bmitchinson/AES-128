from FField import FField
from keyExpansion import keyExpansion
from sBox import sBox, subBytes
from shiftRows import shiftRows
from mixColumns import mixColumns
from util import xorHexStr, addRoundKey


class Encrypt:
    def __init__(self, plainTxt, key, printAllStateChanges):
        self.plainTxt = plainTxt
        self.key = key
        self.state = FField(plainTxt)
        self.printAllStateChanges = printAllStateChanges
        self.currentRound = 0
        print(
            "***********************************************\n"
            + f"Encrypting: {plainTxt}\n"
            + f"Using Key : {key}\n"
        )
        self.go()

    def go(self):
        roundKeys = keyExpansion(self.key)
        if self.printAllStateChanges:
            self.printRound()
            self.printChanges("initializing state")

        self.state = addRoundKey(self.state, roundKeys[self.currentRound])
        if self.printAllStateChanges:
            self.printChanges("adding round 0 addRoundKey")
        self.currentRound += 1
        while self.currentRound < 10:
            input(f"Press return to advance to round {self.currentRound}")
            if self.printAllStateChanges:
                self.printRound()
                self.printChanges(f"state at the start of round {self.currentRound}")

            self.state = subBytes(self.state)
            if self.printAllStateChanges:
                self.printChanges("subbed bytes using sBox")

            self.state = shiftRows(self.state)
            if self.printAllStateChanges:
                self.printChanges("shifted rows")

            self.state = mixColumns(self.state)
            if self.printAllStateChanges:
                self.printChanges("shifted rows")

            self.state = addRoundKey(self.state, roundKeys[self.currentRound])
            if self.printAllStateChanges:
                self.printChanges(f"adding round key {self.currentRound}")

            self.currentRound += 1
            # End of Core Loop (rounds 1-9)

        input(f"Press return to advance to round {self.currentRound} (final round)")

        self.state = subBytes(self.state)
        if self.printAllStateChanges:
            self.printChanges("final byteSub using sBox")
        self.state = shiftRows(self.state)
        if self.printAllStateChanges:
            self.printChanges("final shift rows")
        self.state = addRoundKey(self.state, roundKeys[self.currentRound])
        if self.printAllStateChanges:
            self.printChanges("final add round key")
        if self.printAllStateChanges:
            print(
                "***********************************************\n"
                + f"Final State / Cipher Output\n"
                + "***********************************************"
            )
            self.state.printStateAsGrid()

    def printChanges(self, reason):
        print(f"state after {reason}:")
        self.state.printStateAsGrid()

    def printRound(self):
        print(
            "***********************************************\n"
            + f"round: {self.currentRound}\n"
            + "***********************************************"
        )
