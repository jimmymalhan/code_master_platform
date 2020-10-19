#!/bin/python3

import os
import sys

def timeConversion(s):
    ampm = s[8:]
    hr = int(s[0:2])
    if ampm == 'PM':
        if hr ==12:
            print(s[0:8])
        else:
            hr = hr + 12
            print(str(hr)+s[2:8])
    elif hr == 12:
        print('00'+s[2:8])
    else:
        print(s[0:8])

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)