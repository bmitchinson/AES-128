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
        self.currentRound = 0
        self.f = ffield.FField(8, gen=0x11B, useLUT=0)
        print(
            "***********************************************\n"
            + f"Decrypting: {plainTxt}\n"
            + f"Using Key : {key}\n"
            + "***********************************************"
        )
        self.go()

    def go(self):
        roundKeys = keyExpansion(self.key)
        if self.printMode != OFF:
            self.printChanges(
                "initializing state",
                f"round[0].iinput:     {self.state.getStateAsStr()}",
            )

        self.state = addRoundKey(self.state, roundKeys[self.currentRound])
        if self.printMode != OFF:
            self.printChanges(
                "addRoundKey for round 0", f"round[0].ik_sch:     {roundKeys[0]}"
            )

        self.currentRound += 1
        while self.currentRound < 10:
            if self.printMode != OFF:
                if self.printMode == GRID:
                    input(f"Press return to advance to round {self.currentRound}")
                    print()
                self.printChanges(
                    f"the start of {self.currentRound}",
                    f"round[{self.currentRound}].istart:     {self.state.getStateAsStr()}",
                )

            self.state = invSubBytes(self.state)
            if self.printMode != OFF:
                self.printChanges(
                    "subbed bytes using sBox",
                    f"round[{self.currentRound}].is_box:     {self.state.getStateAsStr()}",
                )

            self.state = invShiftRows(self.state)
            if self.printMode != OFF:
                self.printChanges(
                    "shifted rows",
                    f"round[{self.currentRound}].is_row:     {self.state.getStateAsStr()}",
                )

            self.state = invMixColumns(self.state, self.f)
            if self.printMode != OFF:
                self.printChanges(
                    "mixed columns",
                    f"round[{self.currentRound}].im_col:     {self.state.getStateAsStr()}",
                )

            self.state = addRoundKey(self.state, roundKeys[self.currentRound])
            if self.printMode != OFF:
                self.printChanges(
                    f"addRoundKey {self.currentRound}",
                    f"round[{self.currentRound}].ik_sch:     {roundKeys[self.currentRound]}",
                )

            self.currentRound += 1
            # End of Core Loop (rounds 1-9)

        if self.printMode != OFF:
            if self.printMode == GRID:
                input(f"Press return to advance to round {self.currentRound}")
                print()
            self.printChanges(
                f"the start of {self.currentRound}",
                f"round[{self.currentRound}].istart:    {self.state.getStateAsStr()}",
            )

        self.state = invSubBytes(self.state)
        if self.printMode != OFF:
            self.printChanges(
                "subbed bytes using sBox",
                f"round[{self.currentRound}].is_box:    {self.state.getStateAsStr()}",
            )

        self.state = invShiftRows(self.state)
        if self.printMode != OFF:
            self.printChanges(
                "final shift rows",
                f"round[{self.currentRound}].is_row:    {self.state.getStateAsStr()}",
            )

        self.state = addRoundKey(self.state, roundKeys[self.currentRound])
        if self.printMode != OFF:
            self.printChanges(
                "final add round key",
                f"round[{self.currentRound}].ik_sch:    {roundKeys[10]}",
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
            self.printChanges(
                "", f"round[{self.currentRound}].ioutput:   {self.result}"
            )
        if self.printMode == OFF:
            print("Result: " + self.result)

    def printChanges(self, reason, cmode):
        if self.printMode == GRID:
            print(f"state after {reason}:")
            self.state.printStateAsGrid()
        if self.printMode == CMODE:
            print(cmode)
