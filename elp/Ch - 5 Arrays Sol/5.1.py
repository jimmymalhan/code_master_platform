# Dutch National Flag Problem - 
# Write a program that takes an array A and an index i into A,
# rearranges the elements such that all elements less than A[i] 
# (the 'pivot') appears first,
# followed by elements equal to the pivot, followed by elements 
# greater than the pivot.

# Hint - Think about partion step in quick sort

# elements less than pivot, 
# elements equal to pivot,
# elements greater than pivot
RED, WHITE, BLUE = range(3)

def dutch_flag_partition1(pivot_index, A):
    pivot = A[pivot_index] # fetch the value at pivot_index in A and save it to "pivot" variable
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        # Look for a larger element. Stop when we reach an element less 
        # than pivot, since first pass has moved them to start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
# Time complexity is O(1)
# Space complexity is O(n^2)

##########################################################################
# Improve time complexity
RED, WHITE, BLUE = range(3)

def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group elements larger than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break 
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

# Time complexity = O(n) 
# Space complexity = O(1)

##########################################################################
# performs classficiation into elements less than, equal to, 
# and greater than the pivot in a SINGLE PASS
# intally all elements are in unclassified
RED, WHITE, BLUE = range(3)

def dutch_flag_partition3(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partioning:
    # bottom group: A[smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as ling as there is an unclassfied element.,
    while equal < larger:
        # A[equal] is the incoming unclassfied element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
# each iteration decreases the size of unclassfied by 1
# Time complexity = O(n)
# Space complexity = O(1)