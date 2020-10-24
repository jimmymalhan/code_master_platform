i = int(input())
lis = list(map(int,input().strip().split())) #generates the list
z = max(lis) # find the maximum value in the list
while z == max(lis):
    lis.remove(max(lis)) # removing the maximum number in the list
print(max(lis)) # printing the 2nd biggest number (Runner-up) in the list
