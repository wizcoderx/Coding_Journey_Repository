"""
A leap year is a year in which an extra day is added to the calendar on February 29.
This corrects the calendar for the fact that it takes approximately 365.25 days for the Earth to orbit the sun.

In the Gregorian calendar, a leap year is identified using the following conditions:
1. The year must be evenly divisible by 4, unless:
2. The year is evenly divisible by 100, in which case it is NOT a leap year, unless:
3. The year is also evenly divisible by 400, in which case it IS a leap year.

For example:
- The years 2000 and 2400 are leap years.
- The years 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years.

Task:
Given a year, determine if it is a leap year.
Return True if it is a leap year, otherwise return False.

Input:
- An integer representing a year.

Output:
- A Boolean value: True if the year is a leap year, False otherwise.

Problem URL: https://www.hackerrank.com/challenges/write-a-function
"""

def is_leap(year):
    leap = False

    if (year%4==0) and (year%100!=0 or year%400==0):
        leap = True

    return leap

year = int(input())
print(is_leap(year))