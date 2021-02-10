# Nth Fibonacci

n = 6

# Solution 1:
#O(2^n) time | O(n) space

# def getNthFib(n):
# 	if n == 2:
# 		return 1
# 	if n == 1:
# 		return 0
# 	else:
# 		return getNthFib(n - 1) + getNthFib(n - 2)

# Solution 2:
#O(n) time | O(n) space

# def getNthFib(n, memoize={2: 1, 1: 0}):
#     if n in memoize: # values stored in hash map can be utilized
#         return memoize[n] # once value is calculated, it's stored on hashmap (don't need to calculate again)
#     else:
#         memoize[n] = getNthFib(n - 1) + getNthFib(n - 2)
#         return memoize[n]

# Solution 3:
# O(n) time |  O(1) space
	
def getNthFib(n):
	lastTwo = [0, 1] # first two fib numbers
	counter = 3 # 3rd fib number which gets updated based on nextFib asked to calculate
	while n >= counter: # looping through everytime, whenever asked value of n >= counter
		nextFib = lastTwo[0] + lastTwo[1] # calculate next fib (only storing 2 values)
		lastTwo[0] = lastTwo[1] # removing the first calculated value from the list
		lastTwo[1] = nextFib # nextFib is calculated
		counter += 1 # moving on to the nextfib # next fib value is added as 2nd Fib
	return lastTwo[1] if n > 1 else lastTwo[0] # returning lastTwo[1] for the edge case that if asked to return for lastTwo[1] (1st element)

getNthFib(n)
print(getNthFib(n))