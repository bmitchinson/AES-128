from FField import FField
from keyExpansion import keyExpansion
from sBox import sBox

# from shiftRows import shiftRows
# from mixColumns import mixColumns
from util import xorHexStr


class Encrypt:
    def __init__(self, plainTxt, key, printStateChanges):
        self.plainTxt = plainTxt
        self.key = key
        self.state = FField(plainTxt)
        self.printStateChanges = printStateChanges
        self.currentRound = 0
        self.roundKeys = []
        print(
            "***********************************************\n"
            + f"Encrypting: {plainTxt}\n"
            + f"Using Key : {key}\n"
            + "***********************************************"
        )
        self.go()

    def go(self):
        roundKeys = keyExpansion(self.key)
        if self.printStateChanges:
            print(
                f"round: {self.currentRound}\n"
                + "***********************************************"
            )
            print("state:")
            self.state.printStateAsGrid()
        self.state = FField(xorHexStr(self.state.getStateAsStr(), roundKeys[0]))
        if self.printStateChanges:
            print("state:")
            self.state.printStateAsGrid()

        # while (self.currentRound < 10):
        #   self.state = subBytes(self.state)
        #   self.state = shiftRows(self.state)
        #   self.state = mixColumns(self.state)
        #   self.state = addRoundKey(self.state, self.roundKeys[self.currentRound])
        #   self.currentRound++

        # self.state = subBytes(self.state)
        # self.state = shiftRows(self.state)
        # self.state = addRoundKey(self.state, self.roundKeys[self.currentRound])
