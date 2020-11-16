# Write a program which takes an array of n integers, 
# where A[i] denotes the maximum you can advance from
# index i, and returns whether it is possible to advance
# to the last index starting from the begining of the array
 
# Hint: Analyse each location, starting from the begining
# non- negative integers are included
def can_reach_end(A):
    furthest_reach_so_far, last_index = 1, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

# time complexity is O(n)
# space complexxity O(1)