def calculator(num1,num2,operator):
        if operator == '+':
            return  num1 + num2
        elif operator == '-':
            return  num1 - num2
        elif operator == '*':
            return  num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "ოპერაცია ვერ შესრუ"
            else:
                 return num1/num2
        else:
            return "შეყვანილი ოპერატორი არასწორია."
        
num1 = int((input("პირველი რიცხვი: ")))
num2 = int((input("მეორე რიცხვი: ")))
operator = (input("ოპერატორი (+, -, *, /): "))

result = calculator(num1,num2,operator)

print(result)