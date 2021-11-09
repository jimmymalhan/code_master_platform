# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.


# input: S = "ab#c", T = "ad#c"
# output: true
# Explanation: Both S and T become "ac".

# input: S = "ab##", T = "c#d#"
# output: true
# Explanation: Both S and T become "". # is a special character in the string.

# backspace compare mea
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_string(s):
            stack = [] # stack for backspace # why use stack? because we need to pop the last element
            for c in s: # iterate through string
                if c != '#': # if not backspace
                    stack.append(c) # append to stack
                else:
                    if stack: # if stack is not empty
                        stack.pop() # pop last element
            return ''.join(stack)

        return get_string(S) == get_string(T) # backspace compare 

def main():
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))
    print(sol.backspaceCompare("ab##", "c#d#"))

print(main())