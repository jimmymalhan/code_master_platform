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

recursive - f(n, d) = d + f(l, d +1) + f(r , d + 1)

n - node
d - depth
l - left
r - right
"""

# avg case: when tree is balanced
# O(n) time | O(h) space where n is the number of nodes in the binary tree and h is the height of the binary tree
def nodeDepths(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
"""
recursive - f(n, d) = d + f(l, d + 1) + f(r , d + 1)
n - node
d - depth
l - left
r - right
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# avg case: when tree is balanced
# O(n) time | O(h) space where n is the number of nodes in the binary tree and h is the height of the binary tree
def nodeDepths(root):
	sumOfDepths = 0
	stack = [{"node": root, "depth": 0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths += depth
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})
	return sumOfDepths
"""Iterative
empty stack -> grab root node (1) with the depth 0 and add it to the stack (to know it's depth with the runningNode) -> pop it off the node     # if the stack isn't empty, keep applying the algorithm
grab child nodes (2) and (3) with the depth 1 and add it to the stack (to know it's depth with the runningNode) -> pop it off the node 

"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

