fruits = ["apple", "banana", "apple", "cherry", "banana"]
colors = ["red", "blue", "green", "blue", "yellow"]
numbers = [5, 3, 9, 1, 5, 7]

print(fruits.index("apple")) 
print(colors.index("blue"))  
print(numbers.index(5))       

print(fruits.count("banana"))  
print(colors.count("blue"))    
print(numbers.count(5))        

fruits.sort()
print(fruits)  

colors.sort()
print(colors)  

numbers.sort()
print(numbers) 

sorted_fruits = sorted(fruits)
print(sorted_fruits)  


sorted_colors = sorted(colors)
print(sorted_colors)  

sorted_numbers = sorted(numbers)
print(sorted_numbers) 

print(min(fruits))   
print(min(colors))   
print(min(numbers))  

print(max(fruits))  
print(max(colors))  
print(max(numbers)) 
