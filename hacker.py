#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    neg = 0
    pos = 0
    z = 0
    for i in range(len(arr)):
        if (arr[i] < 0):
            neg += 1
        elif (arr[i] > 0):
            pos += 1
        else:
            z += 1
    neg = neg/len(arr)
    pos = pos/len(arr)
    z = (z/len(arr))
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(z))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
