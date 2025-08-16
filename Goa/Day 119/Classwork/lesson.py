
def s(num):
    return num ** 2

result = s(5)
print(result)  



lambda1 = lambda num: num ** 2

resultlambda = lambda1(5)
print(resultlambda)  




def greet(name):
    return f"Hello {name}"

result_greet = greet("Sanan")
print(result_greet)  



greet_lambda = lambda name: f"Hello {name}"

result_greet_lambda = greet_lambda("Sanan")
print(result_greet_lambda)  


# Lambda ფუნქცია:
# მოკლე ფუნქცია, რომელიც არ საჭიროებს სახელის მინიჭებას.
# გამოიყენება ძირითადად ერთჯერადი ოპერაციებისათვის.