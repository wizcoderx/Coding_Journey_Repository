'''
Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
'''

def are_all_distinct(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return False
        else:
            seen.add(num)

    return True

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 2, 4]

print(are_all_distinct(numbers1))  # Output: True
print(are_all_distinct(numbers2))  # Output: False
