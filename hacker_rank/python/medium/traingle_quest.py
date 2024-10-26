"""
You are given a positive integer n. Your task is to print a numerical triangle of height n.
The triangle should look like this:

1
22
333
4444
55555
...

Each row i contains the integer i repeated i times.

Constraints:
- Use only arithmetic operations, a single for loop, and a single print statement.
- Do not use strings or string manipulations.
- The solution should be no more than two lines of code.

Input:
- A single integer n representing the height of the triangle.

Output:
- A numerical triangle with n rows, where the i-th row contains the integer i repeated i times.

Problem URL: https://www.hackerrank.com/challenges/python-quest-1
"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print( int((i*(pow(10, i) - 1)) / 9 ))

# the alternate code is below:

# n = int(input())
# for i in range(1, n):
#     result = int((i * (pow(10, i) - 1)) / 9)
#     print(result)

