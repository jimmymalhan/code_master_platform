# Problem Name: Breadth-first Search 

# Problem Description:
# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form a acyclic tree-like structure. Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the array, and returns it.

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
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
####################################
"""
Explain the Solution:
1. The Breadth-First Search algorithm works by traversing a graph level by level i.e before traversing any Node's children Nodes, its sibling nodes must be traversed first.
2. Using a queue to store all of the future Nodes that you will need to explore as you traverse the graph. 
  - By adding Nodes children Nodes to the queue everytime you explore them an by using FIFO property of the queue, you can traverse the graph in a BFS manner. - - Don't forget to add every Nodes' name to eh array as you traverse the graph.

##################
Detailed explanation of the Solution:
create the queue as list for self
while the length of queue is greater than 0:
    initialize current = pop the first index from the queue - FIFO
    append the current.name(node) to the array
    for each child of the current.children(node)
        add the child to the queue
return the array
"""
####################################

import unittest
class Node:
    def __init__(self, name):
        self.children = [] # list of children
        self.name = name # name of node

    def addChild(self, name):
        self.children.append(Node(name)) # add child to list of children
        return self # return self to allow chaining

    # v - vertices | # e - edges
    # O(v + e) time | O(v) space          # v frames on call stack

    def breadthFirstSearch(self, array):
        queue = [self] # create queue
        while len(queue) > 0: # while queue is not empty
            current = queue.pop(0) # pop first item from queue - FIFO
            array.append(current.name) # append name of current node to array
            for child in current.children: # for each child in current node
                queue.append(child) # add child to queue
        return array
    
def main():
    root = Node("A")
    root.addChild("B").addChild("C").addChild("D")
    root.addChild("E").addChild("F").addChild("G")
    root.addChild("H").addChild("I").addChild("J")
    print(root.breadthFirstSearch([]))

if __name__ == "__main__":
    main()

class Test(unittest.TestCase):
    def test_node(self):
        root = Node("A")
        root.addChild("B").addChild("C").addChild("D")
        root.addChild("E").addChild("F").addChild("G")
        root.addChild("H").addChild("I").addChild("J")
        self.assertEqual(root.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

def main():
    unittest.main()

if __name__ == "__main__":
    main()