# O(n^2) time | O(1) space
def firstNonRepeatingCharacter(string):
	for i in range(len(string)):
		foundDuplicate = False
		for j in range(len(string)):
			if string[i] == string[j] and i != j:
				foundDuplicate = True
				
		if not foundDuplicate:
			return i
		
	return -1

# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
	characterFrequencies = {}
	
	for character in string:
		characterFrequencies[character] = characterFrequencies.get(character, 0) + 1 
		# it look in the hashMap/Dict - if character is not there(array) it assigns/add the value 0 + 1 = 1 
		
	
	# idx traversal
	for idx in range(len(string)):
		character = string[idx]
		if characterFrequencies[character] == 1: # checking the first non-repeating character in hashMap
			return idx
	return -1