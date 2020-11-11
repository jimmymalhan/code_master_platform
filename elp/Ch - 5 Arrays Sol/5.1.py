# Dutch National Flag Problem - 
# Write a program that takes an array A and an index i into A, rearranges the elements such that all elements less than A[i] (the 'pivot') appears first,
# followed by elements equal to the pivot, followed by elements greater than the pivot.

# Hint - Think about partion step in quick sort

# Time complexity is O(n)
# Space complexity is O(n)
def dutch_flag_partiion(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

# Second pass: group elements larger than pivot.
for i in reversed(range(len(A))):
    if A[i] < pivot:
        break
    # Look for a larger element. Stop when we reach an element less 
    # than pivot, since first pass has moved them to start of A.
        for j in reversed(range(len(A))):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break