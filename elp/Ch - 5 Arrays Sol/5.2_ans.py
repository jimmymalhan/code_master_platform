# Increment an aribitary-precision integer

# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D
# and updates the array to represent the integer D + 1. For example, if the input is [1, 2, 9] then
# you should update the array to [1, 3, 0]. Your algorithm should work even if its implemented in a
# language that has finite - precision arithemetic. 

# Hint:  Experiment with concrete examples # carry out # D + 1 

A = [1,2,9]

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # There is a carry-out, so we need one more digit to store the result.
        # A slick way to do this is to append to 0 at the end of the array, 
        # and update the first entry to 1.
        A[0] = 1
        A.append(0)
    return A

print(plus_one(A))
# Time complexity = O(n), where n is the length of A

