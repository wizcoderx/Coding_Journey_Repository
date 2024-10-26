'''The question is Write a short Python function, minmax(data), that takes a sequence of one or more numbers and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.'''

def minmax(data):
    if not data:
        raise ValueError("The data is in not the sequence")

    small = large = data[0]

    for i in data[1:]:
        if i < small:
            small = i
        elif i > large:
            large = i

    return(small,large)


data = [3, 4, 5, 9, 2, 6, 5, 3, 5]
result = minmax(data)
print(result)  # Output: (1, 9)

