def square_numbers(numbers):
    squared_numbers = []  
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers  
numbers = [5, 12, 5, 2, 6]
result = square_numbers(numbers)
print(result)  
