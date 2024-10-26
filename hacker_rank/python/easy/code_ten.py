'''
The python code has solved the hacker rank questioned mentioned in the URL: https://www.hackerrank.com/challenges/polar-coordinates
'''

import cmath
n = input()
s = complex(n)

print(abs(s),"\n",(cmath.phase(s)))
