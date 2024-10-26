'''The question is Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.'''

def n_square(n):
    total_sum = 0

    for i in range(1,n):
        total_sum += i**2

    return total_sum


s = int(input("Enter a positive integer: "))
while s <= 0:
    print("Enter a positive number")
    s = int(input("Enter a positive integer: "))

result = n_square(s)
print(result)