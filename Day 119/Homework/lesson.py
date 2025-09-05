# 2)
def check_age(age):
    if age < 0:
        raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")
    return f"ასაკი სწორია: {age}"

# 3)
def check_word(word):
    if word == "":
        raise ValueError("სიტყვა არ უნდა იყოს ცარიელი")
    return f"სიტყვა სწორია: {word}"

# 4) 
sum_two = lambda a, b: a + b
print(sum_two(5, 7))  

# 5) 

c_to_f = lambda c: (c * 9/5) + 32
celsius_list = [0, 20, 30, 100]
for c in celsius_list:
    print(f"{c}°C = {c_to_f(c)}°F")

# 6) 
nums = [3, 6, 9, 12, 15]
nums_plus_5 = list(map(lambda x: x + 5, nums))
print(nums_plus_5)  

# 7)
words = ['hello', 'world', 'python']
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)  

# 8) 
nums = [5, 8, 11, 14, 17]
greater_than_10 = list(filter(lambda x: x > 10, nums))
print(greater_than_10) 

# 9)
words = ['ant', 'elephant', 'dog', 'giraffe']
long_words = list(filter(lambda w: len(w) >= 5, words))
print(long_words)  

# 10) 
nums = [2, 4, 6, 8]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  


nums = [1, 2, 3, 4, 5, 6]
even_plus_10 = list(map(lambda x: x + 10, filter(lambda x: x % 2 == 0, nums)))
print(even_plus_10)  
