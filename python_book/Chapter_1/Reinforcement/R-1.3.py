'''
Write a short Python function, `minmax(data)`, that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions `min` or `max` in implementing your solution.
'''

def minmax(data):
    # Initialize the minimum and maximum values with the first element of the data sequence
    min_val = data[0]
    max_val = data[0]

    for i in data[1:]:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i

    return (min_val, max_val)  # Return the minimum and maximum values as a tuple

data = [3, 4, 5, 9, 2, 6, 5, 3, 5]
result = minmax(data)
print(result)  # Output: (1, 9)