'''
Steps to Solve
Convert a Decimal Number to Binary:

Take the given base-10 integer
N
n and convert it to a binary representation (base-2).
Find the Longest Streak of Consecutive 1's in the Binary Representation:

Look at the binary string and find the maximum number of consecutive 1s that occur in the string.
Output the Length of the Longest Streak:

Print the length of the longest consecutive sequence of 1s as a base-10 integer.
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # Convert the given integer to binary and find the longest sequence of consecutive 1's


    # Convert n to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]

    # Split the binary representation by '0' to find groups of consecutive 1's
    groups_of_ones = binary_representation.split('0')

    # Find the length of the longest group of consecutive 1's
    max_consecutive_ones = max(len(group) for group in groups_of_ones)

    # Output the result
    print(max_consecutive_ones)

