# O(n^2) time | O(1) space
def insertionSort(array):
	# Looping through the array once
	for i in range(1, len(array)): # intialize the 'for' loop # keep inserting numbers to the tentative sorted sublist(very first number of the array)
		j = i # 2nd index
		# looping backwards through the array and doing bunch of swaps to poisition, our current number at current place in the tentatively sorted sublist
		while j > 0 and array[j] < array[j - 1]: # j = current number > 0 (haven't reached the very begining of the array | tentatively sorted sublist)
			# AND while our current number(array[j]) is out of position, less than a number before it (array[j - 1])
			swap(j, j-1, array)
			j -= 1 # decrement j and keep track of the number that we are trying to insert
	return array
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    array = [9,8,4,2,5,3]
    print(insertionSort(array))
