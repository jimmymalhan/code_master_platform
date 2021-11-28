# Problem Link: https://www.algoexpert.io/questions/Breadth-first%20Search

# Problem Name: Breadth-first search 

# Problem Description:
# BFS is a search algorithm that starts at the root node and explores as far as possible along each branch before backtracking.

# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form a acyclic tree-like structure. Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the array, and returns it.

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
Explain the solution:


##################
Detailed explanation of the Solution:
Create a queue and store all future nodes as you visit them. By adding Nodes' children to the queue, everytime you visit them and using FIFO.

create the queue
while the queue is not empty
current = pop the first node from the queue - FIFO
append the current node to the array
for each child of the current node
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