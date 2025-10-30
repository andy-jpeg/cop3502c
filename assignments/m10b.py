from base_classes import *

class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self.password = password

    def get_balance(self, password):
        if self.password == password:
            return super().get_balance()
        else:
            print("Incorrect password")

    def deposit(self, amount, password):
        if self.password == password:
            super().deposit(amount)
        else:
            print("Incorrect password")

    def withdraw(self, amount, password):
        if self.password == password:
            super().withdraw(amount)
        else:
            print("Incorrect password")

class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.memory = 0

    def add(self, x, y):
        if x == "RESULT":
            x = self.memory
        if y == "RESULT":
            y = self.memory
        self.memory = super().add(x, y)
        return self.memory
    
    def sub(self, x, y):
        if x == "RESULT":
            x = self.memory
        if y == "RESULT":
            y = self.memory
        self.memory = super().sub(x, y)
        return self.memory

class ImprovedFraction(Fraction):
    def add(self, other):
        if type(other) == int:
            return super().add(ImprovedFraction(other, 1))
        return super().add(other)
    
    def multiply(self, other):
        if type(other) == int:
            return super().multiply(ImprovedFraction(other, 1))
        return super().multiply(other)
    
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"