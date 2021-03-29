# n - len of character in string
# m - len of document in string

# Solution -> 1 counting elements in char and document everytime -> increses the time
# O(m*(n + m)) space | O(1) space 
# counting every element in character(n) + counting every element in document(m)
# -> leads to (n + m)
# every iteration of the document(m) -> will do (n + m) work
# therefore, m*(n + m) time

# Solution -> 2 -> create a set{}, after counting to char's ADD it to the set{}
# -> which means we don't need to count again in set{}
# O(c*(n+m)) time | O(c)space where, c is number of unique elements in the document

# Solution -> 3 -> loop through only once, store the count in hashmap/dictionary 
# as key/vaue store {} to check if we have enough elements to create document
# O(n+m)time | O(c) space where c is number of unique elements in the document

# Solution - 0
# using count  method for python inbuilt
def generateDocument(characters, document):
	for character in document:
		documentFrequency = document.count(character) #O(n)
		charactersFrequency = characters.count(character)
		if documentFrequency > charactersFrequency:
			return False
	return True

# Solution - 1
# O(m*(n + m)) space | O(1) space 
def generateDocument(characters, document):
	for character in document:
		documentFrequency = countCharacterFrequency(character, document)
		charactersFrequency = countCharacterFrequency(character, characters)
		if documentFrequency > charactersFrequency:
			return False
	return True
def countCharacterFrequency(character, target): # target = document + characters
		frequency = 0
		for char in target:
			if char == character:
				frequency += 1
		return frequency


# Solution - 2
def generateDocument(characters, document):
	alreadyCounted = set() # [] - can be used but replace add with append
	
	for character in document:
		if character in alreadyCounted:
			continue
			
		documentFrequency = countCharacterFrequency(character, document)
		charactersFrequency = countCharacterFrequency(character, characters)
		if documentFrequency > charactersFrequency:
			return False
		
		alreadyCounted.add(character) # replace add with append
		
	return True
def countCharacterFrequency(character, target): # target = document + characters
	frequency = 0
	for char in target:
		if char == character:
			frequency += 1
			
	return frequency
# Solution - 3