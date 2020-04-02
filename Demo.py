from Encrypt import Encrypt
from Decrypt import Decrypt
from FField import FField

class Demo():
  def __init__(self):
    demoPlainTxt = "00112233445566778899aabbccddeeff"
    demoKey = "000102030405060708090a0b0c0d0e0f"
    self.demoEncrypt = Encrypt(demoPlainTxt, demoKey)
    self.demoEncrypt.go()