'''
   Design a `Cart` class that allows users to add and remove multiple `Product` instances, representing products in an online store. The `Product` class should have attributes `name`, `price`, and `stock`. Implement a `checkout` method in the `Cart` class that calculates the total price and deducts quantities from the `Product` stock. If an item’s stock is insufficient, the checkout should give an error message.
'''
#Product class

class Prodcut:
   def __init__(self, name, price, stock):
      self.name = name
      self.price = price
      self.stock = stock

#Cart class
class Cart:
   def __init__(self):
      self.products = {}

   def checkout(self):
      total_price = 0
      for product in self.products:
         if self.products[product].stock < self.products[product].quantity:
            print(f"Insufficient stock for {product}")
         else:
            self.products[product].stock -= self.products[product].quantity
            total_price += self.products[product].price * self.products[product].quantity
            del self.products[product]
            return total_price
      






