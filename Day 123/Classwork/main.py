class Person:
    def __init__(self, name, surname, age, work):
        self.name = name
        self.surname = surname
        self.age = age
        self.work = work

    def working(self):
        print(f"{self.name} working at {self.work}")

class Student(Person):
    def __init__(self, name, surname, age, work, year):
        super().__init__(name, surname, age, work) 
        self.year = year

    def working(self):
        print(f"{self.name} studying")

# მემკვიდრეობა (Inheritance) - Student კლასი იღებს Person-ის თვისებებს და მეთოდებს
# პოლიმორფიზმი (Polymorphism) - method working სხვადასხვა კლასში სხვადასხვა მოქმედებას აკეთებს


person1 = Person("Giorgi", "Kapanadze", 30, "CompanyX")
student1 = Student("Nino", "Burchuladze", 20, "None", 2)

print(person1.name, person1.age)
print(student1.name, student1.year)

person1.working() 
student1.working() 


class PersonWithPrivacy:
    def __init__(self, name, surname, age, work, birth_year, id_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.work = work
        self._birth_year = birth_year  
        self.__id = id_number          

    def get_id(self):
        return self.__id

person2 = PersonWithPrivacy("Levan", "Gogoladze", 28, "CompanyY", 1995, 12345)


print(person2._birth_year)

