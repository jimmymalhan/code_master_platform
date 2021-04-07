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