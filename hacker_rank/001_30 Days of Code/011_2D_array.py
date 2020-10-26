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

def get_hourglass_sum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum
    
arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))

max_hourglass_sum = -63 # sum from - 9 to 9 - > constraints 
for i in range(1,5):
    for j in range(1,5):
        current_hourglass_sum = get_hourglass_sum(arr, i ,j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum

print(max_hourglass_sum)