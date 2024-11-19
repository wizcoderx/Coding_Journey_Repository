'''
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

https://www.hackerrank.com/challenges/30-conditional-statements
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:

    print("Weird")

elif 2 <= n <= 5:

    print("Not Weird")

elif 6 <= n <= 20:

    print("Weird")

else:

    print("Not Weird")
