# Given, 3 integers x, y and z representing the dimensions of a 
# cuboid 'n'. Print a list of all possible
# coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k
# is not equal to 'n'.
# NOTE : Use list comprehension instead of multiple loops

# 0 <=i <=x
# 0<=j<=y
# 0 <=k <=z

# Sample Input 0

# 1
# 1
# 1
# 2

# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x, y, z, n = [int(input()) for _ in range(4)]
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k !=n])

# Explanation:
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# list = []

# for i in range(0, x + 1):
#     for j in range(0, y + 1):
#             for z in range(0, z + 1):
#                 if i + j + k != n:
#                     list.append([i, j, k])
# print(list)