class Node:
    def __init__(self, name):
        self.children = []                # contains the graph
        self.name = name                  # root node

    def addChild(self, name):
        self.children.append(Node(name))  # adding the names of children through 'class Node'
        return self

    # v - vertices
    # e - edges
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