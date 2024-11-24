'''
write a simple python code for this hackerrank task: Given N names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each NAME queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for NAME is not found, print Not found instead.





https://www.hackerrank.com/challenges/30-dictionaries-and-maps
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
# create an empty dictionay

phone_book = {}

#take the number of input for the dictionary
n = int(input())

#iterate throughout the dictionary

for _ in range(n):
    entry = input().split() #split the input
    name, phone_number = entry[0],entry[1]
    phone_book[name] = phone_number

while True:
    try:
        query = input() #search query
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break

