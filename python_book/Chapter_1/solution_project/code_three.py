'''
A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the following sentence one hundred times: "I will never spam my friends again." Your program should number each of the sentences and it should make eight different random-looking typos.
'''
import random

# Define the original sentence
original_sentence = "I will never spam my friends again."

# List of possible typos
typos = [
    "I will nevr spam my friends again.",
    "I will never spamm my friends again.",
    "I wil never spam my frends again.",
    "I will never spam my freinds again.",
    "I will never spam my frends agian.",
    "I wil never spamm my friends agan.",
    "I will nevver spam my friends again.",
    "I will never spam my friends agian."
]

# Function to create sentences with typos
def generate_sentence(index):
    if random.random() < 0.08:  # 8% chance to make a typo
        return f"{index}. {random.choice(typos)}"
    return f"{index}. {original_sentence}"

# Generate and print the sentences
for i in range(1, 101):
    print(generate_sentence(i))
