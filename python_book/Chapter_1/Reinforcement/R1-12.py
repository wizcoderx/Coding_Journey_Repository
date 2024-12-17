'''
Python's `random` module includes a function `choice(data)` that returns a random element from a non-empty sequence. The `random` module includes a more basic function `randrange`, with parameterization similar to the built-in `range` function, that return a random choice from the given range. Using only the `randrange` function, implement your own version of the `choice` function.
'''

import random

def choice(data):
    if not data:
        raise ValueError("Data cannot be empty")

    index = random.randrange(len(data))

    return data[index], index

data = [10,20,30,40]
random_element = choice(data)
print(random_element)