#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

import math
import os
import random
import re
import sys


try:
    n = int(input())
    print(n)
except ValueError:
    print("Bad String")