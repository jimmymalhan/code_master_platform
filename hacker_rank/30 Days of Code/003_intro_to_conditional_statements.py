    N = 24
    if N % 2 != 0 or (N % 2 == 0 and N in (range(6, 21))):
        print('Weird')
    else:
        print('Not Weird')