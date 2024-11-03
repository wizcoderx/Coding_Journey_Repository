'''
Write a Python program that outputs all possible strings formed by using the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once.
'''

from itertools import permutations

# Define the characters to use
characters = ['c', 'a', 't', 'd', 'o', 'g']

# Generate all permutations of the characters
all_permutations = permutations(characters)

# Output each permutation as a string
count = 0 #count the number of permutations
for perm in all_permutations:
    count +=1
    print(''.join(perm))

print(count)