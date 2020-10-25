#Find the score of runner up

#Constraints
# 2 <=n <= 10
# -100 <= A[i]

# Sample input
# 5
# 2 3 6 6 5

# Sample Output
# 5

i = int(input())
lis = list(map(int,input().strip().split())) #generates the list
z = max(lis) # find the maximum value in the list
while z == max(lis):
    lis.remove(max(lis)) # removing the maximum number in the list
print(max(lis)) # printing the 2nd biggest number (Runner-up) in the list