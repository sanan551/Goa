class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.name} {self.surname} and I am {self.age} years old.")

    def __str__(self):
        return f"Human(name='{self.name}', surname='{self.surname}', age={self.age})"