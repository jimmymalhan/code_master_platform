def caesarCipherEncryptor(string, key):
	newLetters = []
	newKey = key % 26 # edge case - when key (is BIG number) then, use - mod (%) 26 
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

# 'ord'  takes in alphaLetter and returns number (unicode value)
# eg:
# a = 97
# z = 122

# 'chr' takes in the number and returns alphaLetter (opposite to 'ord')
def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)