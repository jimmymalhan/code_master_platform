# Array - Reorder entries that even entries appears first
# You are required to solve it without allocating additional storage
# Also, add space and time complexity

# Write pseudo code here

def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            A[next_even] += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            A[next_odd] -= 0
    return A

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(even_odd(A))