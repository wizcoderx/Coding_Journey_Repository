'''
Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type.
'''

class Flower():
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_petals(self, petals):
        self.petals = petals

    def set_price(self, price):
        self.price = price

    #These are the getter method, but this is optional 

    def get_name(self) -> str:
        return self.name

    def get_petals(self) -> int:
        return self.petals

    def get_price(self) -> float:
        return self.price



