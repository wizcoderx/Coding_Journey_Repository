'''
   Create a class called `Product` with attributes `name`, `price`, and `quantity_in_stock`. Implement methods to add and remove stock. Then create a class `Inventory` that can store multiple products. Implement methods to add a product, remove a product, and get the total value of all products in the inventory.
'''
class Product:
    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    # Method to add stock
    def add_stock(self, quantity):
        self.quantity_in_stock += quantity

    # Method to remove stock
    def remove_stock(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity
        else:
            print("Not enough stock to remove")

    # Method to get the total value of the product
    def get_total_value(self):
        return self.price * self.quantity_in_stock


class Inventory:
    def __init__(self):
        self.products = {}

    # Method to add a product
    def add_product(self, product):
        self.products[product.name] = product

    # Method to remove a product
    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found")

    # Method to get the total value of all products in the inventory
    def get_total_value(self):
        return sum(product.get_total_value() for product in self.products.values())


# Create some products
p1 = Product("Laptop", 1000, 5)
p2 = Product("Phone", 500, 10)

# Create inventory and add products
inventory = Inventory()
inventory.add_product(p1)
inventory.add_product(p2)

# Check total value of inventory
print("Total Inventory Value:", inventory.get_total_value())
