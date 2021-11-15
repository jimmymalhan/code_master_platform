# O(n) time | O(n) space
def runLengthEncoding(string):
	encodedStringCharacters = [] # lossless data compression
	currentRunLength = 1 # this will always be 1(never be zero)
	
	for i in range(1, len(string)):
		currentCharacter = string[i]
		previousCharacter = string[i - 1]
		
		if currentCharacter != previousCharacter or currentRunLength == 9: # or is req so it can append individually
			encodedStringCharacters.append(str(currentRunLength))
			encodedStringCharacters.append(previousCharacter)
			currentRunLength = 0 # needed so it can add like 9A4A vs 13A(not required)
			
		currentRunLength += 1
		
	encodedStringCharacters.append(str(currentRunLength))
	encodedStringCharacters.append(string[len(string) - 1])
	
	return "".join(encodedStringCharacters)

def main():
	print(runLengthEncoding("AAAABBBCCDAA")) # 4A3B2C1D2A

if __name__ == "__main__":
	main()