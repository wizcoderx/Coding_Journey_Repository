'''
Write a short program that takes as input three integers `a`, `b`, and `c` from the console and determines if they can be used in a correct arithmetic formula (in the given order), such as:

- `a + b = c`
- `a = b - c`
- `a * b = c`

The program should check if any of these conditions hold true.

'''

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

if a + b == c:
    print("The formula a + b = c is correct")
elif a == b -c :
    print("The formula a = b - c is correct")
elif a * b == c:
    print("The formula a * b = c is correct")


