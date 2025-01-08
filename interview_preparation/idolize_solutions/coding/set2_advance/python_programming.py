# #Write a Python function to reverse a string without using any built-in functions.

# def reverse_string(s):
#     reversed_str = ""
#     for i in range(len(s) - 1, -1, -1):
#         reversed_str += s[i]
#     return reversed_str

# # Test the function
# print(reverse_string("hello"))  # Output: "olleh"


def reverse_each_word(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test the function
print(reverse_each_word("hello world"))  # Output: "olleh dlrow"