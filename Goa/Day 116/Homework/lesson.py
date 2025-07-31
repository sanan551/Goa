# 1

try:
    num = 10 / 0
except ZeroDivisionError:
    print("ნულზე გაყოფა არ შეიძლება")


# 2

my_list = [5, 10, 15]
try:
    print(my_list[5])
except IndexError:
    print("ინდექსი არასწორია")


# 3 
try:
    user_input = int(input("შეიყვანეთ რიცხვი: "))
except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი")

# 4

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("ნულზე გაყოფა არ შეიძლება")
    else:
        print("გაყოფა წარმატებით შესრულდა")
        return result

print(divide(10, 2))
print(divide(10, 0))



# 5

def check_negative(num):
    if num < 0:
        raise ValueError("რიცხვი არ შეიძლება იყოს უარყოფითი")
    else:
        print(f"რიცხვი {num} არის სწორი")
        
try:
    check_negative(-5)
except ValueError as e:
    print(e)


#6

try:
    num = int(input("შეიყვანეთ რიცხვი: ")) 
    print(f"შესახვედრი რიცხვი: {num}")
except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი")  
finally:
    print("ამინდის შეყვანა დასრულდა") 


# 7 

while True:
    try:
        num = int(input("შეიყვანეთ რიცხვი: "))
        break
    except ValueError:
        print("არასწორი შეყვანა, შეიყვანეთ მხოლოდ რიცხვი")

# 8

numbers = ["10", "20", "hello", "30"]
for num in numbers:
    try:
        print(float(num))
    except ValueError:
        print(f"მონაცემი არ არის რიცხვი: {num}")

# 9 

values = ['10', '20', 'hello', '30']
for value in values:
    try:
        print(int(value))
    except ValueError:
        print(f"მონაცემი არ არის რიცხვი: {value}")
