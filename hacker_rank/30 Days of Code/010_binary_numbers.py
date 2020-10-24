if __name__ == '__main__':
    n = int(input())

    count = 0
    while n:
        n &= n << 1 # n is shifted to the left by 1 places
        #https://wiki.python.org/moin/BitwiseOperators
        count += 1

    print(count)
