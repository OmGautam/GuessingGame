import random
number = random.randint(1,9)
chances = 0

while chances<5:
    guess = input("Enter you guess: ")
    if guess == number:
        print("Congrats you won!")
        break
    elif guess < number:
        print("Guess is too low. Guess a higher number",guess)
    else:
        print("Guess is too high. Guess a lower number", guess)
    
