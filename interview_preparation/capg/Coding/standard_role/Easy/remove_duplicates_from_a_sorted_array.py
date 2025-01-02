#Write a function that removes duplicate elements from a sorted array and returns the new length.

def remove_duplicated(string):
    print(len(set(string)))
    return set(string)

print(remove_duplicated([1, 1, 2, 2, 3])) #2