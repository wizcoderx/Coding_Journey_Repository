'''The question is Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that returns a random choice from the given range. Using only the randrange function, implement your own version of the choice function.'''

import random

def custom_choice(data):
    if not data:
        raise ValueError("The data in sequence cannot be emoty")

    random_value = random.randint(0,(len(data)))

    return data[random_value]



data = [10, 20, 30, 40, 50]
result = custom_choice(data)
print(f"Randomly selected element: {result}")



