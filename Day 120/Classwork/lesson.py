# 1)
data = [(2, "c", "hello"), (1, "a", "world"), (3, "b", "hi")]
sorted_data = sorted(data, key=lambda x: x[0])

print(sorted_data)


# 2)

def welcome_guests(name, *guests, **person):
    
    print(f"სპეციალური მისალმება შენთვის, {name}! 🎉")

    
    for guest in guests:
        print(f"გამარჯობა {guest}!")

    print("Person dictionary:", person)



welcome_guests("Senan","Nika", "Lasha",age=14, city="Gardabani")

# 3)


def decorator_function(func):
    def wrapper(*args):
        print("Before function execution")   

        val = func(*args)

        print("After function execution")   
        return val 
    return wrapper  


def greeting(name):
    print(f"Greetings {name}")


decorated_greeting = decorator_function(greeting)


decorated_greeting("Senan")
