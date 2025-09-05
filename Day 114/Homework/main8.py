numbers = set()            
numbers.add(1)             
numbers.add(2)             
numbers.add(3)             
numbers.add(4)             
print("numbers set after additions:", numbers)

numbers.remove(1)          
numbers.remove(3)          
print("numbers set after removals:", numbers)


even_numbers = {2, 4, 6, 8}
print("even numbers set:", even_numbers)


all_numbers = numbers.union(even_numbers)  
print("union of numbers and even_numbers:", all_numbers)


common_numbers = numbers.intersection(even_numbers)
print("intersection of numbers and even_numbers:", common_numbers)


diff_numbers = numbers.difference(even_numbers)
print("difference of numbers minus even_numbers:", diff_numbers)
