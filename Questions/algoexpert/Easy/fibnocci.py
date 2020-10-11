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
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n - 1) + getNthFib(n - 2)
#         return memoize[n]

# Solution 3:
# O(n) time |  O(1) space
	
def getNthFib(n):
    lastTwo = [0 , 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

getNthFib(n)
print(getNthFib(n))