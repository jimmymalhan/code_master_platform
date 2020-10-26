# parse an integer from a string and print custom error message
# Read a string S and print its integer value
# if S can't be converted to an integer, print Bad String
# NOTE - without using loops

#Constraints
# 1 <= |S| <=6, S is length of String
# S is composed of either lowercase letters(a-z)
# or decimal digit (0 -9)

try:
    S = int(input().strip())
    print(S)
except ValueError:
    print('Bad String')
