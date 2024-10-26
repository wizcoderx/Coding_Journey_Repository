# Accept the keys and values inside the dictionary from the user

store = {}

# Take input from the user

number = int(input("Enter the number of input values you want to keep in the dictionary: "))

while key in  store:
    key = input("Enter a unique key for your value: ")
    if key not in store.keys():
        for i in range(number):
            key = int(input("Enter the Key: "))

            value = int(input("Enter the Value: "))

            store[key] = value

print(store)




