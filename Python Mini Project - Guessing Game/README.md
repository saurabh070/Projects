# Number Guessing Game

Welcome to the Number Guessing Game! This is a simple console-based game where you try to guess a randomly selected number between 1 and 100. The game provides feedback to help you guess the number correctly.

## How to Play

1. The computer picks a random number between 1 and 100.
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

## Running the Game

To run the game, ensure you have Python installed on your machine. Then, execute the script using the following command:

```sh
python number_guessing_game.py
