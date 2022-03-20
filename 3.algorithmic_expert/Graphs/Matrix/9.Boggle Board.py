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
the boggle board in such a way that allows you to contrcut strings letter by letter;
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

"""
####################################

# O(nm*8^s + ws) time | O(nm + ws) space 
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if '*' in trieNode:
        finalWords[trieNode['*']] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False

def getNeighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append((i-1, j-1))
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append((i-1, j+1))
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append((i+1, j+1))
    if i < len(board) - 1 and j > 0:
        neighbors.append((i+1, j-1))
    if i > 0:
        neighbors.append((i-1, j))
    if i < len(board) - 1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < len(board[0]) - 1:
        neighbors.append((i, j+1))
    return neighbors

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word


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