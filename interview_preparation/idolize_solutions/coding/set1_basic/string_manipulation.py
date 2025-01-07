#Given a string, write a Python function to count the number of vowels in it.

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

print(count_vowels('hello')) # 2