#Write a Python function to remove all duplicates from a list of strings.

def remove_duplicates(lst):
    return list(set(lst))

# Test the function
print(remove_duplicates(["hello", "world", "hello", "world"]))  # Output: ['world', 'hello']
