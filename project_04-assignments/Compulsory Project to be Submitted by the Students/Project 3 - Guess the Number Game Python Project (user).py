import random

def computer_guessing_game():
    """guessing game where the computer has to guess the correct number."""

    print("Think of a secret number between 1 and 100.")
    print("I will try to guess it. Please tell me if my guess is:")
    print("- 'h' for higher")
    print("- 'l' for lower")
    print("- 'c' for correct")

    low = 1
    high = 100
    attempts = 0

    while True:
        attempts += 1
        computer_guess = random.randint(low, high)
        print(f"\nIs your number {computer_guess}? (h/l/c): ", end="")
        feedback = input().lower()

        if feedback == 'c':
            print(f"Yay! Thw Computer guessed your number {computer_guess} in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = computer_guess - 1
            if low > high:
                print("You are giving inconsistent feedback! Please play honestly.")
                break
        elif feedback == 'l':
            low = computer_guess + 1
            if low > high:
                print("You are giving inconsistent feedback! Please play honestly.")
                break
        else:
            print("Invalid feedback. Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guessing_game()