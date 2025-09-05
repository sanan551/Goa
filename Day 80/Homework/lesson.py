import random  

def secret_number_game():
    secret_number = random.randint(1, 100) 
    print(" საიდუმლო რიცხვი არჩეულია 1-დან 100-მდე. სცადეთ მისი გამოცნობა!")

    attempts = 0
    guess = None  

    while guess != secret_number:
        guess = input("შეიყვანეთ თქვენი გამოცნობა: ")
        while not guess.isdigit():  
            print(" გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
            guess = input("შეიყვანეთ თქვენი გამოცნობა: ")

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("🔼 საიდუმლო რიცხვი უფრო მაღალია!")
        elif guess > secret_number:
            print("🔽 საიდუმლო რიცხვი უფრო დაბალია!")

    print(f" გილოცავთ! თქვენ გამოიცანით რიცხვი {attempts} მცდელობაში.")


secret_number_game()
