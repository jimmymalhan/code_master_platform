# Problem Name: Suffix Trie Construction

# Problem Description:
# Write a SuffixTrie class for Suffix-Trie-like data structures. The class should have a root property set to be the root node of the trie and should support:
#      - Creating the trie from a string; this will be done by calling populateSuffixTrieFrom method upon class instantiation, which should populate the root of the class.
#      - Searching for strings in the trie.

# Note that every string added to the trie should end with special endSymbol character: "*".



# Sample Input (for creation):
# string = "babc"

# Sample Output (for creation):
    # The structure below is the root of the trie:
# {
#   "c": {"*": true},
#   "b": {
#      "c": {"*": true},
#      "a": {"b": {"c": {"*": true}}},
#   },
#   "a": {"b": {"c": {"*": true}}},
# }

# Sample Input (for searching in the suffix trie above):
# string = "abc"

# Sample Output (for searching in the suffix trie above):
# True
####################################
"""
Explain the solution:
- Building a suffix-trie-like data structure consists of essentially storing every suffic of a given string in a trie. To do so, iterate through the input string one character at a time, and insert every substring starting at each character and ending at the end of string into the trie.

- To insert a string into the trie, start by adding the first character of the string into the root node of the trie. and mapping it to an empty hash table if it isin't already there. Then, iterate through the rest of the string inserting each of the remaining characters into the previous character's corresponding node(or hash table) in the trie, making sure to add an endSymbol "*" at the end.

- Searching the trie for a specific string should follow a nearlt identical logic to the one used to add a string in the trie.

# Creation: O(n^2) time | O(n^2) space - where n is the length of the input string
# Searching: O(m) time | O(1) space - where m is the length of the input string

##################
Detailed explanation of the Solution:

"""
####################################

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        pass

    def contains(self, string):
        # Write your code here.
        pass

def main():
    pass

if __name__ == '__main__':
    main()