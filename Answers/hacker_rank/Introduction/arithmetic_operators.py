# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.


# Explanation
# 3 + 2 = 5
# 3 - 2 = 1
# 3 * 2 = 6

a = 3
b = 2

if __name__ == "__main__":
    # print(a+b)
    # print(a-b)
    # print(a*b)

#or
    # for list in a,b:
    #     print((a+b), (a-b), (a*b))
    #     break
#or
    print('{0} \n{1} \n{2}'.format((a+b), (a-b), (a*b)))