# read from backwards

class MyClass:
    def __init__(self, string:str) -> bool:
        self.string = string
    def isPalindrome(self):
        print(self.string[:-1])

p1 = MyClass("abcdcbc").isPalindrome()