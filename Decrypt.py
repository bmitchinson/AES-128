from FField import FField
from keyExpansion import keyExpansion
from sBox import invSBox, invSubBytes
from shiftRows import invShiftRows
from mixColumns import invMixColumns
from util import xorHexStr, addRoundKey
from pyfinite import ffield

# Print Enums
OFF = 0
GRID = 1
CMODE = 2


class Decrypt:
    def __init__(self, plainTxt, key, printMode=OFF):
        self.plainTxt = plainTxt
        self.key = key
        self.state = FField(plainTxt)
        self.printMode = printMode
        self.currentRound = 10
        self.f = ffield.FField(8, gen=0x11B, useLUT=0)
        print(
            "***********************************************\n"
            + f"Decrypting: {plainTxt}\n"
            + f"Using Key : {key}\n"
            + "***********************************************"
        )
        self.go()

    def go(self):
        words = keyExpansion(self.key)

        if self.printMode != OFF:
            self.printChanges(
                "initializing state",
                f"round[0].iinput:     {self.state.getStateAsStr()}",
            )

        key = "".join(words[40:44])
        self.state = addRoundKey(self.state, key)
        if self.printMode != OFF:
            self.printChanges(
                f"addRoundKey for round {self.currentRound}",
                f"round[0].ik_sch:     {key}",
            )

        self.currentRound -= 1
        flip = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        while self.currentRound > 0:
            printRound = flip[self.currentRound - 1]
            if self.printMode != OFF:
                if self.printMode == GRID:
                    input(f"Press return to advance to round {self.currentRound}")
                    print()
                self.printChanges(
                    f"the start of {self.currentRound}",
                    f"round[{printRound}].istart:     {self.state.getStateAsStr()}",
                )

            self.state = invShiftRows(self.state)
            if self.printMode != OFF:
                self.printChanges(
                    "shifted rows",
                    f"round[{printRound}].is_row:     {self.state.getStateAsStr()}",
                )

            self.state = invSubBytes(self.state)
            if self.printMode != OFF:
                self.printChanges(
                    "subbed bytes using sBox",
                    f"round[{printRound}].is_box:     {self.state.getStateAsStr()}",
                )

            key = "".join(words[self.currentRound * 4 : (self.currentRound + 1) * 4])
            self.state = addRoundKey(self.state, key)
            if self.printMode != OFF:
                self.printChanges(
                    f"addRoundKey {self.currentRound}",
                    f"round[{printRound}].ik_sch:     {key}",
                )
                self.printChanges(
                    f"addRoundKey {self.currentRound}",
                    f"round[{printRound}].ik_add:     {self.state.getStateAsStr()}",
                )

            self.state = invMixColumns(self.state, self.f)

            self.currentRound -= 1
            # End of Core Loop (rounds 1-9)

        if self.printMode != OFF:
            if self.printMode == GRID:
                input(f"Press return to advance to round {self.currentRound}")
                print()
            self.printChanges(
                f"the start of {self.currentRound}",
                f"round[10].istart:    {self.state.getStateAsStr()}",
            )

        self.state = invShiftRows(self.state)
        if self.printMode != OFF:
            self.printChanges(
                "final shift rows",
                f"round[10].is_row:    {self.state.getStateAsStr()}",
            )

        self.state = invSubBytes(self.state)
        if self.printMode != OFF:
            self.printChanges(
                "subbed bytes using sBox",
                f"round[10].is_box:    {self.state.getStateAsStr()}",
            )

        key = "".join(words[0:4])
        self.state = addRoundKey(self.state, key)
        if self.printMode != OFF:
            self.printChanges(
                "final add round key", f"round[10].ik_sch:    {key}",
            )

        self.result = self.state.getStateAsStr()

        if self.printMode == GRID:
            print(
                "***********************************************\n"
                + f"Final State / Cipher Output\n"
                + "***********************************************"
            )
            self.state.printStateAsGrid()
        if self.printMode == CMODE:
            self.printChanges("", f"round[10].ioutput:   {self.result}")
        if self.printMode == OFF:
            print("Result: " + self.result)

    def printChanges(self, reason, cmode):
        if self.printMode == GRID:
            print(f"state after {reason}:")
            self.state.printStateAsGrid()
        if self.printMode == CMODE:
            print(cmode)
