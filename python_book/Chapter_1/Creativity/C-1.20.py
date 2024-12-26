'''
Python's `random` module includes a function `shuffle(data)` that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The `random` module includes a more basic function `randint(a, b)` that returns a uniformly random integer from `a` to `b` (including both endpoints). Using only the `randint` function, implement your own version of the `shuffle` function.
'''

import random

def custom_shuffle(data):
    n = len(data)
    for i in range(n):
        # Pick a random index j such that i <= j < n
        j = random.randint(i, n - 1)
        # Swap elements at index i and j
        data[i], data[j] = data[j], data[i]

# Example Usage
data = [1, 2, 3, 4]
custom_shuffle(data)
print(data)  # Output: A random permutation, e.g., [3, 1, 4, 2]
