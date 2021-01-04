# O(n) time | O(1) space
def findThreeLargestNumbers(array):
	threeLargest = [None, None, None] # Intializing the array
	for num in array: #num is the currentvalue # traversing the array
		updateLargest(threeLargest, num)
	return threeLargest
	
def updateLargest(threeLargest, num):
	if threeLargest[2] is None or num > threeLargest[2]: # compare the currentNumber "num" to the 3rd Value in the 'threeLargest' array represents the largest number
		shiftAndUpdate(threeLargest, num, 2) # shifting numbers to the left in the array
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest, num, 1)
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0)
		
def shiftAndUpdate(array, num, idx):
	for i in range(idx + 1): #idx + 1 is exclusive # 0 to idx
		if i == idx:# At the point of iteration where, we are at last index that have passed in the method
			array[i] = num # update the number to the 'threelargest' array
		else:
			array[i] = array[i + 1] #