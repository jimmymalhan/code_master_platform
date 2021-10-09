# caesar cipher encryptor

# Input
string = "xyz"
key = 2

# Output
# "zab"

# Creating your own mapping of letters to codes. In other words, try associating each letter in the alphabet with a specific number -its poistion in the alphbet, for instance - and using that to determine which letters the input string's letters should be mapped to.

# Handle cases:
# - where a letter gets shifted to a position that requires wrapping around the alphabet.
# - where the key is very large and causes multiple wrappings around the alphabet (modulo operator)

# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
	newLetters = []
	newKey = key % 26 # edge case - when key (is BIG number) then, use - mod (%) 26 
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey, alphabet))
	return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
	newLetterCode = alphabet.index(letter) + key
	return alphabet[newLetterCode % 26]

# # O(n) time |  O(n) space
# def caesarCipherEncryptor(string, key):
# 	newLetters = []
# 	newKey = key % 26
# 	for letter in string:
# 		newLetters.append(getNewLetter(letter, newKey))
# 	return "".join(newLetters)

# # 'ord'  takes in alphaLetter and returns number (unicode value)
# # eg:
# # a = 97
# # z = 122

# # 'chr' takes in the number and returns alphaLetter (opposite to 'ord')
# def getNewLetter(letter, key):
# 	newLetterCode = ord(letter) + key
# 	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)