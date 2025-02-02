#https://www.hackerrank.com/challenges/collections-counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if y[size]:
        y[size] -= 1
        total += rate
print(total)