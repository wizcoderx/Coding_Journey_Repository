'''
The python code has solved the hacker rank questioned mentioned in the URL: https://www.hackerrank.com/challenges/collections-counter/
'''

from collections import Counter

x = int(input())
shoe_sizes = Counter(map(int, input().split()))
N = int(input())
total_earnings = 0

for i in range(N):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        total_earnings += price
        shoe_sizes[size] -= 1

print(total_earnings)