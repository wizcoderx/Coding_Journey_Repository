'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

https://www.hackerrank.com/challenges/mini-max-sum
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):

    arr.sort()


    max_ans = sum(arr[:4])
    min_ans = sum(arr[1:])

    print(max_ans, min_ans)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

'''
Alternate approch:

def miniMaxSum(arr):
    total_sum = sum(arr)           # Calculate the total sum of the array
    min_sum = total_sum - max(arr) # Exclude the largest element to get the minimum sum
    max_sum = total_sum - min(arr) # Exclude the smallest element to get the maximum sum
    print(min_sum, max_sum)        # Print the results

'''