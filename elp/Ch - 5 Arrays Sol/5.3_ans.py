# Multiply two aribitary precision integers

# Write a program that takes two arrays representing integers, and returns an integer representing their product.
# For example, since 193707721 x -761838257287 = -127573952589676412927, if the inputs are {1,9,3,7,0,7,7,2,1} and
# {-7,6,1,8,3,8,2,5,7,2,8,7}, your function should return {-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7}

# Hint: Use arrays to simulate the grade-school multuplication algorithm
def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs (num2[0])

    result = [0] * (len(num1)+ len(num2))
    for i in reversed(range(len(num1):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # remove the leading zeroes.
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return[sign * result[0] + result[1:]]

# There are m partial product, each with at most n + 1 digits. We perform O(1) operations on each digit in each 
# partial product, so the 
# time complexity = O(nm)  