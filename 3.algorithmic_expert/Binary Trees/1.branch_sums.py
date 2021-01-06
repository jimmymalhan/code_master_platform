"""
Branch Sums 
		 1
	   /   \
	  2      3
     / \    / \
	4   5  6   7
   / \  |
  8   9 10

Output - [15, 16, 18, 10, 11]
15 == 1 + 2 + 4 + 8
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7

Depth first Search - 
Begins with left subtree vs right subtree

O(n) time - traversing each of the node and time is constant
O(n) space - returning to empty list(sums) at n number of operations, where half of them are leaf nodes and another half are branch nodes

"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space - where n is the nodes in the Binary Tree
def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, runningSum, sums): # recursive function
	if node is None: # if node is 
		return
	
	newRunningSum = runningSum + node.value
	# if you're running at a leaf node then add it to the sums(empty list), newRunningSum is a branch sum
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	# if not at a leaf node, then keep calculating branch sums(keep going down in the tree)
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)