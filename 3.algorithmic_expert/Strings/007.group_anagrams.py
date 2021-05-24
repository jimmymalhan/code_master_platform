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

# O(w * n * log(n) time) | O (wn) space - where w is the number of words and 
# n is the length of the longest word

# words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
def groupAnagrams(words):
	anagrams = {}
	for word in words: # print(word) # yo, act, flop, tac, foo, cat, oy, olfp
		sortedWord = "".join(sorted(word)) # sort indices # oy, act, flop, act, foo, act, oy, flop
		if sortedWord in anagrams:
			# print(sortedWord) # act, act, oy, flop # keys
			# print(anagrams)
				# {'oy': ['yo'], 'act': ['act'], 'flop': ['flop']}
				# {'oy': ['yo'], 'act': ['act', 'tac'], 'flop': ['flop'], 'foo': ['foo']}
				# {'oy': ['yo'], 'act': ['act', 'tac', 'cat'], 'flop': ['flop'], 'foo': ['foo']}
				# {'oy': ['yo', 'oy'], 'act': ['act', 'tac', 'cat'], 'flop': ['flop'], 'foo': ['foo']}
			# print(anagrams[sortedWord]) # ['act'], ['act', 'tac'], ['yo'], ['flop']
			# value = key
			anagrams[sortedWord].append(word) # if sorted word in anagram -> appending keys(word)
		else:
			anagrams[sortedWord] = [word] # if word is not found in anagram then adding word
	# print(anagrams) #{'oy': ['yo', 'oy'], 'act': ['act', 'tac', 'cat'], 'flop': ['flop', 'olfp'], 'foo': ['foo']}
	# print(list(anagrams.keys())) # ['oy', 'act', 'flop', 'foo']
	# print(list(anagrams.values())) # [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
	return list(anagrams.values())