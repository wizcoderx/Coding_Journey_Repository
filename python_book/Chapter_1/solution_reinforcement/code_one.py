''' The question is R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.'''

def multiplication(n,m ):
      """
  Checks if n is a multiple of m.

  Args:
      n: An integer value.
      m: An integer value.

  Returns:
      True if n is a multiple of m, False otherwise.
  """
      if n % m == 0:
            return True
      else:
            return False

print(multiplication(10, 2))  # True
print(multiplication(12, 3))  # True
print(multiplication(15, 4))  # False