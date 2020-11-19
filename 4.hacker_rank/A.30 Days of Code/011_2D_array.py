#Input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

#Output
# 19

#Constraints
# -9 <= A[i][j] <= 9
# 0 <= i, j <= 5

import os
# hourglass
# a b c
#   d    
# e f g

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = []
    for i in range(len(arr)-2): #-2 because (from hour glass), if the pointer is at 'a' it can go to 'b' and then 'c' by adding 1 and then 1 again
        # - 2 is basically done for indexing coz defined by hourglass
        for j in range(len(arr)-2): # -2 because if the pointer is at 'a' it can go go 'e' 'f' 'g' by adding 1 and then 1 again
            sum.append(
                    arr[i][j]
                    +arr[i][j+1]
                    +arr[i][j+2]
                    +arr[i+1][j+1]
                    +arr[i+2][j]
                    +arr[i+2][j+1]
                    +arr[i+2][j+2])
    # print(max(sum)) # debug output
    return(max(sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
