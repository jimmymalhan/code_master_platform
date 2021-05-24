# O(n * l) time | O(c) space - where n is th number of words,
# l is the length of the longest word, and c is the number of
# unique characters across all words

###########
# The space complexity of O(c), where c is the number of unique 
# characters across all words, is actually a lower bound for our 
# solution's space complexity.

# This is because the maximumCharacterFrequencies hash table will 
# take up O(c) space, but the output array of characters might take 
# up more space if some unique characters appear multiple times in 
# a single word. For example, we might have a hash table {"a": 3"} 
# with one character but an output array ["a", "a", "a"] with three 
# characters.

# An upper bound for the space complexity is O(n * l), which happens 
# when every single character in each word is unique across all words 
# and the output array therefore contains n * l characters.

def minimumCharactersForWords(words):
	maximumCharacterFrequencies = {}
	
	for word in words:
		characterFrequencies = countCharacterFrequencies(word)
		updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)
	
	return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)

def countCharacterFrequencies(string):
	characterFrequencies = {}
	
	for character in string:
		if character not in characterFrequencies:
			characterFrequencies[character] = 0
		
		characterFrequencies[character] += 1
	
	return characterFrequencies

def updateMaximumFrequencies(frequencies, maximumFrequencies):
	for character in frequencies:
		frequency = frequencies[character]
		
		if character in maximumFrequencies:
			maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
		else:
			maximumFrequencies[character] = frequency

def makeArrayFromCharacterFrequencies(characterFrequencies):
	characters = []
	
	for character in characterFrequencies:
		frequency = characterFrequencies[character]
		
		for _ in range(frequency):
			characters.append(character)
	
	return characters