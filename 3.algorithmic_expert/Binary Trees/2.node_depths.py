"""
tree =              1
                  /   \
                2       3
               / \     /  \
              4   5   6    7
            /   \
           8     9

Sample Output - 16
The depth of the node with value 2 is 1. # process of calculation DEPTH of the tree (DFS) begins from the ROOT of the node
The depth of the node with value 3 is 1.
The depth of the node with value 4 is 2. # to get the depth of the CHILD, need to know the depth of the PARENT- rootNode
The depth of the node with value 5 is 2.
The depth of the node with value 6 is 2.
The depth of the node with value 7 is 2.
The depth of the node with value 8 is 3.
The depth of the node with value 9 is 3.
Summing all of these depths yields 16.

1
3 2
3 5 4
3 4 9 8
3 5 9
3 5
3

recursive - f(n, d) = d + f(l, d +1) + f(r , d + 1)

n - node
d - depth
l - left
r - right
"""
"""
recursive - f(n, d) = d + f(l, d + 1) + f(r , d + 1)
n - node | d - depth | l - left | r - right
"""
# avg case: when tree is balanced
# O(n) time | O(h) space where n is the number of nodes in the binary tree and h is the height of the binary tree
def nodeDepths(root, depth=0):
	if root is None: # base case - if node has null value
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1) # adding depth to the runningSum

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""Iterative
empty stack -> grab root node (1) with the depth 0 and add it to the stack (to know it's depth with the runningNode) -> pop it off the node     # if the stack isn't empty, keep applying the algorithm
grab child nodes (2) and (3) with the depth 1 and add it to the stack (to know it's depth with the runningNode) -> pop it off the node 
"""

# avg case: when tree is balanced
# O(n) time | O(h) space where n is the number of nodes in the binary tree and h is the height of the binary tree
def nodeDepths(root):
	sumOfDepths = 0 # runningSum for all the depths
	stack = [{"node": root, "depth": 0}] # to find the depth ? node needs to be stored as well
	while len(stack) > 0: # so long, when the stack is non-empty
		nodeInfo = stack.pop() # keeps poping the node
		node, depth = nodeInfo["node"], nodeInfo["depth"] # defining variables to it's value
		if node is None: # check if the node value is null
			continue
		sumOfDepths += depth # add it to the current depth
		stack.append({"node": node.left, "depth": depth + 1}) #adding children left
		stack.append({"node": node.right, "depth": depth + 1}) #adding children right
	return sumOfDepths


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

