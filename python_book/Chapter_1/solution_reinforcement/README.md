## Reinforcement

1. Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False (code_one.py)

2. Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators (code_two.py)

3. Write a short Python function, minmax(data), that takes a sequence of one or more numbers and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution. (code_three.py)

4. Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n. (code_four.py)

5. Give a single command that computes the sum from Exercise 4, relying on Python’s comprehension syntax and the built-in sum function. (code_five.py)

6. Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n. (code_six.py)

7. Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function. (included in code_six.py)

8. Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index -n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element? (code_eight.py)

9. What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80? (code_nine.py)

10. What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8? (code_ten.py)

11. Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].(code_ten.py)

12.  Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that returns a random choice from the given range. Using only the randrange function, implement your own version of the choice function. (code_twelve.py)

13. Write a short Python function that counts the number of vowels in a given character string.

14. Write a short Python function that takes a string 's'  representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string “Let’s try, Mike.”, this function would return “Lets try Mike”.

15. Write a short program that takes as input three integers `a`, `b`, and `c` from the console and determines if they can be used in a correct arithmetic formula (in the given order), such as:

- `a + b = c`
- `a = b - c`
- `a * b = c`

The program should check if any of these conditions hold true.

## Projects

1. Write a Python program that outputs all possible strings formed by using the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once.

2. Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2

3. A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the following sentence one hundred times: "I will never spam my friends again." Your program should number each of the sentences and it should make eight different random-looking typos.

4. Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You need not worry about efficiency at this point, however, as this topic is something that will be addressed later in this book.