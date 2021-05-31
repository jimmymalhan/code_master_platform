# maximumCharacterFrequencies , countCharacterFrequencies

words = ["this", "that", "did", "deed", "them!", "a"]

def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}
    for word in words:
        characterFrequencies = countCharacterFrequencies
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)
    # return countCharacterFrequencies

def countCharacterFrequencies(string):
    characterFrequencies = {}
    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] += 0
        characterFrequencies[character] += 1
    return countCharacterFrequencies

def updateMaximumFrequencies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]
        
        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency    

print(minimumCharactersForWords(words))