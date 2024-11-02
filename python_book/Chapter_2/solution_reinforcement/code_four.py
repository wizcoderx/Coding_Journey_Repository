'''
Write a Python function that takes a sequence of numbers and determines if there is a distinct pair of numbers in the sequence whose product is odd.
'''

def has_odd_product(nums):

    odd_count = 0
    for num in nums:
        if num % 2 != 0:
            odd_count += 1
            if odd_count >= 2:
                return True
    return False

numbers = (2, 4, 6, 8, 9)
print(has_odd_product(numbers))



