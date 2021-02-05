# special array contains integers or other special arrays -> Recursion problem

# O(n) time | O(d) space = d is depth
def productSum(array, multipler = 1):
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multipler + 1)
		else:
			sum += element
	return sum * multipler