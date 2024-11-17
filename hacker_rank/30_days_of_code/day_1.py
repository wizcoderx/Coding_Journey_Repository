'''
Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

Declare  variables: one of type int, one of type double, and one of type String.
Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
Use the  operator to perform the following operations:
Print the sum of  plus your int variable on a new line.
Print the sum of  plus your double variable to a scale of one decimal place on a new line.
Concatenate  with the string you read as input and print the result on a new line.
Note: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.
'''
#https://www.hackerrank.com/challenges/30-data-types/

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
num1 = int(input())
float1 = float(input())
s2 = str(input())
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
ans_int = i + num1
print(ans_int)
# Print the sum of the double variables on a new line.
ans_double = d + float1
print(ans_double)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
ans_string = s + s2
print(ans_string)