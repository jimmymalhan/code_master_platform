# The provided code stub reads and integer,n, from STDIN. For all non-negative integers i < n, print i^2.

n = 3

# The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.
# Output
# 0
# 1
# 4

if __name__ == '__main__':
    [print (i**2) for i in range (n)]