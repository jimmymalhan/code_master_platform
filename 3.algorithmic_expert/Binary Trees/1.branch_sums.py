"""
Branch Sums 
# 1 will be passing down	         1 	|(0) starts from + 1) = 1 runningSum # 1 will be passing down
					              /     \
   3 = 2 + runningSum(1)        2         3    |(1)runningSum + 3 = 4 # 4 will be passing down
# 3 will be passing down       / \      /   \
7 = 4 + runningSum(3)	      4   5(3)  6(4) 7 |(4)runningSum | 6 + 4 = 10 and 7 + 4 = 11 # No leaf nodes for left and right, return output
# 7 & 8 will be passing down /  \   |  			
				         (7)8 (7)9 10(8) | 7 + 8 = 15, 7 + 9 = 16, 10 + 8 = 18 # No leaf nodes for left and right, return output
Depth First Search - 
Begins with left subtree vs right subtree from the rootNode

Output - [15, 16, 18, 10, 11]
15 == 1 + 2 + 4 + 8
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7

O(n) time - traversing all the nodes value and running at constant time operations
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