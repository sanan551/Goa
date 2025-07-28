numbers = set()
numbers.add(5)
numbers.add(10)
numbers.remove(5)
numbers.remove(10)

even_numbers = {2, 4, 6, 8, 10}
union_set = numbers.union(even_numbers)
intersection_set = numbers.intersection(even_numbers)
difference_set = numbers.difference(even_numbers)

def modify_set(input_set):
    input_set.add(1)
    input_set.add(2)
    input_set.add(3)
    input_set.remove(1)
    return input_set

student = {'name': 'John', 'hobby': 'reading', 'height': 180, 'weight': 75}
name = student.get('name')
height = student.pop('height')

def modify_dict(input_dict):
    input_dict.update({'age': 14})
    input_dict.popitem()
    return input_dict

student_keys = student.keys()
student_values = student.values()

person = {'name': 'Alice', 'age': 30}
for key, value in person.items():
    print(key, value)

animal = {'type': 'cat', 'color': 'black'}
animal_copy = animal.copy()
animal.clear()
print(animal)
print(animal_copy)

animal.update({'age': 3})
animal.popitem()

numbers = [1, 4, 7, 10, 13, 16, 19]
new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num * 2)

new_list_comprehension = [num * 2 for num in numbers if num % 2 != 0]

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)

long_words_comprehension = [word for word in words if len(word) > 5]

nums = list(range(1, 21))
squares = []
for num in nums:
    squares.append(num ** 2)

squares_comprehension = [num ** 2 for num in nums]

mixed = [2, 5, 8, 11, 14, 17, 20]
evens = [num for num in mixed if num % 2 == 0]
odds = [num for num in mixed if num % 2 != 0]

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = [animal[0] for animal in animals]
e_animals = [animal for animal in animals if animal[0] == 'e']
