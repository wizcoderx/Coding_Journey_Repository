'''
url: https://www.hackerrank.com/challenges/symmetric-difference
'''

m = int(input())
set_a = set(map(int(),input().split))
n = int(input())
set_b = set(map(int(),input().split))
a = (set_a.difference(set_b))
b = (set_a.difference(set_a))
ans = a.union(b)
for i in sorted(ans):
    print(i)
