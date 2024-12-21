'''
Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
'''

def has_odd_product(seq):

    #Extract all the odd number from the sequence
    odd_numbers = [num for num in seq if num % 2 != 0]

    #Check the len of the pair of odd numbers, if greater than or equal to 2

    return len(odd_numbers) >= 2

sequence = [2, 3, 4, 6,8,11]
print(has_odd_product(sequence))