# Problem Name: Multi String Search

# Problem Description: 
# Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether the small string at that index in the array of small strings is contained in the big string.

####################################
# Sample Input #1:
# bigString = "this is a big string"
# smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

# Sample Output:
# [True, False, True, True, False, True, false]

# Sample Input #2:
# bigString = "abcdefghijklmnopqrstuvwxyz"
# smallStrings = ["abc", "mnopqr", "wyz", "no", "e". "tuuv"]

# Sample Output:
# [True, True, False, True, True, False]

####################################
"""
Explain the solution:
1. Brute Force: Iterate through each small string and check if it is in the big string.

2. Build a suffix-trie-like data structure containing all of the big string's suffixes. Then, iterate through all of the small strings and check if each of them is is contained in the trie.

3. Build a trie-like data structure containing all of the small strings. Then, iterate through all of the big string's suffixes and check if each of them is is contained in the trie.

# O(ns + bs) time | O(ns) space - where n is the number of small strings, s is the length os small sting, and b is the length of big string.

##################
Detailed explanation of the Solution:

"""
####################################

# brute force solution  
def multiStringSearchBruteForce(bigString, smallStrings):
# Iterate through each small string and check if it is in the big string.
    result = []
    for smallString in smallStrings:
        result.append(bigString.find(smallString) != -1) # If the small string is not in the big string, the find method returns -1.
    return result