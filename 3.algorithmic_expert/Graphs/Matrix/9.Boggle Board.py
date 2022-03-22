# Problem Name: Boggle Board

# Problem Description:
# You're given two-dimensional array(a matrix) of potentially unequal height and 
# width containing letters; this matrix represents a boggle board. 
# You're also given a list of words.

# Write a function that returns an array of all the words contained in the boggle 
# board. The final words don't need to be in any particular order.

# A word is constructed in the boggle board by connecting adjacent (horizontally, 
# vertically, or diagonally) letters, without using any single letter at a given 
# position more than once; while a word can of course have repated letters, those 
# repeated letters must come from different positions in the bogggle board in order 
# for the word to be contained in the board. Note that two or more words are allowed
#  to overlap and use the same letters in the boggle board.

####################################
# Sample Input:
# board = [
#   ["t", "h", "i", "s", "i", "s", "a"],
#   ["s", "i", "m", "p", "l", "e", "x"],
#   ["b", "x", "x", "x", "x", "e", "b"],
#   ["x", "o", "g", "g", "l", "x", "o"],
#   ["x", "x", "x", "D", "T", "r", "a"],
#   ["R", "E", "P", "E", "A", "d", "x"],
#   ["x", "x", "x", "x", "x", "x", "x"],
#   ["N", "O", "T", "R", "E", "-", "P"],
#   ["x", "x", "D", "E", "T", "A", "E"]
# ]
# words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", 
# "REPEATED", "NOTRE-PEATED"]

# Sample Output:
# ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]

####################################
"""
Explain the solution:
- You can divide this question into two separate problems: one part involves traversing
the boggle board in such a way that allows you to construct strings letter by letter;
the other part involves actually comparing the strings you construct in the board
against the words in the list that you're given. For the second part, what data 
structure lends itself very well to matching characters tu multiple strings at once?

- Try creating a trie out of the input list of words. This will allow you to compare
letters in the boggle board against all input words in constant time. How can you 
efficiently traverse the boggle board to construct all potentially valid strings,
without counting letters twice in any string?

- Treat the board as a graph. where each element in the board is a node with up to 8
neighboring nodes. Traverse it in a depth-first-search-like fashion, checking if 
letters are contained in the trie and traversing the trie simultaneously if it makes
sense to do so. How can you keep track of letters that you've already visited in order
to avoid erroneously counting some of them twice in a single string? Could you keep 
track of visited nodes in an auxiliary data structure?

- Keeping in mind that you only want to mark nodes as visited in a single branch of 
the graph that you're traversing (i.e, you don't want the state of visited nodes in
one branch of the graph to spill into the state of another branch of the graph), try
marking any node you traverse as unvisited  at the end of the recursive call that 
actually traverses it, after traversing through all of the nodes's neighbors and 
performing the same actions on them recursively.

# O(nm*8^s + ws) time | O(nm + ws) space - where n is the width of the board, m is
height of the board, w is the number of words, and s is the length of the longest
word.

##################
Detailed explanation of the Solution:
function boggleBoard(board, words):
    trie is equal to a Trie() # object to store the trie
    loop for word in words:
        trie.add(word) # add each word to the trie
    finalWords is equal to {} # create a dictionary to store the final words
    visited is equal to [[False for letter in row] for row in board] # create a visited matrix
    loop for i in range(len(board)): # for each row
        loop for j in range(len(board[i])): # for each column
            explore(i, j, board, trie.root, visited, finalWords) # explore the board
    return list(finalWords.keys())

function explore(i, j, board, node, visited, finalWords):
    if visited[i][j]: # if the node has been visited, return nothing
        return
    letter is equal to board[i][j] # get the letter at the current node
    if letter not in trieNode: # if the letter is not in the trie, return nothing # to check if the letter is in the trie
        return
    visited[i][j] is equal to True # mark the node as visited
    trieNode is equal to trieNode[letter] # get the trieNode corresponding to the letter
    if '*' in trieNode: # if the trieNode contains a wildcard, add the word to the finalWords dictionary
        finalWords[trieNode['*']] = True
    neighbors is equal to getNeighbors(i, j, board) # get the neighbors of the node
    loop for neighbor in neighbors: # for each neighbor
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords) # explore the neighbor
    visited[i][j] is equal to False # mark the node as unvisited

function getNeighbors(i, j, board):
    neighbors is equal to [] # create a list to store the neighbors
    if i > 0 and j > 0: # top left
        neighbors.append((i-1, j-1)) # add the neighbor
    if i > 0 and j < len(board[0]) - 1: # top right
        neighbors.append((i-1, j+1))
    if i < len(board) - 1 and j < len(board[0]) - 1: # bottom right
        neighbors.append((i+1, j+1))
    if i < len(board) - 1 and j > 0: # bottom left
        neighbors.append((i+1, j-1))
    if i > 0: # top
        neighbors.append((i-1, j))
    if i < len(board) - 1: # bottom
        neighbors.append((i+1, j))
    if j > 0: # left
        neighbors.append((i, j-1))
    if j < len(board[0]) - 1: # right
        neighbors.append((i, j+1))
    return neighbors

class Trie:
    def __init__(self):
        self.root = {} # create a root node
        self.endSymbol = '*' # create an end symbol

    def add(self, word):
        current is equal to self.root # start at the root
        for letter in word: # for each letter in the word
            if letter not in current: # if the letter is not in the trie
                current[letter] = {} # add the letter to the trie
            current = current[letter] # move to the next node
        current[self.endSymbol] = True # mark the end of the word

"""
####################################

# O(nm*8^s + ws) time | O(nm + ws) space 
def boggleBoard(board, words):
    trie = Trie() # object to store the trie
    for word in words: 
        trie.add(word) # add each word to the trie
    finalWords = {} # create a dictionary to store the final words
    visited = [[False for letter in row] for row in board] # create a visited matrix
    for i in range(len(board)): # for each row
        for j in range(len(board[i])): # for each column
            explore(i, j, board, trie.root, visited, finalWords) # explore the board
    return list(finalWords.keys()) # return the final words

def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]: # if node has been visited, return nothing
        return
    letter = board[i][j] # get the letter at this node
    if letter not in trieNode: # if the letter isn't in the trie, return # to check if the letter is in the trie
        return
    visited[i][j] = True # mark this node as visited
    trieNode = trieNode[letter] # get the trieNode corresponding to this letter
    if '*' in trieNode: # if we've reached the end of a word, add it to the final words
        finalWords[trieNode['*']] = True # add the word to the final words
    neighbors = getNeighbors(i, j, board) # get the neighbors of this node
    for neighbor in neighbors: # for each neighbor
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords) # explore it for all visited neighbors
    visited[i][j] = False # mark this node as unvisited

def getNeighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0: # top left
        neighbors.append((i-1, j-1)) # add the neighbor
    if i > 0 and j < len(board[0]) - 1: # top right
        neighbors.append((i-1, j+1))
    if i < len(board) - 1 and j < len(board[0]) - 1: # bottom right
        neighbors.append((i+1, j+1))
    if i < len(board) - 1 and j > 0: # bottom left
        neighbors.append((i+1, j-1))
    if i > 0: # top
        neighbors.append((i-1, j))
    if i < len(board) - 1: # bottom
        neighbors.append((i+1, j))
    if j > 0: # left
        neighbors.append((i, j-1))
    if j < len(board[0]) - 1: # right
        neighbors.append((i, j+1))
    return neighbors

class Trie: # trie data structure
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word):
        current = self.root # start at the root
        for letter in word:
            if letter not in current: # if the letter isn't in the trie
                current[letter] = {} # add it
            current = current[letter] # move down the trie
        current[self.endSymbol] = word # mark the end of the word


print(boggleBoard([["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
],["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]))