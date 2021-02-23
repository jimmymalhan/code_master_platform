# # O(n^2) time | O(n) space
def isPalindrome(string):
	reversedString = "" #
	for i in reversed(range(len(string))):
		reversedString += (string[i]) # creating newString -> increases time
	return string == reversedString

# # O(n) time | O(n) space
def isPalindrome(string):
	reversedString = [] #
	for i in reversed(range(len(string))):
		reversedString.append(string[i]) # adding directly to newString -> imporving
	return string =="".join(reversedString)

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