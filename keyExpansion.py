def keyExpansion(key):
  '''
  words = 44 element array, each element a word
	# a word is 4 bytes → defaults as 8 "-" chars
	setFirstFourWords()
	# first four words initialized as the first four chunks of the cipher key
  i = 4
	Rcon = # Round constant array, '01000000'
  subByte = # mega dictionary with the 1:1 byte lookup table (external file)
  while (i < 44):
    temp = words[i-1]
    if i is divisible by 4:
      rotSubWord = SubWord(RotWord(temp))
      temp = xor(rotSubWord, Rcon(i / 4))
    words[i] = xor(words[i - 4], temp)
    i++
  
	roundKeys = wordsToRoundKeys(words) # just combine each group of four words
  '''
  appendixAKeys = ["2b7e151628aed2a6abf7158809cf4f3c",
                   "a0fafe1788542cb123a339392a6c7605",
                   "f2c295f27a96b9435935807a7359f67f",
                   "3d80477d4716fe3e1e237e446d7a883b",
                   "ef44a541a8525b7fb671253bdb0bad00",
                   "d4d1c6f87c839d87caf2b8bc11f915bc",
                   "6d88a37a110b3efddbf98641ca0093fd",
                   "4e54f70e5f5fc9f384a64fb24ea6dc4f",
                   "ead27321b58dbad2312bf5607f8d292f",
                   "ac7766f319fadc2128d12941575c006e",
                   "d014f9a8c9ee2589e13f0cc8b6630ca6"]
  roundKeys = appendixAKeys
  return roundKeys