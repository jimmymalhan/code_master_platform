# Given, a space 'n' integers as input
# create a tuple 't' of those 'n' integers
# compute and print the result of hash(t)
# Note: hash() is one of the functions in __builtins__
# module, so it needs to be imported

# input format
# first line contains an integer 'n', denoting the
# elements in the tuple.
# the second line contains n space-separated integers
# describing the elements in tuple 't'.

# Output format
# print the result of hash(t)

n = int(input())
integer_list = input().split()
for i in range(len(integer_list)):
    integer_list[i] = int(integer_list[i])
t = tuple(integer_list)
print(hash(t))