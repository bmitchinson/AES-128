import FField from FField
import keyExpansion from keyExpansion
import subBytes from subBytes
import shiftRows from shiftRows
import mixColumns from mixColumns
import addRoundKey from addRoundKey

class Encrypt():
  def __init__(self, plainTxt, key):
    self.plainTxt = plainTxt
    self.key = key
    self.state = FField(plainTxt)
    self.printStateChanges = True
    self.currentRound = 0
    self.roundKeys = []

  def go(self):
    self.roundKeys = keyExpansion(key)
    addRoundKey(self.state, self.roundKeys[self.currentRound])
    
    # while (self.currentRound < 10):
    #   self.state = subBytes(self.state)
    #   self.state = shiftRows(self.state)
    #   self.state = mixColumns(self.state)
    #   self.state = addRoundKey(self.state, self.roundKeys[self.currentRound])
    #   self.currentRound++
    
    # self.state = subBytes(self.state)
    # self.state = shiftRows(self.state)
    # self.state = addRoundKey(self.state, self.roundKeys[self.currentRound])

    return self.state
