#Explain the difference between a list and a tuple in Python. When would you use each?

'''
List and Tuple are two of the most commonly used data structures in Python.
List:
- List is a collection of items which is ordered and changeable.
- List is defined by using square brackets [].
- List can contain items of different data types.
- List can contain duplicate items.
- List is mutable.
- List can be modified after it is created.
- List is slower than Tuple.
- List is used when you need to store multiple items in a single variable.
Tuple:
- Tuple is a collection of items which is ordered and unchangeable.
- Tuple is defined by using parentheses ().
- Tuple can contain items of different data types.
- Tuple can contain duplicate items.
- Tuple is immutable.
- Tuple cannot be modified after it is created.
- Tuple is faster than List.
- Tuple is used when you need to store multiple items in a single variable but do not want to change it.
- Tuple is used when you want to use the data as a key in a dictionary.

'''

#python code for tuple
t = (1, 2, 3, 4, 5)
print(t)

#python code for list
l = [1, 2, 3, 4, 5]
print(l)
