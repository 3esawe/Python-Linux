#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = sum(map(lambda x : x > 0, arr)) * 1.0/len(arr)
    neg = sum(map(lambda x : x < 0, arr)) * 1.0/len(arr)
    equal = sum(map(lambda x : x == 0, arr)) * 1.0/len(arr)
    print ("%f\n%f\n%f\n" % (pos, neg ,equal))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
