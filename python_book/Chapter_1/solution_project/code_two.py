'''
    Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2
'''

num1 = int(input("Enter a number greater than 2: "))
while num1 <= 2:
    num1 = int(input("Please enter a number greater than 2: "))

count = 0
while num1 >= 2:  # Keep dividing until num1 is less than 2
    num1 = num1 / 2
    count += 1

print(f"The number must be divided by 2 a total of {count} times before getting a value less than 2.")
