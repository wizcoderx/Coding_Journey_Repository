#Write a Python function to reverse a string without using any built-in functions.

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

# Test the function
print(reverse_string("hello"))  # Output: "olleh"

