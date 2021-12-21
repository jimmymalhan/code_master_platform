class MyClass:
    def __init__(self, string:str):
        self.string = string

# O(n^2) time | O(n) space
    def isPalindrome_bruteforce(self):
        self.string = self.string.lower()
        # self.string = self.string.replace(" ", "")
        # use isalnum() to check if the string contains only alphanumeric characters
        self.string = ''.join(e for e in self.string if e.isalnum())
        reversedString = []
        for i in reversed(range(len(self.string))):
            reversedString.append(self.string[i]) # adding directly to newString -> imporving
        return self.string == "".join(reversedString)

# O(n) time and O(n) space
    def isPalindrome_quickSol(self):
        self.string = self.string.lower()
        # self.string = self.string.replace(" ", "")
        # use isalnum() to check if the string contains only alphanumeric characters
        self.string = ''.join(e for e in self.string if e.isalnum())
        return self.string == self.string[::-1]

# recursion
# O(n) time | O(n) space
    def isPalindrome_recursion(self, i = 0):
        j = len(self.string) - 1 - i
        return True if i >= j else self.string[i] == self.string[j] and self.isPalindrome_recursion(i + 1)
    # string[i] = firstIdx
    # stringp[j] = lastIdx
    # recursion always involve extra memory because of tail recursion
    # tail recursion - 


# O(n) time and O(1) space
    def isPalindromeOptimized(self):
        self.string = self.string.lower()
        # self.string = self.string.replace(" ", "")
# use isalnum() to check if the string contains only alphanumeric characters
        self.string = ''.join(e for e in self.string if e.isalnum())
        leftIdx = 0 # pointer on firstIdx
        rightIdx = len(self.string) - 1 # # pointer on lastIdx
        while leftIdx < rightIdx:
            if self.string[leftIdx] != self.string[rightIdx]:
                return False
            leftIdx += 1
            rightIdx -= 1
        return True


def main():
    stringName = MyClass("abcdcbA ##$@$  ^##^$")
    print(stringName.isPalindrome_bruteforce())
    print(stringName.isPalindrome_quickSol())
    print(stringName.isPalindrome_recursion())
    print(stringName.isPalindromeOptimized())
    print(stringName.countPalindromes())

if __name__ == '__main__':
	main()

############################################################################################################################
# count palidromes in a string

def isPalindrome(s):
    return s == s[::-1]

def countPalindromes(s):
    count = 0
    for i in range(len(s)): # i = 0, 1, 2, 3
        for j in range(i, len(s)): # j = 0, 1, 2, 3, 4
            if isPalindrome(s[i:j+1]): # s[i:j+1] = s[0:4] = "toco"
                count += 1
    return count

print(countPalindromes("daata"))