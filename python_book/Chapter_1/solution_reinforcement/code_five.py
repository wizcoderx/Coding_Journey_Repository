'''The question is Give a single command that computes the sum from Exercise 4, relying on Python’s comprehension syntax and the built-in sum function.'''


s = int(input("Enter a positive integer: "))
while s <= 0:
    print("Enter a positive number")
    s = int(input("Enter a positive integer: "))

result = sum(i**2 for i in range(1,s))
print(result)   