# O(w * n * log(n) + n * w * log(w)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word

words =["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

def groupAnagrams(words):
	if len(words) == 0:
		return []
	
	sortedWords = ["".join(sorted(w)) for w in words] # sorts as list
	indices = [i for i in range(len(words))] # list of indices
	indices.sort(key=lambda x: sortedWords[x]) # sorting the indices based on sortedWords (which was done alphabetically)
	
	result = []
	currentAnagramGroup = []
	currentAnagram = sortedWords[indices[0]] # current running Anagram .. starting from index 0
	for index in indices:
		word = words[index] # word is sorted but not arranged 
		sortedWord = sortedWords[index] # word is sorted and arranged alphbetically

		if sortedWord == currentAnagram:
			currentAnagramGroup.append(word)
			continue
			
		result.append(currentAnagramGroup) # act, tac, cat
		currentAnagramGroup = [word] # flop, olfp
		currentAnagram = sortedWord # oy, yo
		
	result.append(currentAnagramGroup)
	
	return result

#	=== 

# O(w * n * log(n) time) | O (wn) space - where w is the number of words and 
# n is the length of the longest word
def groupAnagrams(words):
	anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())