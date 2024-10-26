'''The question is Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.'''

def sum_all(n):
    total_sum = 0

    for i in range(1,n,2):
        total_sum += i**2

    return total_sum



s = int(input("Enter a positive integer: "))
while s <= 0:
    print("Enter a positive number")
    s = int(input("Enter a positive integer: "))


'''implementing it using the sum function inside the multipline comments below
sum_all = sum(i**2 for i in range(1,s,2))
print(sum_all)
'''

result = sum_all(s)
print(result)





