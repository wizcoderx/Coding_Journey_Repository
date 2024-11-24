'''
Objective
In this challenge, we will use loops to do some math. Check out the Tutorial tab to learn more.

Task
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

Example

The printout should look like this:

https://www.hackerrank.com/challenges/30-loops
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        ans = n * i
        print(n,"x",i,"=",ans)
