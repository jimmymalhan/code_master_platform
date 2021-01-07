"""
Branch Sums 
# 1 will be passing down	         1 	|(0)runningSum for rootNode + 1 = 1 	#1 will be passing down
					              /     \
   3 = 2 + runningSum(1)        2         3    |(1)runningSum + 3 = 4 	#4 will be passing down
# 3 will be passing down       / \      /   \
7 = 4 + runningSum(3)	      4   5(3)  6(4) 7 |(4)runningSum | 6 + 4 = '10' and 7 + 4 = '11' 	#No leaf nodes for left and right, return output
# 7 & 8 will be passing down /  \   |  			
				         (7)8 (7)9 10(8) | 7 + 8 = '15', 7 + 9 = '16', 10 + 8 = '18' 	#No leaf nodes for left and right, return output

* Depth First Search is Applied
* Begin traversing with left subtree vs right subtree from the rootNode

Output - [15, 16, 18, 10, 11]
15 == 1 + 2 + 4 + 8
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7

O(n) time - traversing all the nodes value and running at constant time operations
<<<<<<< HEAD
O(n) space - returning to empty list(sums) at n number of operations, where half of them are leaf nodes and another half are branch nodes
"""

# using depth first Search - from left to right
# calculate branchSums - based on runningSum and append to the new list
# edge case - if branch has one leaf or null node, return none
# calculate branch for left and right node

=======
O(n) space - We are not gonna exceed n node operations.  
			1) List of branch sums [15, 16, 18, 10, 11] - complicated - counted by branch sums (branch nodes and lead nodes). You will never have more than n nodes.
			2) recursive nature of the algorithm - multiple function calls on call stacks recursively 
				For balanced BST at average O(n) space- O(logn(n))
										unlike, 1 super long branch without nodes
														1
														|
														2
														|
														3
														|
														4
														|
														5
"""

>>>>>>> 88debf1601ce1689cbc4a068c8c1818e5b1badd9
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space - where n is the nodes in the Binary Tree

def branchSums(root):
	sums = [] # List
	calculateBranchSums(root, 0, sums) # 0 is the runningSum for rootNode (see conceptual Overview)
	return sums

def calculateBranchSums(node, runningSum, sums): # recursive function
<<<<<<< HEAD
	if node is None: # if branch has one child or node has null value
=======
	if node is None: # if node have 1 child or null value
>>>>>>> 88debf1601ce1689cbc4a068c8c1818e5b1badd9
		return
	
	newRunningSum = runningSum + node.value #newRunningSum is a branch sum
	if node.left is None and node.right is None: # if you're running at a leaf node then append add it to the sums(empty list) 
		sums.append(newRunningSum)
		return
	# if not at a leaf node, then keep calculating branch sums/keep going down in the tree(traversing down)
	calculateBranchSums(node.left, newRunningSum, sums) # recursively calling
	calculateBranchSums(node.right, newRunningSum, sums) # recursively calling