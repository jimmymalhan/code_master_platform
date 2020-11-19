# FOR n * i = result 
# print in this format:
# n x i = result 

# Constraints 
# (where 1<= i <= 10)

n = int(input().strip())
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))