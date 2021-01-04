"""
# Average: O(log(N)) time (because of searching or removal algorithms) | O(log(N)) space(N frames were used on the call stack) or o(D) space where D is depth of the branch
                            # if used iteratively space complexity becomes O(1)- won't be using the frames on the call stack
# Worst: O(N) time| (when BST has only 1 branch) | (N) space
                            # if used iteratively space complexity becomes O(1)
            BST has 1 branch ONLY
                        10 
                        |
                        15
                        |
                        22
                        |
                        30

find closest value to 12 
        10
       /   \
     5      15
    / \    /   \
   2   5  13    22
  /     /    \
 1    None    14
assigning the variable 'closest = inifinity'(best candidate for the closest value)
abs value = rootValue(which is currentNode) - targetValue(12) = |absoluteDifference|
if the |absoluteDifference| b/w infinty and targetValue && rootValue(which is currentNode) and targetValue is less then, value gets updated with the least differnce to the targetValue
|infinity - 12| = infinity |10 - 12| = 2
if infinity < 2: # obviously NO
    therefore- 10(currentNode) is closer to 12(targetValue) than infinity closer to 12
Hence, closest value gets updated in the variable to the currentNode -> closest = 10
    which means right side of the 10(rootValue) >= 12(targetValue) because we are in BST
    AND left side of 10 <= 12 (Don't have to explore and gets ignored)

Next value is 15
so, |15(currentNode) - 12(targetValue)| = 3 vs |10(rootNode)/(closest - assigned variable) - 12(targetValue)| = 2
|15 - 12| = 3 vs |10 - 12| = 2
since, 3(absolute difference of 15) > 2(absolute difference of 10)
    which means 15 is farthest away from 10
    therefore, we don't update the closestValue - which will remain 'closest = 10'
Next Value = 22 gets eliminated because it's greater than 15(which makes the absoluteDifference further away from 15's absoluteDifference) # on average that eliminates, half of the BST
Next Value = 13
|13-12| = 1 vs |10-12| = 2
so, 1 < 2 therefore, 'closest = 1' (value gets updated)
Also, 12(currentValue) < 13(closest value) -> therefore, it elminates any other nodes beyond 13(which is 14 in our case) and also find if there is any other Node(Null or has value)
-> Answer is 13

Edge Case to make it optimal
if the |currentValue - targetValue| = 0 -> hence you found the closestValue (STOP HERE) and 'closest = *updatedValue*' gets updated 
"""
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target- closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None