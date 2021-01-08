"""
tree =              1
                  /   \
                2       3
               / \     /  \
              4   5   6    7
            /   \
           8     9

Sample Output - 16
The depth of the node with value 2 is 1.
The depth of the node with value 3 is 1.
The depth of the node with value 4 is 2.
The depth of the node with value 5 is 2.
Etc..
Summing all of these depths yields 16.
"""

# avg case: when tree is balanced
# O(n) time | O(h) space where n is the number of nodes in the binary tree and h is the height of the binary tree
def nodeDepths(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

# This is the class of the input binary tree.
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
	
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

