# Ques - Array - Reorder entries that even entries appears first
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]



# Pg - 39 - List Comprehension
[print(x**2) for x in range(6)]

[print(x**2) for x in range(6) if x % 2 == 0]

# # # Product of sets 
A = [1, 3, 5]
B = ['a', 'b']
print = [print(x, y) for x in A for y in B]

# # Ques - Covert a 2D list to 1D list as list comprehension
M = [['a', 'b', 'c'], ['d', 'e', 'f']]

# for row in M:
#     print(M)
#     for x in row:
#         print(x)
[print(x) for row in M for x in row]
