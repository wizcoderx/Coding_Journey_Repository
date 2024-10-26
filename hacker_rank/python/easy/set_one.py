'''

url = https://www.hackerrank.com/challenges/py-introduction-to-sets

'''

def average(array):
   my_set = set(arr)
   avg = sum(my_set)/len(my_set)

   return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)