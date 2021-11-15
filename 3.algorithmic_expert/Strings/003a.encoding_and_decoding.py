# compress and decompress string in python

# approach:

# class Solution:
#     def __init__(self):
#         self.dic = {}
#         self.count = 0
#         self.compressed = ''
#         self.decompressed = ''

#     def compress(self, s):
#         self.count = 0
#         self.dic = {}
#         for i in range(len(s)): # i is the index of s
#             if s[i] not in self.dic: # if s[i] is not in dic
#                 self.dic[s[i]] = 1 # add s[i] to dic
#             else:
#                 self.dic[s[i]] += 1 # if s[i] is in dic, add 1 to the value
#         for key in self.dic: # for each key in dic
#             if self.dic[key] == 1: # if the value of key is 1
#                 self.compressed += key # add key to compressed
#             else: # if the value of key is not 1
#                 self.compressed += key + str(self.dic[key]) # add key and value to compressed
#         return self.compressed

#     def decompress(self, s):
#         #input: a3b4c3
#         #output: aaabbbbccc
#         start = 0
#         end = 0
#         while end < len(s): # while end is less than the length of s
#             while end < len(s) and not s[end].isdigit(): # if s[end] is not a digit
#                 end += 1 # add 1 to end
#             self.decompressed += s[start:end] * int(s[end]) # add s[start:end] * int(s[end]) to decompressed # s[end] is a digit
#             start = end + 1 # start is the index of s after end
#             end = start # end is the index of s after start
#         return self.decompressed



# def main():
#     s = Solution()
#     print(s.compress('aaabbbbccc'))
#     print(s.decompress('a3b4c3'))

# if __name__ == '__main__':
#     main()

#################################################################
# Method 1 (using 2 stacks)

# decode a string
# input = "3[b2[ca]]"
# output = bcacabcacabcaca

# Method 1(Using 2 stacks)
# The idea is to use two stacks, one for integers and another for characters. 
# Now, traverse the string, 

# Whenever we encounter any number, push it into the integer stack and in case of any alphabet (a to z) or open bracket (‘[‘), push it onto the character stack.
# Whenever any close bracket (‘]’) is encounter pop the character from the character stack until open bracket (‘[‘) is not found in the character stack. Also, pop the top element from the integer stack, say n. Now make a string repeating the popped character n number of time. Now, push all character of the string in the stack.


# O(n) time | O(n) space
class Solution:
    def decodeString(self, s: str) -> str:
        integerstack = []
        stringstack = []
        temp = ""
        result = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                integerstack.append(int(s[i]))
                i += 1
            elif s[i] == "[":
                stringstack.append(temp)
                temp = ""
                i += 1
            elif s[i] == "]":
                if len(integerstack) != 0:
                    count = integerstack.pop()
                    temp = stringstack.pop() + count * temp
                    i += 1
                else:
                    stringstack.append(temp)
                    temp = ""
                    i += 1
            else:
                temp += s[i]
                i += 1
        return temp

def main():
    s = Solution()
    print(s.decodeString("3[b2[ca]]")) # bcacabcacabcaca
    print(s.decodeString("3[a]"))
    print(s.decodeString("3[a2[b]]"))
    print(s.decodeString("2[cd]"))

if __name__ == "__main__":
    main()



# Method 2(Using 1 stack)
# Algorithm:

# Loop through the characters of the string
# If the character is not ‘]’, add it to the stack

# If the character is ‘]’:
#    While top of the stack doesn’t contain ‘[‘, pop the characters from the stack and store it in a string temp(Make sure the string isn’t in reverse order)
#    Pop ‘[‘ from the stack
#    While the top of the stack contains a digit, pop it and store it in dig
#    Concatenate the string temp for dig number of times and store it in a string repeat
#    Add the string repeat to the stack
# Pop all the characters from the stack(also make the string isn’t in reverse order) 


# O(n) time | O(n) space - where n is the length of the input string
# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = [] # stack is a list
#         for c in s: # c is a character
#             if c == ']': # if c is ']'
#                 tmp = '' # tmp is a string
#                 while stack[-1] != '[': # while the last element of stack is not '['
#                     tmp += stack.pop() # add the last element of stack to tmp
#                 stack.pop() # pop the last element of stack
#                 stack.append(tmp * int(stack.pop())) # append the string tmp * int(stack.pop()) to stack
#             else:
#                 stack.append(c) # append c to stack
#         return ''.join(stack)

# def main():
#     s = Solution()
#     print(s.decodeString("3[a]"))
#     print(s.decodeString("3[a2[b]]"))
#     print(s.decodeString("2[cd]"))
#     print(s.decodeString("3[b2[ca]]")) # acacbacacbacacb

# if __name__ == '__main__':
#     main()