class Pakuri():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}, {self.name}!")

    def attack(self, attack_name):
        print(f"{self.name} used {attack_name}!")

class BankAccount():
    def __init__(self):
        self.balance = 0

    def display(self):
        print(f"Current balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}")
            else:
                print("You don't have enough money :(")
        else:
            print("Invalid amount.")

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
            
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
        
    def __str__(self):
        return f"({self.x}, {self.y})"