'''
The python code has solved the hacker rank questioned mentioned in the URL:  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])