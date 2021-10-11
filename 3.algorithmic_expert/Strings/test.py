class MyClass:
    def __init__(self, string:str) -> bool:
        self.string = string
		
    def isPalindrome(self):
        reversedString = ""
        for i in reversed(range(len(self.string))):
            reversedString += self.string[i] # creating newString -> increases time
        return self.string == reversedString

def main():
    stringName = MyClass("abcdcba")
    print(stringName.isPalindrome())
    example2 = MyClass("abcdcb")
    print(example2.isPalindrome())

if __name__ == '__main__':
	main()

# class MyClass:
# 	def __init__(self, string, key):
#     	self.string = string
#     	self.key = key
		
# 	def caesarCipherEncryptor(self):
# 		newLetters = []
# 		newKey = self.key % 26 # edge case - when key (is BIG number) then, use - mod (%) 26 
# 		alphabet = list("abcdefghijklmnopqrstuvwxyz")
# 		for letter in self.string:
# 			newLetters.append(getNewLetter(letter, newKey, alphabet))
# 		return "".join(newLetters)

# 	def getNewLetter(letter, key, alphabet):
# 		newLetterCode = alphabet.index(letter) + self.key
# 		return alphabet[newLetterCode % 26]

# def main():
# 	print(MyClass("xyz", 2).caesarCipherEncryptor())

# if __name__ == '__main__':
# 	main()