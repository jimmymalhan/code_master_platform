# caesar cipher encryptor

### returns a new string by shifting every letter in the input string by k poistions in the alphabet, where k is the key

# Sample Input
# string = "xyz"
# key = 2

# Sample Output
# "zab"

# Creating your own mapping of letters to codes. In other words, try associating each letter in the alphabet with a specific number -its poistion in the alphbet, for instance - and using that to determine which letters the input string's letters should be mapped to.

# Handle cases:
# - where a letter gets shifted to a position that requires wrapping around the alphabet.
# - where the key is very large and causes multiple wrappings around the alphabet (modulo operator)

# O(n) time | O(n) space
class Solution:
    def __init__(self, string:str, key:int):
        self.string = string
        self.key = key

    def caesarCipherEncryptor(self):
        newLetters = []
        newKey = self.key % 26
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        for letter in self.string:
            newLetters.append(self.getNewLetter(letter, newKey, alphabet))
        return "".join(newLetters)

    def getNewLetter(self, letter, key, alphabet):
        newLetterCode = alphabet.index(letter) + self.key
        return alphabet[newLetterCode % 26]
            
def main():
    givenString1 = Solution("xyz", 2)
    print(givenString1.caesarCipherEncryptor())
    
if __name__ == '__main__':
    main()

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