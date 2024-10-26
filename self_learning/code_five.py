'''
Question 5: Inventory Item
Create an Item class that represents an item in an inventory with:

An __init__ method that takes name, price, and quantity as parameters.
A total_cost method that returns the total cost of the item (price * quantity).
A display_item method that prints the items name and total cost.
'''
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Total cost of the item
    def total_cost(self):
        return self.price * self.quantity

    #display items
    def display_item(self):
        print(f"Item: {self.name} + {self.price}")

item = Item("Laptop", 1000, 3)
print(item.total_cost())      # Output: 3000
item.display_item()           # Output: "Laptop - Total Cost: 3000"
