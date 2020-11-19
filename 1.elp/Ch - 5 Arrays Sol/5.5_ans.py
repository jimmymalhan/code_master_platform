# Delete duplicates from a sorted array

# Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and 
# the remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements.
# Many languages have library functions for performing this operation you cannot use these functions.

# Hint: There is an O(n)time and O(1) space solution

# returns the number of valid enteries after deletion.

def delete_duplicates(A):
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

# LC = 0026 Remove Duplicates from Sorted Array