# Array - Reorder entries that even entries appears first

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A
if __name__ == "__main__":
    print(even_odd(A))
    
# Space Complexity - O(1) # couple of variable to hold indices, and temporary variable to perform swap
# Time Complexity  - O(n) # constant amount of processing per entry

# iterating
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def reoder(A):
    i, j = 0, len(A) - 1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] % 2 == 0:
                i += 1
            else:
                A[i], A[j] = A[j], A[i]
                j += 1
    return A

print(reoder(A))