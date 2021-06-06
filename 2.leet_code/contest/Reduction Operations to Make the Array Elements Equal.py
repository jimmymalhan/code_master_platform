# Function to return minimum operations need
# to be make each element of array equal
def minCost(A, n):
     
    # Initialize cost to 0
    cost = 0
     
    # Sort the array
    A.sort();
     
    # Middle element
    K = A[int(n / 2)]
     
    #Find Cost
    for i in range(0, n):
        cost = cost + abs(A[i] - K)
     
    # If n, is even. Take minimum of the
    # Cost obtained by considering both
    # middle elements
    if n % 2 == 0:
        tempCost = 0
        K = A[int(n / 2) - 1]
         
        # FInd cost again
        for i in range(0, n):
            tempCost = tempCost + abs(A[i] - K)
         
        # Take minimum of two cost
        cost = min(cost, tempCost)
         
    # Return total cost
    return cost
     
# Driver code
A = [1, 6, 7, 10]
n = len(A)
 
print(minCost(A, n))
         
# This code is contributed
# by Shashank_Sharma