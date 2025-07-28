# 1. შექმენით სია 0-იდან 21-მდე რიცხვებით
number_list = []
for x in range(0, 21):
    number_list.append(x)
print(number_list)

# 2. აიღეთ სია 1-დან 10-მდე რიცხვების კვადრატებით
squared_numbers = []
for x in range(1, 10):
    squared_numbers.append(x * x)
print(squared_numbers)

# 3. შექმენით სია ლუწ რიცხვებით 20-იდან 40-მდე
even_numbers = []
for x in range(20, 41):
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)

# 4. შექმენით რიცხვების სია და გადატანეთ მხოლოდ კენტ რიცხვები ორზე გაზრდილ სიაში
sample_numbers = [1, 2, 3, 4, 5]
odd_numbers_multiplied = []
for x in sample_numbers:
    if x % 2 != 0:
        odd_numbers_multiplied.append(x * 2)
print(odd_numbers_multiplied)

# 1. იგივე სია 0-იდან 21-მდე
numbers = [x for x in range(22)]
print(numbers)

# 2. კვადრატები 1-დან 10-მდე
number_squares = [x * x for x in range(1, 11)]
print(number_squares)

# 3. ლუწი რიცხვები 20-იდან 40-მდე
even_numbers_20_40 = [x for x in range(20, 41) if x % 2 == 0]
print(even_numbers_20_40)

# 4. კენტ რიცხვები ორზე გაზრდილი
odd_numbers_doubled = [x * 2 for x in range(1, 11) if x % 2 != 0]
print(odd_numbers_doubled)
