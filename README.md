<p align="center">
  <a href="/"><img align="center" width="400" src="https://i.imgur.com/IFiBDHe.png"></a>
  <h1 align="center">🔒 AES-128 🐍</h1>
</p>
<p align="center">
  An implementation of AES-128 in python from scratch, with several demos to verify it's accuracy against <a href="https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf">FIPS197</a>. 
</p>

---

## 💻 Getting Started - ([Skip this and use an Online Sandbox!](https://aes-128.bmitchinson.repl.run/))
To run the demos, you'll need a version of python 3 installed] (I used 3.8). Required libraries are listed in [`requirements.txt`](https://github.com/bmitchinson/AES-128/blob/master/requirements.txt) and can be installed with `pip install -r requirements.txt` from the root directory of the project.
- If you're on an osx system with multiple versions of python installed, note that you might need to specify `pip3 install -r requirements.txt`

**If the following setup instructions do not work for your machine, feel free to test out each demo and explore the codebase in an online sandbox linked to this repository, [available here](https://repl.it/@bmitchinson/AES-128). No setup needed.**

Afterwards, you may load any of the following demos.

## 🔑 Demos (7 of them)
You may run any of the following scripts after setup has been complete. Use `python {filename}` to start each one. 
- or `python3 {filename}` if you're on osx or running in the online sandbox.

If you have not followed the pip install step in the above "Getting Started" section, the following demos will not function properlly.

### FIPS197 Appendix Verificaions
- `python appendixA.py` will print each of the words generated in the process of keyExpansion. The output of the test vector is validated against the documented outcome in FIPS197.
- `python appendixB.py` will show the user 4x4 grids of the datapath for comparision to Appendix B of FIPS197. It's final outcome is validated.
- `python appendixC-Encrypt.py` completes the appendixC demonstration of encryption, and validates the result.
- `python appendixC-Decrypt.py` completes the appendixC demonstration of decryption, and validates the result.

### Additional
- `python customDecrypt.py` will propmpt the user for their own 16 byte hex ciphertext + Key, and will decrypt the ciphertext while printing the data pathway.
- `python customEncrypt.py` will propmpt the user for their own 16 byte hex plaintext + Key, and will encrypt the plaintext while printing the data pathway.
- `python decryptMessage.py` will decrypt the message instructed to decrypt in the original assignment, while printing the data pathway as required.


**Note:** On any of the following demos, you may change how the datapath of the algorithm is represented along the way. In the demo file you'd like to run, in either the Decrypt or Encrypt method, change the `printMode` parameter to one of the values listed at the top of the file.
- OFF: Will simply finish the demo as soon as possible, with little insight into state
- GRID: Will show state 4x4 squares as the demo progresses, with a description of each change.
<p align="center">
  <img align="center" width="300" src="https://i.imgur.com/rMmGXN7.png">
</p>

- CMODE: (Default) Will show the state listed as a 32 character length string, as shown in AppendixC of FIPS 197. 

## 📝 Documentation
### [Code Structure](https://github.com/bmitchinson/AES-128/wiki/Code-Structure)
### [AES Overview](https://github.com/bmitchinson/AES-128/wiki/AES-Overview)
### [Report that combines both into one document](https://github.com/bmitchinson/AES-128/wiki.pdf)
