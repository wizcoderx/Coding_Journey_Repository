'''
Write a short Python function, `is_even(k)`, that takes an integer value and returns `True` if `k` is even, and `False` otherwise. However, your function cannot use the multiplication, modulo, or division operators.
'''

def is_even(k):

    return k[-1] in ['0','2','4','6','8']

k = input()
result = is_even(k)
print("True") if result else print("False")
