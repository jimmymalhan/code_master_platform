# read from backwards

class MyClass:
    def __init__(self, string:str) -> bool:
        self.string = string
    def isPalindrome(self):
        reversedString = ""
        for i in reversed(range(len(self.string))):
            reversedString += self.string[i]
        return self.string == reversedString

print(MyClass("abcdcba").isPalindrome())