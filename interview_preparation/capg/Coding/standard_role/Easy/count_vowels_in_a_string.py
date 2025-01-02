#Write a function that counts the number of vowels (`a`, `e`, `i`, `o`, `u`) in a given string.

def count_vowels(string):
    count = 0
    for char in string:
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("You Gange"))