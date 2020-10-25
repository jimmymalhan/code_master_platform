# for each name queried print->  name = phonebook
# if not found print -> print Not found

# Constraints
# 1 <= n <= 10^5
# 1 <= queries <= 10^5

# Sample input
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

# Sample Output
# sam=99912222
# Not found
# harry=12299933

import sys

n = int(sys.stdin.readline().strip())
phone_book = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split(' ')
    phone_book[entry[0]] = entry[1] # this is setup based on sample input. So Index 0 (entry) is name and index 1 is phone_number (entry)

query = sys.stdin.readline().strip() # reading the queries
while query:
    phone_number = phone_book.get(query)
    if phone_number: #if phone_number exists print it
        print(query + '=' + phone_number) 
    else: #if phone number doesn't exist
        print('Not found')
    query = sys.stdin.readline().strip()