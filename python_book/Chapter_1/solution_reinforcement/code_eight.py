'''The question is Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index -n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element? '''

def convert_negative_index(s, k):
    n = len(s)

    if -n<k<0:
        return n + k
    else:
        raise ValueError("Invalid index or out of range")
# Example usage:
s = "hello"
k = -2  # Example negative index
j = convert_negative_index(s, k)
print(f"The positive index equivalent of {k} is {j}, which references the element '{s[j]}'")
