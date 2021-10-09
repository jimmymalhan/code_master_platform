class MyClass:
	# def __init__(self, string, key):
    # 	self.string = string
    # 	self.key = key
		
	def caesarCipherEncryptor(self):
		newLetters = []
		newKey = self.key % 26 # edge case - when key (is BIG number) then, use - mod (%) 26 
		alphabet = list("abcdefghijklmnopqrstuvwxyz")
		for letter in self.string:
			newLetters.append(getNewLetter(letter, newKey, alphabet))
		return "".join(newLetters)

	def getNewLetter(letter, key, alphabet):
		newLetterCode = alphabet.index(letter) + self.key
		return alphabet[newLetterCode % 26]

def main():
	print(MyClass("xyz", 2).caesarCipherEncryptor())

if __name__ == '__main__':
	main()