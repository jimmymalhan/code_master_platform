class MyClass:
    def __init__(self, string:str) -> bool:
        self.string = string
    def isPalindrome(self):
        reversedString = ""
        for i in reversed(range(len(self.string))):
            reversedString += self.string[i] # creating newString -> increases time
        return self.string == reversedString

def main():
	print(MyClass("abcdcba").isPalindrome())

if __name__ == '__main__':
	main()