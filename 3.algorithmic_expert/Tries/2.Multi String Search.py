# Problem Name: Multi String Search

# Problem Description: 
# Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether the small string at that index in the array of small strings is contained in the big string.

####################################
# Sample Input #1:
# bigString = "this is a big string"
# smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

# Sample Output:
# [True, False, True, True, False, True, false]

# Sample Input #2:
# bigString = "abcdefghijklmnopqrstuvwxyz"
# smallStrings = ["abc", "mnopqr", "wyz", "no", "e". "tuuv"]

# Sample Output:
# [True, True, False, True, True, False]

####################################
"""
Explain the solution:
1. Brute Force: Iterate through each small string and check if it is in the big string.

2. Build a suffix-trie-like data structure containing all of the big string's suffixes. Then, iterate through all of the small strings and check if each of them is is contained in the trie.

3. Build a trie-like data structure containing all of the small strings. Then, iterate through all of the big string's suffixes and check if each of them is is contained in the trie.

# O(ns + bs) time | O(ns) space - where n is the number of small strings, s is the length os small sting, and b is the length of big string.

##################
Detailed explanation of the Solution:

"""
####################################

# brute force solution  | using built-in function
def multiStringSearchBruteForce(bigString, smallStrings):
# Iterate through each small string and check if it is in the big string.
    result = []
    for smallString in smallStrings:
        result.append(bigString.find(smallString) != -1) # If the small string is not in the big string, the find method returns -1.
    return result

# brute force solution  | without using built-in function
# O(bns) time | O(ns) space - where n is the number of small strings, s is the length of longest small sting, and b is the length of big string.
def multiStringSearch(bigString, smallStrings):
	return[isInBigString(bigString, smallString) for smallString in smallStrings]

def isInBigString(bigString, smallString):
	for i in range(len(bigString)):
		if i + len(smallString) > len(bigString):
			break
		if isInBigStringHelper(bigString, smallString, i):
			return True
	return False

def isInBigStringHelper(bigString, smallString, startIdx):
	leftBigIdx = startIdx
	rightBigIdx = startIdx + len(smallString) -1
	leftSmallIdx = 0
	rightSmallIdx = len(smallString) -1
	while leftBigIdx <= rightBigIdx:
		if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]:
			return False
		leftBigIdx += 1
		rightBigIdx -= 1
		leftSmallIdx += 1
		rightSmallIdx -= 1
	return True

# O(b^2 + ns) time | O(b^2 + n) space - where n is the number of small strings, s is the length of longest small sting, and b is the length of big string.

# b^2 is the construction of the trie

def multiStringSearch(bigString, smallStrings):
	modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
	return[modifiedSuffixTrie.contains(string) for string in smallStrings]

class ModifiedSuffixTrie:
	def __init__(self, string):
		self.root = {}
		self.populateModifiedSuffixTrieFrom(string)
		
	def populateModifiedSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubstringStartingAt(i, string)
			
	def insertSubstringStartingAt(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
			
	def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return True

# O(ns + bs) time | O(ns) space - where n is the number of small strings, s is the length of longest small sting, and b is the length of big string.

def multiStringSearch(bigString, smallStrings):
	trie = Trie()
	for string in smallStrings:
		trie.insert(string)
	containedStrings = {}
	for i in range(len(bigString)):
		findSmallStringsIn(bigString, i, trie, containedStrings)
	return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
	currentNode = trie.root
	for i in range(startIdx, len(string)):
		currentChar = string[i]
		if currentChar not in currentNode:
			break
		currentNode = currentNode[currentChar]
		if trie.endSymbol in currentNode:
			containedStrings[currentNode[trie.endSymbol]] = True
			
class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def insert(self, string):
		current = self.root
		for i in range(len(string)):
			if string[i] not in current:
				current[string[i]] = {}
			current = current[string[i]]
		current[self.endSymbol] = string

print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"])) # [True, False, True, True, False, True, False]