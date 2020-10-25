# list = []
# insert i e: insert e at position i
# print: print the list
# remove e: Delete the first occurence of integer e
# append e: Insert integer e at the end of the list
# sort: sort the list
# pop: the last element from the list
# reverse: reverse the list
 
#Sample Input 0
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print
 
#Sample Output 0
#[6, 5, 10]
#[1, 5, 9 , 10]
#[9, 5, 1]

def handler(result):
    inp = input().split()
    command = inp[0]
    values = inp[1:]
    if command == 'print':
        print(result)
    else:
        execute = 'result.' + command + "(" + ",".join(values) + ")"
        eval(execute)

result = []
for i in range(int(input())):
    handler(result)
