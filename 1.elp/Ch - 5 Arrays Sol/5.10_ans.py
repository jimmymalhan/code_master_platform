# Permute the elements of an array

# What is permutation?
# A permutation can speciffied by an array P, where P[i] represents the location 
# of the element at i in the permutation. For example, the array[2,0,1,3] represents
# the permutation that maps the element at location 0 to location 2, the element at
# location 1 to 0, the element at location 2 to location 1 and keep the element at 
# location 3 unchanges. A permutation can applied to an array to reorder the array. 
# For example, the permutation [2, 0 ,2, 3] applied to A = [a, b, c, d] yields [b,c a, d].

# Given an array A of n elements and permutation P, apply P to A.

# Hint: Any permutation can be viewed as a set of cyclic permuatations. For an element in
# a cycle, how would you identify if it has been permuted? 

# Solution 1 - create new array
# If additonal storage is available. We allocate a new array B of the same length, set
# B[P[i]] = A[i] for each i, and then copy B to A.
# The time complexity is O(n), and the
# additional space complexity is O(n).

# Solution 2 - swap the elements
# A key insight to improving space complexity is to decompose permutations into simpler
# structures which can be processed incrementally. For example, consider the permutation
# [3,2,1,0]. To apply it to an array A = [a, b, c, d], we move the element at index 0[a]
# to index 3 and the element already at index 3[d] to index(0). Continuing, we move all
# the element at index 1 (b) to index 2 and the element aldreadt at index (c) to indexx 1.
# Now all elements have been moved according to the permutation, and the result is 
# [d,c,b,a].
# This EXAMPLE, gernalizes: every permuation can be represented by a collection of independent
# permutations, each of which is cyclic, that is, it moves all elements by a fixed offset,
# wrapping around.
# This is  significant, because a single cyclic permutation can be performed one element at
# a time, i.e., with constant additional storage. Therefore, we want to identify the disjoint
# cycles that constitutes the permutation.
# It is trivial to do this by storing a Boolean for each array element.

# Solution 3-  SUBTRACT n from P[i] after applying (NOT USING EXTRA SPACE)
# One way to perform this without explicitly using additional O(n) storage is to use the sign bit
# in the entries in the permutation-array. Specifically, we subtract n from P[i] after applying it.
# This means that if an entry in P[i] is negative, we have performed the corresponding move. 
# EXAMPLE: to apply [3,1,2,0], we begin with the first entry, 3. We move A[0] to A[3], first saving
# the original A[3]. We update the permutation to [-1,1,2,0]. We move A[3] to A[0]. Since P[0]
# is negative we know we are done with the cycle starting at 0. We update the permutation to [-1,1,3,-4].
# Now we examine P[1]. Since it is not negative, it means the cycle it belongs to cannot have been applied. 

def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtract len(perm) from an array in perm to make it negative, which indicates the corresponding
            # move has been performed.
            perm[next] -= len(perm)
            next = temp
        # Restore perm
        perm[:] = [a + len(perm) for a in perm]
# Time Complexity is O(n).
# The space complexity is O(1), ASSUMING we can temporarily modify the sign bit from entries in the permutation array.

# Clean way to write:
def apply_permutation(A,P):
    for i in range(len(A)):
        next = i
        while P[next] >=0:
            A[next], A[P[next]] = A[P[next]], A[next]
            next = P[next]
            # make P[next] negative once it is used
            P[next] -= len(A)
    return A

# https://www.geeksforgeeks.org/permute-the-elements-of-an-array-following-given-order/
# Approach: Every permutation can be represented by a collection of independent permutations, each of which is cyclic i.e. 
# it moves all the elements by a fixed offset wrapping around. To find and apply the cycle that indicates entry i, 
# just keep going forward (from i to P[i]) till we get back at i. After completing the current cycle, find another cycle
# that has not yet been applied. To check this, subtract n from P[i] after applying it. This means that if an entry in 
# P[i] is negative, we have performed the corresponding move.

def apply_permutation(A,P):
    for i in range(len(A)):
        next = i
        while P[next] >=0:
            A[next], A[P[next]] = A[P[next]], A[next]
            next = P[next]
            # make P[next] negative once it is used
            P[next] -= len(A)
    return A

if __name__ == '__main__': 
    A = [5, 6, 7, 8] 
    P = [3, 2, 1, 0] 
  
    print(apply_permutation(A, P))
# Time Complexity is O(n).
# The space complexity is O(1), ASSUMING we can temporarily modify the sign bit from entries in the permutation array.