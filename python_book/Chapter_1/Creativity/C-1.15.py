'''
Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
'''

def is_distinct(seq):
    print(len(seq))
    print(len(set(seq)))
    return len(seq) == len(set(seq))

sequence = [2, 3, 4, 6, 8, 11]
print(is_distinct(sequence))