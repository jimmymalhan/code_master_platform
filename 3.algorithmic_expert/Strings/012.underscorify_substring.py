# Problem Name: Underscorify Substring

# Problem Description:
# Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores.

# If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these substrings should only appear on the far left og the leftmost substring and on the far right of the righmost substring. If the main string doesn't contain the other string at all, the function should return the main string intact.

####################################
# Sample Input:
# string = "testthis is a testtest to see if testtesttest it works"
# substring = "test"
# Sample Output:
# "_test_this is a _testtest_ to see if _testestest_ it works"
####################################
"""
Explain the solution:
1. The first thing you need to do to solve this question is to get the locations of all instances of the substring in the main string. Try traversing the main string one character at a time and calling whatever substring-matching function to built into the language you're working in. Store a 2D array of locations, where each subarray holds the starting and ending indices of a specific instance of the substring in the main string.

2. The second thing you need to do is to "collapse" the 2D array mentioned in Hint #1. In essence, you need to merge the location of substrings that overlap each other or sit next to each other. Traverse the 2D array mentioned in Hint #1 and build a new 2D arrat that holds these "collapsed" locations.

3. Finally, you need to create a new string with underscores added in the correct positions. Construct this new string by traversing the main string and 2D array mentioned in Hint #2 at the same time. You might have to keep track of when you are "in between" underscores in order to correctly traverse the 2D array.

4. Average case: O(n + m) time and O(n) space - where n is the length of the main string and m is the length of the substring.
##################
Detailed explanation of the Solution:

"""
####################################

# O(n + m) time and O(n) space - where n is the length of the main string and m is the length of the substring.

def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring)) # locations is a 2D array 
    return underscorify(string, locations)

def getLocations(string, substring):
    locations = [] 
    startIdx = 0
    while startIdx < len(string): 
        nextIdx = string.find(substring, startIdx) # find the next index of the substring
        if nextIdx != -1: # if the next index is not -1, then there is a substring or substring is found
            locations.append([nextIdx, nextIdx + len(substring)]) # append the start and end indices of the substring
            startIdx = nextIdx + 1 # start the search from the next index
        else: # if the next index is -1, then there is no substring or substring is not found, so break out of the loop
            break
    return locations

def collapse(locations):
    if not len(locations): # if there are no locations, return the empty array
        return locations
    newLocations = [locations[0]] # start with the first location
    previous = newLocations[0] # previous is the first location
    for i in range(1, len(locations)): # iterate through the rest of the locations
        current = locations[i] # current is the next location
        if current[0] <= previous[1]: # if the current location starts before the previous location ends
            previous[1] = current[1] # update the end index of the previous location
        else:
            newLocations.append(current) # otherwise, add the current location to the new locations
            previous = current # update the previous location
    return newLocations 

def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False # keep track of whether or not you are in between underscores
    finalChars = [] # keep track of the final characters
    i = 0 # keep track of the index of the string
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]: # if you are at the start of a location
            finalChars.append("_") # add an underscore
            inBetweenUnderscores = not inBetweenUnderscores # flip the boolean
            if not inBetweenUnderscores: # if you are not in between underscores
                locationsIdx += 1 # increment the locations index
            i = 0 if i == 1 else 1 # flip the index
        finalChars.append(string[stringIdx]) # add the current character to the final characters
        stringIdx += 1 # increment the string index
    if locationsIdx < len(locations): # if there are still locations left
        finalChars.append("_") # add an underscore
    elif stringIdx < len(string): # if there are still characters left
        finalChars.append(string[stringIdx:]) # add the remaining characters
    return "".join(finalChars) # return the final characters


print(underscorifySubstring("testthis is a testtest to see if testtesttest it works", "test")) # _test_this is a _testtest_ to see if _testestest_ it works