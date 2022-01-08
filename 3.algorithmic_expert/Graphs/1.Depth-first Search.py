# Problem Name: Depth-first Search

# Problem Description:
# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form a acyclic tree-like structure.

# Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-First Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the array, and returns it.

####################################
# Sample Input:
# graph = A
#       / | \
#      B  C  D
#     / \    / \
#    E   F  G   H
#       / \  \
#      I   J  K

# Sample Output:
# ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']

####################################
"""
Explain the Solution:
1. The Depth-First Search algorithm works by traversing the graph branch by branch, starting at the root node. Before traversing any Node's sibling Nodes, its children nodes must be traversed first.
2. Start at the root Node and try simply calling the depthFirstSearch method on all children Nodes of each child Node. Add the name of the child Node to the array at every call of depthFirstSearch.
# O(v + e) time | O(v) space, where v is the number of vertices and e is the number of edges

##################
Detailed explanation of the Solution:
function depthFirstSearch(self, array)
append rootNode in the array
loop through leafnodes
    call DFS on all children on array
return array
"""
####################################

class Node:
    def __init__(self, name):
        self.children = [] # list of children
        self.name = name # name of the root node

    def addChild(self, name):
        self.children.append(Node(name)) # add child to list of children
        return self # return self to allow chaining

    # v - vertices | # e - edges
    # O(v + e) time | O(v) space          # v frames on call stack

    def depthFirstSearch(self, array):
        array.append(self.name)           # adding root Node
        for child in self.children:       # looping for every object in children
            child.depthFirstSearch(array) # calling recursively
        return array
"""
    Explanation:

    def depthFirstSearch(self, array):
        array.append(self.name)          # Step - 1 start at rootNode and ADD - 'A' | Step - 4 append 'B'
        for child in self.children:      # Step - 2 go to 'B'                     | Step - 5 go to 'E'
            child.depthFirstSearch(array)# Step - 3 call the stack in DFS for 'B' | step - 6 so on and so forth
        return array
"""

def main():
    root = Node('A')
    root.addChild('B').addChild('C')
    root.children[0].addChild('D')
    root.children[0].children[0].addChild('E')
    print(root.depthFirstSearch([])) # ['A', 'B', 'D', 'E', 'C']

if __name__ == '__main__':
    main()