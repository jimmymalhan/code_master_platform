# O(n) time | O(1) space
def findThreeLargestNumbers(array):
	threeLargest = [None, None, None] # Intialize the array
	# traversing the array and update the threeLargest accordingly
	for num in array: #num is the currentvalue 
		updateLargest(threeLargest, num) # helper method to pass arguments
	return threeLargest
	
def updateLargest(threeLargest, num):
	if threeLargest[2] is None or num > threeLargest[2]: # compare the currentNumber "num" to the 3rd Value in the 'threeLargest' array which represents THE largest number
		shiftAndUpdate(threeLargest, num, 2) # shifting numbers to the left in the array
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest, num, 1)
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0)
		
def shiftAndUpdate(array, num, idx):
	for i in range(idx + 1): #idx + 1 is exclusive so, we are going from [0 to idx]
		if i == idx:# At the point of iteration where, we are at last index that have passed in the method
			# i = 0
			# i = 1
			# i = 2
			# idx = 2
			array[i] = num # update the array[i] to the number
		else:
			array[i] = array[i + 1]

"""example # passing index '2'
[0, 1, 2] # indices
[x, y, z]
for i in range(0, 2 + 1) # + 1 is excluded in the range
if i == 2:
	[x, y, num] #z gets updated 
else:
	[y, z, num]# since, it's +1, x becomes y, y becomes z and z becomes num
"""