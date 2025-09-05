# 1

def sum_numbers(args):
    total = 0
    for num in args:
        total += num
    return total


# 2
def join_strings(args):
    result = ""
    for text in args:
        result += text
    return result

# 3
def print_person_info(**kwargs):
    print(f"სახელი: {kwargs['სახელი']}, ასაკი: {kwargs['ასაკი']}")


print_person_info(სახელი="გიორგი", ასაკი=25)

# 4
def print_car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_car_info(მოდელი="BMW", წელი=2020, ფერი="შავი")


# 5

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("ფუნქცია დაიწყო")  
        result = func(*args, **kwargs)  
        print("ფუნქცია დასრულდა")   
        return result
    return wrapper



def say_hello(name):
    print(f"გამარჯობა {name}!")

decorated_say_hello = my_decorator(say_hello)
decorated_say_hello("Senan")


# 6
 
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print("ფუნქცია დაიწყო")
        result = func(*args, **kwargs)
        print("ფუნქცია დასრულდა")
        return result
    return wrapper


# 7) 
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


# 8) 
def min_max(*args):
    min_num = args[0]
    max_num = args[0]
    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num


print(multiply(2, 3, 4))      
print(min_max(4, 9, 1, 7))    


# 9) 
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper


def test():
    print("გაშვებული ფუნქცია!")


decorated_test = timer_decorator(test)
decorated_test()



def hello(name):
    return "hello " + name

decorated_hello = uppercase_decorator(hello)
print(decorated_hello("senan")) 

