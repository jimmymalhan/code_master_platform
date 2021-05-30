# maximumCharacterFrequencies , countCharacterFrequencies

words = ["this", "that", "did", "deed", "them!", "a"]

def minimumCharactersForWords(words):
	maximumcharacterFrequencies = {}
	
	for word in words:
		characterFrequencies = countCharacterFrequencies
        updateMaximumFrequencies(characterFrequencies, maximumcharacterFrequencies)
		
def countCharacterFrequencies(string):
	characterFrequencies = {}
    
    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0

        characterFrequencies[character] += 1

    return characterFrequencies

def updateMaximumFrequencies(characterFrequencies, maximumcharacterFrequencies):
    