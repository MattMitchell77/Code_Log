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
    # Write your code here
    positive = []
    negative = []
    zero = []
    
    for x in arr:
        if x > 0:
            positive.append(1)
        elif x < 0:
            negative.append(1)
        elif x == 0:
            zero.append(1)
            
    positive_ratio = len(positive) / len(arr)
    print("{:.6f}".format(positive_ratio))
    
    negative_ratio = len(negative) / len(arr)
    print("{:.6f}".format(negative_ratio)) 
    
    zero_ratio = len(zero) / len(arr)
    print("{:.6f}".format(zero_ratio)) 
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
