# caesarCipher.py
#
# 2022-12-27
# Rajat Hooja

strKey = "abcdefghijklmnopqrstuvwxyz"
intOffset = 5

strInput = "encode this sample string with a specified offset"
# strInput = "abcdefghijklmnopqrstuvwxyz"

intKeyLength = len(strKey)
strInput = strInput.strip()
strOutput = ""
intNewCharIndex = 0

for charCurrent in strInput:
    if charCurrent.isspace():
        strOutput = strOutput + charCurrent
        continue

    intCurrCharIndex = strKey.index(charCurrent)

    intNewCharIndex = intCurrCharIndex + intOffset

    if intNewCharIndex >= intKeyLength:
        intNewCharIndex = intNewCharIndex - intKeyLength

    charEncoded = strKey[intNewCharIndex]

    strOutput = strOutput + charEncoded

print("original: " + strInput)
print("offset: " + str(intOffset))
print("encoded: " + strOutput)
