words = ["this", "that", "did", "deed", "them!", "a"]

def minimumCharacter(words):
    maximumCharacterFrequencies = {}

    for word in words:
        characterFrequencies = countCharacterFrequencies
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)

def countCharacterFrequencies(string):
    characterFrequencies = {}

    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0
        characterFrequencies[character] += 1
    return characterFrequencies

def updateMaximumFrequencies(frequencies, maximumCharacterFrequencies):
    for character in frequencies:
        frequency = frequencies[character]

        