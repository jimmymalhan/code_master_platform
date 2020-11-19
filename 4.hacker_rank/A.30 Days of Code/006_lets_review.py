# S = str of length N > idx 0 to N-1
#print even-idx and odd-idx char 
# as 2 space-separated strs on a single line

# Constraints
# 1 <= T <= 10
# 2 <= length of S <= 10000

# Sample Input 
# 2
# Hacker
# Rank

#Sample Output
# Hce akr
# Rn ak

num_test_cases = int(input())

for i in range(num_test_cases):
    test_str = input()
    even_idx_char = ''
    odd_idx_char = ''

    for j in range(len(test_str)):
        if j % 2 == 0:
            even_idx_char += test_str[j]
        else:
            odd_idx_char += test_str[j]
    
    print('{} {}'.format(even_idx_char, odd_idx_char))