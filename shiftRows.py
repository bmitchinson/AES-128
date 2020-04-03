from FField import FField


def shiftRows(state):
    s = state.state
    newStateStr = f"{s[0][0]}{s[1][1]}{s[2][2]}{s[3][3]}{s[0][1]}{s[1][2]}{s[2][3]}{s[3][0]}{s[0][2]}{s[1][3]}{s[2][0]}{s[3][1]}{s[0][3]}{s[1][0]}{s[2][1]}{s[3][2]}"
    return FField(newStateStr)


def invShiftRows(state):
    s = state.state
    newStateStr = f"{s[0][0]}{s[1][1]}{s[2][2]}{s[3][3]}{s[0][3]}{s[1][0]}{s[2][1]}{s[3][2]}{s[0][2]}{s[1][3]}{s[2][0]}{s[3][1]}{s[0][1]}{s[1][2]}{s[2][3]}{s[3][0]}"
    return FField(newStateStr)
