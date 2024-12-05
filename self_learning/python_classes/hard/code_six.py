'''
   Design a `Cart` class that allows users to add and remove multiple `Product` instances, representing products in an online store. The `Product` class should have attributes `name`, `price`, and `stock`. Implement a `checkout` method in the `Cart` class that calculates the total price and deducts quantities from the `Product` stock. If an item’s stock is insufficient, the checkout should give an error message.
'''

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Cart:
    def __init__(self):
        self.products = {}  # Stores product name as key and (Product, quantity) as value

    def add_product(self, name, price=None, stock=None, quantity=1):
        if name in self.products:
            product, current_quantity = self.products[name]
            if product.stock >= quantity:
                self.products[name] = (product, current_quantity + quantity)
                print(f"Added {quantity} more of {name} to the cart. Total quantity: {current_quantity + quantity}")
            else:
                print(f"Only {product.stock} of {name} are available in stock.")
        else:
            if stock is None or price is None:
                print(f"Cannot add {name} without stock and price details.")
                return
            if stock >= quantity:
                product = Product(name, price, stock)
                self.products[name] = (product, quantity)
                print(f"Added {name} to the cart with quantity: {quantity}")
            else:
                print(f"Insufficient stock to add {name}. Only {stock} available.")

    def delete_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Product {name} removed from the cart.")
        else:
            print(f"Product {name} not found in the cart.")

    def remove_product_quantity(self, name, quantity):
        if name in self.products:
            product, current_quantity = self.products[name]
            if current_quantity >= quantity:
                self.products[name] = (product, current_quantity - quantity)
                print(f"Removed {quantity} of {name} from the cart. Remaining quantity: {current_quantity - quantity}")
                if self.products[name][1] == 0:
                    self.delete_product(name)
            else:
                print(f"Cannot remove {quantity} of {name}. Only {current_quantity} in the cart.")
        else:
            print(f"Product {name} not found in the cart.")

    def checkout(self):
        total = 0
        for name, (product, quantity) in self.products.items():
            if product.stock < quantity:
                print(f"Insufficient stock for {name}. Only {product.stock} available.")
                return
            total += product.price * quantity
            product.stock -= quantity
            print(f"Purchased {quantity} of {name} for ${product.price * quantity:.2f}")
        self.products.clear()
        print(f"Total cost: ${total:.2f}")
        print("Checkout successful!")

# Example usage
product1 = Product("Laptop", 1000, 10)
product2 = Product("Mouse", 50, 25)

cart = Cart()

# Adding products
cart.add_product("Laptop", 1000, 10, 2)
cart.add_product("Mouse", 50, 25, 5)

# Remove product quantity
cart.remove_product_quantity("Mouse", 2)

# Check out
cart.checkout()