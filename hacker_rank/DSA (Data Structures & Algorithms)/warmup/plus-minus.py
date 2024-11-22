'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

https://www.hackerrank.com/challenges/plus-minus
'''

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
    n = len(arr)
    zero_count = 0
    positive_count = 0
    negative_count = 0

    for num in arr:
        if num>0:
            positive_count +=1
        elif num<0:
            negative_count +=1
        else:
            zero_count += 1


    #calculate the ratios
    zero_count_ratio = zero_count/n
    positive_count_ratio = positive_count/n
    negative_count_ratio = negative_count/n

    print(f"{positive_count_ratio:.6f}")
    print(f"{negative_count_ratio:.6f}")
    print(f"{zero_count_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
