# O(1) time | O(1) space
def validIPAddresses(string):
	ipAddressesFound = []
	
	for i in range(1, min(len(string), 4)): # from index 0 - 4
		currentIPAddressParts = ["","","",""]
		
		currentIPAddressParts[0] = string[:i] # before the first period
		if not isValidPart(currentIPAddressParts[0]):
			continue
			
		for j in range(i + 1, i + min(len(string) - i, 4)): # i + 1 = for second period, placement of i at most in 3 positions past of i 
			currentIPAddressParts[1] = string[i : j] # start from index i where the first position started to j at placement
			if not isValidPart(currentIPAddressParts[1]):
				continue
			
			for k in range(j + 1, j + min(len(string) - j, 4)): # j + 1 = for third period, placement of j at most in 3 positions past of j 
				currentIPAddressParts[2] = string[j:k] # 3rd section
				currentIPAddressParts[3] = string[k:] # 4th section
				
				if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
					ipAddressesFound.append(".".join(currentIPAddressParts))
					
	return ipAddressesFound
		
def isValidPart(string):
	stringAsInt = int(string)
	if stringAsInt > 255:
		return False
	
	return len(string) == len(str(stringAsInt)) # check for leading 0 # 00 converted to  0, 01 converted to 1