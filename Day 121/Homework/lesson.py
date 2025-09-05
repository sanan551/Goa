# 1)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 2)
class Cat:
    def __init__(self, cat_name):
        self.cat_name = cat_name

    def meow(self):
        print(f"{self.cat_name} says Meow!")

# 3)
class Animal(Human, Cat):
    def __init__(self, name, age, cat_name):
        Human.__init__(self, name, age)
        Cat.__init__(self, cat_name)

    def show_info(self):
        self.greet()
        self.meow()

# 4)
class Batman:
    def fight(self):
        print("Batman is fighting crime!")

    def fly(self):
        print("Batman is flying with his Batwing!")

# 5)
class SuperHero(Animal, Batman):
    def __init__(self, name, age, cat_name):
        super().__init__(name, age, cat_name)  


superhero = SuperHero("Bruce", 35, "Whiskers")
superhero.show_info() 
superhero.fight()     
superhero.fly()       
