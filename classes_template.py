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

####################
# String
####################

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

####################
# Array
####################

# class graph:
#     def __init__(self, array):
#         self.array = array
    
#     def hasSingleCycle(self):
#         numElementsVisited = 0
#         currentIdx = 0

#         while numElementsVisited < len(self.array):
#             if numElementsVisited > 0 and currentIdx == 0:
#                 return False
#             numElementsVisited += 1
#             currentIdx = self.getNextIndex(currentIdx, self.array)
#         return currentIdx == 0
    
#     def getNextIndex(self, currentIdx, array):
#         jump = self.array[currentIdx]
#         # print(jump) # [2, 1, -4, 2, 3, -4]
#         nextIdx = (currentIdx + jump) % len(self.array)
#         # print(nextIdx) # [2, 3, 5, 1, 4, 0]
#         return nextIdx if nextIdx >= 0 else nextIdx + len(self.array)

# def main():
#     givenArray1 = graph([2, 3, 1, -4, -4, 2])
#     print(givenArray1.hasSingleCycle())

#     givenArray2 = graph([2, 2, -1])
#     print(givenArray2.hasSingleCycle())

# if __name__ == '__main__':
#     main()

####################
# self is the only parameter
####################

# class Solution:
#     def fizzbuzz(self):
#         for i in range(1, 101): # 0 - 100
#             if i % 3 == 0 and i % 5 == 0:
#                 print("Fizz Buzz")
#             elif i % 3 == 0:
#                 print("Fizz")
#             elif i % 5 == 0:
#                 print("Buzz")
#             else:
#                 print(i)

# def main():
#     p1 = Solution()
#     p1.fizzbuzz()

# if __name__ == '__main__':
#     main()