# Breadth-first search is a search algorithm that starts at the root node and explores as far as possible along each branch before backtracking.

# Create a queue and store all future nodes as you visit them. By adding Nodes' children to the queue, everytime you visit them and using FIFO -> you can create a breadth-first search.

# Create/initialize the queue, while que is not empty, pop/dequeue the first node and add it to the visited list (append name of current node to array). For each child in current node, add it to the queue.
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
        queue = [self] # create/initialize the queue
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