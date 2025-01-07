#Write a Python script that reads a list of numbers and prints only the even numbers.

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

print(even_numbers([1, 3, 5, 7, 9,10,2])) # None