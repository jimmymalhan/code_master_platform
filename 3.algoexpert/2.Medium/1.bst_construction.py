class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
# Average: O(log(n)) time | O(1) space
# Worst : O(n) time | O(1) space

    def insert(self, value):
		currentNode = self # insertion node | also, tell you where you are with the current node
		while True:
			if value < currentNode.value: # traverse left subtree
				if currentNode.left is None: 
					currentNode.left = BST(value) # successfully inserted the value
					break
				else: # currentNode.left is not None, still have left subtree to explore
					currentNode = currentNode.left #currentNode.left - assigning it to left subtree
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self

# Average: O(log(n)) time | O(1) space
# Worst : O(n) time | O(1) space	

    def contains(self, value):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.self
			elif value > currentNode.value:
				currentNode = currentNode.right
			else: 
				return True
		return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self