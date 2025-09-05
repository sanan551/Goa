class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Not enough balance!")

    def get_balance(self):
        return self._balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.get_balance())


class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtil.add(5, 3))
print(MathUtil.multiply(4, 2))




class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog("Buddy")
cat = Cat("Kitty")

dog.sound()
cat.sound()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def discount(price, percent):
        return price * (1 - percent / 100)

class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def show_products(self):
        for p in self._products:
            print(f"{p.name}: ${p.price}")

p1 = Product("Laptop", Product.discount(1000, 10))
p2 = Product("Mouse", Product.discount(50, 20))

order = Order()
order.add_product(p1)
order.add_product(p2)
order.show_products()

