import random

logo='''
    ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/                                                                                           
'''
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.randint(1, 100)

if level == "easy":
    attempts = 10
else:
    attempts = 5


def guessing_game():
    global attempts

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            return

        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses.")
            return

        if guess < number:
            print("Too low.")
        else:
            print("Too high.")

        print("Guess again.\n")

guessing_game()
