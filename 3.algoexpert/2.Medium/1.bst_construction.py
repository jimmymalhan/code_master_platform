class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
	# Average: O(log(n)) time | O(1) space
	# Worst : O(n) time | O(1) space
    def insert(self, value):
		currentNode = self ## intialize the current node | also, tell you where you are with the current node
		while True:
			if value < currentNode.value: # traverse left subtree
				if currentNode.left is None: 
					currentNode.left = BST(value) # successfully inserted the value
					break
				else: # currentNode.left is not None, still have left subtree to explore
					currentNode = currentNode.left #currentNode.left = assigning it to left subtree
			else: # traverse right subtree
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
			if value < currentNode.value: # if value is less than explore left subtree
				currentNode = currentNode.left
			elif value > currentNode.value: # or if value is greater than, explore right subtree
				currentNode = currentNode.right
			else: # or value == currentNode.value # found the value
				return True
		return False # if currentNode is None or null |  value didn't match

    def remove(self, value, parentNode = None):
    	currentNode = self 
		while currentNode is not None:  # removal is two step process 1) find the node 2) remove the node
			if value < currentNode.value: 
				parentNode = currentNode # keep track of parent/root node coz to reassign child node to the parent of the node we are removing
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			else: # value is == currentNode and found the value | Deals with 2 subcases
				if currentNode.left is not None and currentNode.right is not None: # FIRST SUBCASE - ROOT HAS 2 CHILD NODES
					currentNode.value = currentNode.right.getMinValue() # get the smallest value in the given right subtree
					currentNode.right.remove(currentNode.value, currentNode) # currentNode.value = smallest value of right subtree # currentnode is passing as parentNode
				elif parentNode is None: # SECOND SUBCASE - ROOT DOESN't HAVE 2 CHILD NODES | RooT node doesn't have a parentNode
					if currentNode.left is not None: # if the child node is the left node > replace the values with left node
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left # important to assign the left value in the last line so as to overwrite
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right # important to assign the right value in the last line so as to overwrite
					else: # root node which doesn't have a parent node and root node which doesn't have the children node # This is a single-node tree; do nothing
						pass # currentNode.value = None
				elif parentNode.left == currentNode: # ONLY have 1 child node or none and if the node is left child or right child
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right # left child of the parent node
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right # right child of the parent node
				break
		return self

	def getMinValue(self): # calling for right subtree
		currentNode = self
		while currentNode.left is not None: # traverse to left of the right subtree to see if there is None value > return the value
			currentNode = currentNode.left
		return currentNode.value