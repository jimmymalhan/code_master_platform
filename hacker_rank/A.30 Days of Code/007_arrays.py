# first line contains an integer N(the size of our array)
# second line contains N space-seperated integers describing array A's elements

# Constraints
# 1 <= N <= 1000
# 1 <= Ai <= 10000, where Ai is the ith iteger in the array

# Sample Input
# 4
# 1 4 3 2

# Sample Output
# 2 3 4 1

n = int(input())
arr = list(map(int, input().rstrip().split()))
reversed_array = []
for i in range(n):
    reversed_array.append(arr[n - i - 1]) 
    # explaining based on sample input
    # i = 0 at begining , n = 4 | 4 - 0 - 1 [n-i-1] = 3 (index vaule is 3) and then gets append to the array (output) at index 0
    # i = 1, n = 4 | 4 - 1 - 1 = 2 (index value is 2) and then gets append to the array (output) at index 1 ans sooo on..

print(' '.join(str(i) for i in reversed_array))

# print(*reversed(arr))