import random

# Generates a random number between 1 and 100
sys_num = random.randint(1, 100)


# Game Rules
print('''
Welcome to the Number Guessing Game!

Here's how to play:

1. The computer has picked a random number between 1 and 100.
2. Your task is to guess the correct number.
3. If your guess is too low or too high (less than 1 or more than 100), you'll be told "OUT OF BOUNDS."
4. On your first turn:
   - If your guess is within 10 of the number, you'll be told "WARM!"
   - If your guess is more than 10 away, you'll be told "COLD!"
5. On subsequent turns:
   - If your new guess is closer than the previous one, you'll be told "WARMER!"
   - If your new guess is farther, you'll be told "COLDER!"
6. Keep guessing until you get the correct number!
7. Once you guess correctly, you'll be informed, and the game will tell you how many guesses it took.

Now, let the guessing begin! Good luck!
''')

# Variables Initialized
guesses = []
old_guess = None

while True:
    # User's input guess
    user_num = int(input("Guess the number between 1 and 100: "))

    # Checking out of bounds for user input
    if user_num < 1 or user_num > 100:
        print("OUT OF BOUNDS")
        continue

    # Checking if the guess is correct
    if user_num == sys_num:
        guesses.append(user_num)
        print("Congratulations! You've guessed the correct number in", len(guesses), "guesses.")
        break

    # Guess Evaluation
    guesses.append(user_num)
    if old_guess is None:
        # First guess
        if abs(user_num - sys_num) <= 10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        # Subsequent guesses
        if abs(user_num - sys_num) < abs(old_guess - sys_num):
            print("WARMER!")
        else:
            print("COLDER!")

    # Update variables for the next iteration
    old_guess = user_num
