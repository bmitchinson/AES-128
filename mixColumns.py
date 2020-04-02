from FField import FField
from pyfinite import ffield


def mixColumns(state, f):
    s = state.state
    oldCols = [
        [con(s[0][0]), con(s[1][0]), con(s[2][0]), con(s[3][0])],
        [con(s[0][1]), con(s[1][1]), con(s[2][1]), con(s[3][1])],
        [con(s[0][2]), con(s[1][2]), con(s[2][2]), con(s[3][2])],
        [con(s[0][3]), con(s[1][3]), con(s[2][3]), con(s[3][3])],
    ]

    newCols = []

    for oldCol in oldCols:
        tmp = [
            hex(
                f.Multiply(2, oldCol[0])
                ^ f.Multiply(3, oldCol[1])
                ^ oldCol[2]
                ^ oldCol[3]
            ),
            hex(
                oldCol[0]
                ^ f.Multiply(2, oldCol[1])
                ^ f.Multiply(3, oldCol[2])
                ^ oldCol[3]
            ),
            hex(
                oldCol[0]
                ^ oldCol[1]
                ^ f.Multiply(2, oldCol[2])
                ^ f.Multiply(3, oldCol[3])
            ),
            hex(
                f.Multiply(3, oldCol[0])
                ^ oldCol[1]
                ^ oldCol[2]
                ^ f.Multiply(2, oldCol[3])
            ),
        ]
        for j in range(0, 4):
            tmp[j] = "{0:#0{1}x}".format(int(tmp[j], 16), 4)[2:]
        newCols.append(tmp)

    newState = FField("--------------------------------")
    newState.state = [
        [newCols[0][0], newCols[1][0], newCols[2][0], newCols[3][0]],
        [newCols[0][1], newCols[1][1], newCols[2][1], newCols[3][1]],
        [newCols[0][2], newCols[1][2], newCols[2][2], newCols[3][2]],
        [newCols[0][3], newCols[1][3], newCols[2][3], newCols[3][3]],
    ]
    return newState


def con(ele):
    return int(ele, 16)
