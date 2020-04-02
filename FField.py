class FField:
    def __init__(self, initState):
        self.state = [
            [initState[0:2], initState[8:10], initState[16:18], initState[24:26]],
            [initState[2:4], initState[10:12], initState[18:20], initState[26:28]],
            [initState[4:6], initState[12:14], initState[20:22], initState[28:30]],
            [initState[6:8], initState[14:16], initState[22:24], initState[30:]],
        ]

    def printStateArrayAsGrid(self):
        s = self.state
        print(
            f"[{s[0][0]}][{s[0][1]}][{s[0][2]}][{s[0][3]}]\n"
            + f"[{s[1][0]}][{s[1][1]}][{s[1][2]}][{s[1][3]}]\n"
            + f"[{s[2][0]}][{s[2][1]}][{s[2][2]}][{s[2][3]}]\n"
            + f"[{s[3][0]}][{s[3][1]}][{s[3][2]}][{s[3][3]}]"
        )

    def getStateArrayAsGridStr(self):
        s = self.state
        con = self.byte2ele
        return (
            f"{con(s[0][0])}{con(s[0][1])}{con(s[0][2])}{con(s[0][3])}"
            + f"{con(s[1][0])}{con(s[1][1])}{con(s[1][2])}{con(s[1][3])}"
            + f"{con(s[2][0])}{con(s[2][1])}{con(s[2][2])}{con(s[2][3])}"
            + f"{con(s[3][0])}{con(s[3][1])}{con(s[3][2])}{con(s[3][3])}"
        )

    def byte2ele(self, ele):
        return ele[0]
