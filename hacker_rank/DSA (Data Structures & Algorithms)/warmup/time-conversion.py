'''
The image provides a problem description where you need to convert a given time in a 12-hour AM/PM format to a 24-hour (military) time format.

Explanation of the Task:
You are given a string s that represents the time in a 12-hour AM/PM format, such as 12:01:00PM or 12:01:00AM.
The task is to convert this time into a 24-hour time format.
Conversion Rules:
AM and PM conversions:
For AM: If the hour is 12 (i.e., 12:00AM), it should be converted to 00 (midnight).
For PM: If the hour is 12 (i.e., 12:00PM), it remains 12 (noon).
For any other hour, if it’s in AM, it stays the same except for converting the 12-hour format to 24-hour format.
For PM, add 12 to the hour if it's not 12 (for example, 1:00PM becomes 13:00).

https://www.hackerrank.com/challenges/time-conversion
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    minutes_seconds = s[2:-2]

    if period == "AM":
        # Special case for 12 AM
        if hour == 12:
            hour = 0
    else:
        # Special case for 12 PM
        if hour != 12:
            hour += 12

    # Format hour to two digits (e.g., 01, 13)
    return f"{hour:02}{minutes_seconds}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
