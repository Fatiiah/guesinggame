
import random

print("Welcome to the Guess the Number game!")

limit = int(input("Choose a limit: "))
guess = random.randint(1, limit)

difficulty = int(input(
    "Select difficulty: 1 for easy, 2 for medium, 3 for difficult: "
))

if difficulty == 1:
    no_of_trials = 10
elif difficulty == 2:
    no_of_trials = 5
elif difficulty == 3:
    no_of_trials = 3
else:
    print("Invalid Input!")
    exit()

attempts = 0

while no_of_trials > 0:
    user_input = int(input("Enter your guess: "))
    attempts += 1

    if user_input == guess:
        print(f"Congratulations! You guessed {guess} correctly!")
        print(f"You got it in {attempts} attempt(s)!")
        break

    elif user_input > guess:
        print("Too High!")

    else:
        print("Too Low!")

    no_of_trials -= 1

    if no_of_trials > 0:
        print(f"You have {no_of_trials} trials left.")

if no_of_trials == 0 and user_input != guess:
    print(f"Game Over! The correct number was {guess}.")
    print(f"You used all {attempts} attempts.")
