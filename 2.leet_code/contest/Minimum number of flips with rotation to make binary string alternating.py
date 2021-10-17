# Function that finds the minimum
# number of flips to make the
# binary string alternating if
# left circular rotation is allowed
def MinimumFlips(s: str) -> int:

    n = len(s)
    a = [0] * n
    
    for i in range(n):
        a[i] = 1 if s[i] == '1' else 0
 
    # Initialize prefix arrays to store
    # number of changes required to put
    # 1s at either even or odd position
    oddone = [0] * (n + 1)
    evenone = [0] * (n + 1)
 
    for i in range(n):
 
        # If i is odd
        if(i % 2 != 0):
 
            # Update the oddone
            # and evenone count
            if(a[i] == 1):
                oddone[i + 1] = oddone[i] + 1
            else:
                oddone[i + 1] = oddone[i] + 0
 
            if(a[i] == 0):
                evenone[i + 1] = evenone[i] + 1
            else:
                evenone[i + 1] = evenone[i] + 0
 
        # Else i is even
        else:
 
            # Update the oddone
            # and evenone count
            if (a[i] == 0):
                oddone[i + 1] = oddone[i] + 1
            else:
                oddone[i + 1] = oddone[i] + 0
 
            if (a[i] == 1):
                evenone[i + 1] = evenone[i] + 1
            else:
                evenone[i + 1] = evenone[i] + 0
 
    # Initialize minimum flips
    minimum = min(oddone[n], evenone[n])
 
    # Check if substring[0, i] is
    # appended at end how many
    # changes will be required
    for i in range(n):
        if(n % 2 != 0):
            minimum = min(minimum, oddone[n] - oddone[i + 1] + evenone[i + 1])
            minimum = min(minimum, evenone[n] - evenone[i + 1] + oddone[i + 1])
 
    # Return minimum flips
    return minimum
 
# Driver Code
 
# Given String
s = "000001100"
 
# Function call
print(MinimumFlips(s))