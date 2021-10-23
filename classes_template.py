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

# class Dictionary:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary

#     def sort_ascending(self):
#         return sorted(self.dictionary.items(), key=lambda x: x[1])

#     def sort_descending(self):
#         return sorted(self.dictionary.items(), key=lambda x: x[1], reverse=True)

# def main():
#     dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(Dictionary(dictionary).sort_ascending())
#     print(Dictionary(dictionary).sort_descending())

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

#########
# # Max Subarray with Unit Test
#########
# """ Note:
# Kadane's Algorithm
# """

# Max Subarray

# # O(n) time, O(1) space
# class Solution:
#     def maxSubArray(self, nums) -> int:
#         max_sum, current_sum = -float('inf'), 0    
#         for num in nums:   
#             current_sum = max(num, current_sum + num) # if nums > current_sum + nums, then current_sum + nums is the new current_sum
#             max_sum = max(current_sum, max_sum) # if current_sum > max_sum, then current_sum is the new max_sum    
#         return max_sum

# import unittest
# class Test(unittest.TestCase):
#     def test(self):
#         test = Solution()
#         nums = [-2,1,-3,4,-1,2,1,-5,4]
#         self.assertEqual(test.maxSubArray(nums), 6)
#     def test2(self):
#         test = Solution()
#         nums = [-2,1]
#         self.assertEqual(test.maxSubArray(nums), 1)
# def main():
#     unittest.main()

# if __name__ == "__main__":
#     main()