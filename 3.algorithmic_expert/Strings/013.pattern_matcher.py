# Problem Name: Pattern Matcher

# Problem Description:
# You're given two non-empty strings. The first one is a pattern consisting of only "x"s and /or "y"s; the other one is a normal string of alphanumeric characters. Write a function that checks whether normal string matches the pattern.

# A string S0 is said to match a pattern if replacing all "x"s in the pattern with some non-empty substring S1 of S0 and replacing all "y"s in the pattern with some non-empty substring S2 of S0 yields the same string S0.

# If the input string doesn't match the input pattern, the function should return an empty array; otherwise, it should return an array holding the strings S1 and S2 that represent "x" and "y" in the normal string, in that order. If the pattern doesn't contain any "x"s or "y"s, the respective letter should be represented by an empty string in the final array that you return.

# You can assume that there will never be more that one pair of strings S1 and S2 that appropriately represent "x" and "y" in the normal string.

####################################
# Sample Input:
# pattern = "xxyxxy"
# string = "gogopowerrangergogopowerranger"

# Sample Output:
# ["go", "powerranger"]

####################################
"""
Explain the solution:
1. Start by checking if the pattern starts with an "x". If it doesn't, consider generating a new pattern that swaps all "x"s with "y"s and vice versa; this might greatly simplify the rest of your algorithm. Make sure to keep track of whether or not you do this swap, as your final answer will be affected by it.
 - Example: We need the pattern = "xxyxxy". If the Pattern is provided = "yyxxyy" , we need to swap "x"s with "y"s to get the new pattern = "xxyxxy".

2. Use a hash table to store the number of "x"s and "y"s that appear in the pattern, and keep track of the position of the first "y". Knowing how many "x"s and "y"s appear in the pattern, paired with the length of the main string which you have access to, will allow you to quickly test out various possible lengths for "x" and "y". Knowing whether the first "y" appears in the pattern will allow you to actually generate potential substrings.

3. Traverse the main string and try different combinations of substrings that could represent "x" and "y". For each potential combination, map the new pattern mentioned in Hint #1 and see if it match the main string.

# O(n^2 + m) time | O(n + m) space - where n is the length of the main string and m is the length of the pattern.

##################
Detailed explanation of the Solution:

"""
####################################

def patternMatcher(pattern, string):
    if len(pattern) > len(string): # If the pattern is longer than the string, it can't match.
        return []
    newPattern = getNewPattern(pattern) # Get the new pattern that swaps "x"s with "y"s.
    didSwitch = newPattern[0] != pattern[0] # If the first character of the new pattern is not the same as the first character of the original pattern, we need to swap "x"s and "y"s.
    counts = {"x": 0, "y": 0} # Keep track of the number of "x"s and "y"s in the pattern.
    firstYPos = getCountsAndFirstYPos(newPattern, counts) # # updates the counts and the position of the first "y" in the pattern.
    if counts["y"] != 0: # If there are "y"s in the pattern, we need to make sure that the first "y" appears in the pattern.
        for lenOfX in range(1, len(string)):
            # print(lenOfX) # 1, 2
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"] # lenofY needs to be even number. Result is in float.
            #(30 - 1 * 4) / 2 = 26/2 = 13.0
            #(30 - 2 * 4) / 2 = 22/2 = 11.0
            if lenOfY <= 0 or lenOfY % 1 != 0: # validate that lenOfY is a positive integer - if it is not, continue to the next iteration.
                continue
            # print(lenOfY) # 13
            lenOfY = int(lenOfY) # Convert lenOfY from float to an integer.
            # print(lenOfY) # 13, 11
            yIdx = firstYPos * lenOfX # The index of the first "y" in the pattern.
            # print(yIdx) # 2, 4
            x = string[:lenOfX] # The substring that could represent "x".
            # print(x) # g, go
            y = string[yIdx:yIdx + lenOfY] # The substring that could represent "y". eg. "powerranger"
            # print(y) # gopowerranger, powerranger
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern) # check if the new pattern matches the string.
            if string == "".join(potentialMatch): # If the substring that could represent "x" and "y" matches the main string, return the substring that could represent "x" and "y".
                return [x, y] if not didSwitch else [y, x] # If we swapped "x"s and "y"s, return the substring that could represent "y" and "x" in the correct order.

    else: # If there are no "y"s in the pattern, we can just check if the pattern matches the main string.
        lenOfX = len(string) / counts["x"] # lenOfX is the length of the substring that could represent "x"
        if lenOfX % 1 == 0: # If lenOfX is a positive integer, we can check if the pattern matches the main string.
            lenOfX = int(lenOfX) # Convert lenOfX to an integer.
            x = string[:lenOfX] # The substring that could represent "x". eg. "go"
            potentialMatch = map(lambda char: x, newPattern) # check if the substring that could represent "x" matches the main string. eg. "go"
            if string == "".join(potentialMatch): # If the substring that could represent "x" matches the main string, return the substring that could represent "x".
                return [x, ""] if not didSwitch else ["", x]
    return [] # If the pattern doesn't match the main string, return an empty array.

def getNewPattern(pattern): # Get the new pattern that swaps "x"s with "y"s.
    patternLetters = list(pattern) # Convert the pattern to a list of characters.
    if patternLetters[0] == "x": # If the first character is an "x", just return the pattern.
        return patternLetters
    else: # If the first character is not an "x", swap all "y"s with "x"s.
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters)) # Swap all "x"s with "y"s.

def getCountsAndFirstYPos(pattern, counts): # updates the counts of "x" and "y" and the position of the first "y" in the pattern.
    firstYPos = None
    # counts = {"x": 0, "y": 0} # defined in the main function.
    for i, char in enumerate(pattern):
        counts[char] += 1 # increment the count of the current character if it is an "x" or "y".
        # print(counts) # {'x': 1, 'y': 0}
                        # {'x': 2, 'y': 0}
                        # {'x': 2, 'y': 1}
                        # {'x': 3, 'y': 1}
                        # {'x': 4, 'y': 1}
                        # {'x': 4, 'y': 2}
        if char == "y" and firstYPos is None: # If the current character is an "y" and the first "y" position hasn't been set, set it to the current index.
            # print(firstYPos) # None
            firstYPos = i # Set the first "y" position to the current index.
            # print(firstYPos) # 2
    return firstYPos

print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))