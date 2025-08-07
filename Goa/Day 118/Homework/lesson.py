
# 1) რა არის ფუნქცია და რისთვის ვიყენებთ?
# ფუნქცია პროგრამაში არის კოდის ბლოკი
# რომელსაც თავისი სახელი აქვს და რომელიც შეიძლება მრავალჯერ გამოიძახო
# ფუნქციები ეხმარება კოდს:
# გამარტივებაში
# კოდის სტრუქტურირებაში


# 2) რამდენი ტიპის ფუნქცია არსებობს?
# ჩაშენებული  მაგალითად print(), len()
# მომხმარებლის მიერ შექმნილი  შენ თვითონ ქმნი def-ით.

# 3 პარამეტრები, არგუმენტები და დაბრუნება (return)

# def greet(name):  # name არის პარამეტრი

# greet("Senan")  # "Senan" არის არგუმენტი

def add(x, y):
    return x + y

# 4) რა არის მაღალი იერარქიის ფუნქცია?
# მაღალი იერარქიის ფუნქცია  რომელიც იღებს ფუნქციას არგუმენტად ან აბრუნებს სხვა ფუნქციას.

# მაგალითად

def apply(func, value):
    return func(value)

apply(abs, -5)  # აბრუნებს 5

# 5) წმინდა და არაწმინდა ფუნქციები
# წმინდა ფუნქცია 
# ყოველთვის აბრუნებს ერთსა და იმავე შედეგს იგივე არგუმენტებით.

def square(x):
    return x * x

# არაწმინდა ფუნქცია

# შეიძლება ჰქონდეს გვერდითი ეფექტები მაგ. დაბეჭდოს ეკრანზე, ჩაწეროს ფაილში და ა.შ.
def log_message(msg):
    print(msg)  # გვერდითი ეფექტი


# 6
# manual_index ფუნქცია

def manual_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1  # თუ ვერ იპოვა

# 7
# manual_count ფუნქცია

def manual_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


# 8
# Turtle მოდულით კვადრატის დახატვა
from turtle import *

def draw_square(x, y):
    penup()
    goto(x, y)
    pendown()
    for _ in range(4):
        forward(100)
        right(90)


draw_square(0, 0)
done()
