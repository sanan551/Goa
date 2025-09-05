
number = int(input("შეიყვანეთ რიცხვი: "))

factorial = 1
counter = 1

while counter <= number:
    factorial *= counter
    counter += 1

print(f"{number}-ის ფაქტორიალი არის: {factorial}")
