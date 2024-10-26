'''

 is a right triangle,  at .
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°

URL for problem is = "https://www.hackerrank.com/challenges/find-angle"

'''

import math

# Function to calculate the angle theta (MBC) in degrees
def find_angle_mbc(ab, bc):
    # Using arctangent to find the angle
    theta = math.degrees(math.atan(ab / bc))
    return round(theta)

# Example input
ab = float(input())  # Length of AB
bc = float(input())  # Length of BC

# Finding the angle MBC
angle_mbc = find_angle_mbc(ab, bc)
print(f"{angle_mbc}\u00B0") #\u00B0 this is used to get the degree logo/symbol
