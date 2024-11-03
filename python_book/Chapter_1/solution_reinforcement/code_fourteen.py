'''
Write a short Python function that takes a string 's', representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string “Let’s try, Mike.”, this function would return “Lets try Mike”.
'''

def take_string(s):
    # Import the string module to access punctuation
    import string
    # Use the translate method to remove punctuation from the string
    s = s.translate(str.maketrans('', '', string.punctuation))
    return s

print(take_string("hello! this is you mom :)"))

