# O(wn(log(n) + nwlog(w)) time | O(wn) space - where w is the number of words and n is the length of the longest word
# time O(wn(log(n) + nwlog(w)) |space w * (n + 1) = wn
# sorted at length of n {n(log(n))} with w words = wn(log(n))
# comparisons n with sorted length w {w(log(w))}

words =["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

def groupAnagrams(words):
	if len(words) == 0:
		return []
	
	sortedWords = ["".join(sorted(w)) for w in words] # sorted in a list | oy, act, flop, act, foo, act, oy, flop
	indices = [i for i in range(len(words))] # list of indices
	indices.sort(key=lambda x: sortedWords[x]) # sorting the indices based on sortedWords (which was done alphabetically)
	
	result = []
	currentAnagramGroup = []
	currentAnagram = sortedWords[indices[0]] # current running Anagram .. starting from index 0
	for index in indices: # index - 1, 3, 5, 2, 7, 4, 0, 6
		word = words[index] # word is sorted but not arranged | act, tac, cat, flop, olfp...
		sortedWord = sortedWords[index] # word is sorted and arranged alphbetically | act, act, act, flop, flop, foo, oy, oy
		
		if sortedWord == currentAnagram:
			currentAnagramGroup.append(word)
			continue
			
		result.append(currentAnagramGroup) # act, tac, cat
		currentAnagramGroup = [word] # flop, olfp
		currentAnagram = sortedWord # oy, yo
		
	result.append(currentAnagramGroup)
	
	return result

#	=== 

# O(wnlog(n) time) | O (wn) space - where w is the number of words and n is the length of the longest word
# sort w  at length n | checking hashtable at constant space with wn
def groupAnagrams(words):
	anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word)) # sorted in a list | oy, act, flop, act, foo, act, oy, flop

		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())

print(groupAnagrams(words))