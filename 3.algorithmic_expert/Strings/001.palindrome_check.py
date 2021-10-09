# # O(n^2) time | O(n) space

# brute force
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

# recursion
# # O(n) time | O(n) space
def isPalindrome(string):
	reversedString = []
	for i in reversed(range(len(string))):
		reversedString.append(string[i]) # adding directly to newString -> imporving
	return string == "".join(reversedString)

# # O(n) time | O(n) space
def isPalindrome(string, i = 0):
	j = len(string) - 1 - i
	return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)
# string[i] = firstIdx
# stringp[j] = lastIdx
# recursion always involve extra memory because of tail recursion
# tail recursion - 

# # O(1) time | O(n) space
def isPalindrome(string):
	leftIdx = 0 # pointer on firstIdx
	rightIdx = len(string) - 1 # # pointer on lastIdx
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True

