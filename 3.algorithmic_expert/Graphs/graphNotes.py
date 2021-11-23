# # itialize 6x6 grid with 0s dynamically

# class Grid:
#     def __init__(self, n):
#         self.n = n
#         self.grid = [[0 for i in range(n)] for j in range(n)]

#     def grid_print(self):
#         for i in range(self.n):
#             for j in range(self.n):
#                 print(self.grid[i][j], end=" ")
#             print()

# def main():
#     n = int(6) # 6x6 grid
#     grid = Grid(n)
#     grid.grid_print()

# # output:
# # 0 0 0 0 0 0 
# # 0 0 0 0 0 0 
# # 0 0 0 0 0 0 
# # 0 0 0 0 0 0 
# # 0 0 0 0 0 0 
# # 0 0 0 0 0 0 

# if __name__ == "__main__":
#     main()

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]
# # horizontal_matrix 
# j = matrix[0][0] # first row first column
# k = matrix[0][1] # first row second column
# l = matrix[0][2] # first row third column
# m = matrix[0][3] # first row fourth column
# n = matrix[0][4] # first row fifth column

# c = matrix[1][0] # second row first column
# d = matrix[1][1] # second row second column 
# e = matrix[1][2] # second row third column
# f = matrix[1][3] # second row fourth column
# g = matrix[1][4] # second row fifth column
# print(j, k, l, m, n) # 1 0 0 1 0
# print(c, d, e, f, g) # 1 0 1 0 0

# # vertical_matrix
# h = matrix[2][0] # third row first column
# i = matrix[3][0] # fourth row first column
# j = matrix[4][0] # fifth row first column 
# print(h, i, j) # 0 1 1

# for i in range(len(matrix)):
#     print(matrix[i]) # print the whole matrix
#     for j in range(len(matrix[i])): 
#         print(j, end=" ") # what is j? # j is the index count of the row on the pointer for 'i'
#         # 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4
# # 0 1 2 3 4 [1, 0, 1, 0, 0]
# # 0 1 2 3 4 [0, 0, 1, 0, 1]
# # 0 1 2 3 4 [1, 0, 1, 0, 1]
# # 0 1 2 3 4 [1, 0, 1, 1, 0]

a = [[False for col in matrix[0]] for row in matrix] # initialize a 2d array with False
b = [[False for value in row] for row in matrix] # initialize a 2d array with False
c = [[0 for value in row] for row in matrix] # initialize a 2d array with 0s

print(a)
print(b)
print(c)