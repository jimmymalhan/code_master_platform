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

# counts and maximum frequency(unique characters) is required to keep track of characters
def minimumCharactersForWords(words):
	maximumCharacterFrequencies = {}
	# loop through words - count all the characters in the words and update the hashmap as I find
	for word in words:
		characterFrequencies = countCharacterFrequencies(word) # counting characters
		updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies) # using character frequencies to update the maximumCharacterFrequencies
	
	return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies) # generating a list from a maximumCharacterFrequencies

def countCharacterFrequencies(string):
	characterFrequencies = {} # count no of times, characters occur in this string
	
	for character in string:
		if character not in characterFrequencies: # checking - if character is already in hashmap
			characterFrequencies[character] = 0
		
		characterFrequencies[character] += 1
	
	return characterFrequencies

def updateMaximumFrequencies(frequencies, maximumFrequencies): # function for - using character frequencies to update the maximumCharacterFrequencies
	for character in frequencies:
		frequency = frequencies[character]
		
		if character in maximumFrequencies:
			maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
		else:
			maximumFrequencies[character] = frequency
# don't need to return anything as we are modifying the hashMap
def makeArrayFromCharacterFrequencies(characterFrequencies): # function for - character frequencies to update the maximumCharacterFrequencies
	characters = []
	
	for character in characterFrequencies:
		frequency = characterFrequencies[character]
		
		for _ in range(frequency):
			characters.append(character)
	
	return characters