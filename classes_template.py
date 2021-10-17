class Solution:
    def __init__(self, string: str):
        self.string = string

    def toQuestion(self):
        pass
            
def main():
    givenString1 = Solution("enter_string")
    print(givenString1.toQuestion())

    givenString2 = Solution("enter_2nd_string")
    print(givenString2.toQuestion())

if __name__ == '__main__':
    main()

# class Solution:
#     def __init__(self, string:str, key:int) -> int:
#         self.string = string
#         self.key = key

#     def caesarCipherEncryptor(self):
#         newLetters = []
#         newKey = self.key % 26
#         alphabet = list("abcdefghijklmnopqrstuvwxyz")
#         for letter in self.string:
#             newLetters.append(self.getNewLetter(letter, newKey, alphabet)) # this function calls it's sub function
#         return "".join(newLetters)

#     def getNewLetter(self, letter, key, alphabet):
#         newLetterCode = alphabet.index(letter) + self.key
#         return alphabet[newLetterCode % 26]
            
# def main():
#     givenString1 = Solution("xyz", 2)
#     print(givenString1.caesarCipherEncryptor())
#     # don't need to call getNewLetter sub function

# if __name__ == '__main__':
#     main()