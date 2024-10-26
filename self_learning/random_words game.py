#Create a list of random words
import random as rn

random_list = ["lucky","piss","pandit"]

#choose a random word from the list

choose_word = rn.choice(random_list)

print(choose_word)

# print the number of blank lines as per the choosen word!

for i in range (len(choose_word)):
    dash = "_"
    print(dash)

