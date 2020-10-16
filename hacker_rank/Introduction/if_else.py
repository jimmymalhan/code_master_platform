# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird <-
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird <-
# If n is even and greater than 20, print Not Weird

# Test Cases:
# n = 3 -> Weird
# n = 24 -> Not Weird

#!/bin/python3

import os
import random
import re
import sys

n = 24

if __name__ == '__main__':
    if n % 2 != 0 or n in (range(6, 21)):
        print("Weird")
    else:
        print('Not weird')  