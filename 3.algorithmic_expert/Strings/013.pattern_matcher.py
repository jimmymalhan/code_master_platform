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

2. Use a hash table to store the number of "x"s and "y"s that appear in the pattern, and keep track of the position of the first "y". Knowing how many "x"s and "y"s appear in the pattern, paired with the length of the main string which you have access to, will allow you ti quickly test out various possible lengths for "x" and "y". Knowing whether the first "y" appears in the pattern will allow you to actually generate potential substrings.

3. Traverse the main string and try different combinations of substrings that could represent "x" and "y". For each potential combination, map the new pattern mentioned in Hint #1 and see if it match the main string.

# O(n^2 + m) time | O(n + m) space - where n is the length of the main string and m is the length of the pattern.

##################
Detailed explanation of the Solution:

"""
####################################

def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts)
    if counts["y"] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"] # lenOfY is the length of the substring that could represent "y"
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos * lenOfX
            x = string[:lenOfX]
            y = string[yIdx :  yIdx + lenOfY]
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]

    else:
        lenOfX = len(string) / counts["x"]
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]
    return []

def getNewPattern(pattern):
    patternLetters = list(pattern)
    if patternLetters[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters))

def getCountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and firstYPos is None:
            firstYPos = i
    return firstYPos

print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))