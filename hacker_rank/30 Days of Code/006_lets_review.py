# S = string of length N > INDEXED 0 to N-1
#print even-INDEXED and odd-INDEXED characters 
# as 2 space-separated strings on a single line

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
    test_string = input()
    even_indexed_characters = ''
    odd_indexed_characters = ''

    for j in range(len(test_string)):
        if j % 2 == 0:
            even_indexed_characters += test_string[j]
        else:
            odd_indexed_characters += test_string[j]
    
    print('{} {}'.format(even_indexed_characters, odd_indexed_characters))