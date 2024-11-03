'''
Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You need not worry about efficiency at this point.
'''

# Input a list of words separated by whitespace
words = input("Enter a list of words separated by whitespace: ").split()

# Create a dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    else:
        # Otherwise, add the word to the dictionary with a count of 1
        word_count[word] = 1

# Output the word counts
print("Word counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")
