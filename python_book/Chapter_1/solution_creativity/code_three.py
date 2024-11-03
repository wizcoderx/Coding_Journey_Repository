'''
Demonstrate how to use Python's list comprehension syntax to produce the list ['a', 'b', 'c', ..., 'z'], but without having to type all 26 such characters literally.
'''
# Define a string of all lowercase English letters
all_letters = 'abcdefghijklmnopqrstuvwxyz'
# Use list comprehension to create a list of individual letters
letter_list = [letter for letter in all_letters]
# Print the resulting list
print(letter_list)