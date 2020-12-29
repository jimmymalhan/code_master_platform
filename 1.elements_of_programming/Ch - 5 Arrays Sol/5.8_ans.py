# Computing an Alternation

# Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array B having the property that
# B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ... 

# Hint: Can you solve the problem buy making local changes to A?

# Iterating through an array and swapping A[i] and A[i + 1] when i is even AND
# A[i] > A[i + 1] or i is odd and A[i] < A[i + 1]


for i in range(len(A)):
    A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
