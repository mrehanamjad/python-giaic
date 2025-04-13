import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    win_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < win_number:
                print("Too low! Try again.")
            elif guess > win_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {win_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    number_guessing_game()