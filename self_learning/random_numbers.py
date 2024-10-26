import random

randomnum = random.randint(10,30)

print(randomnum)

randomflot = random.random() * randomnum


print(randomflot)


#Exercise

random_side = random.randint(1,2) # Check if it is heads or tails
print(random_side)
if random_side == 1:
    print("Its Head's")
else:
    print("Its Tail's")

