import requests
import json
import random

# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.
print('-----------------------------------------------')
print('00_joke-bot')
PROMPT = "What do you want? "
SORRY = "Sorry I only tell jokes"
user_input = input(PROMPT)

if user_input.lower() == "joke" :
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        joke_data = response.json()
        setup = joke_data.get("setup")
        punchline = joke_data.get("punchline")
        if setup and punchline:
            print("Here is a joke for you!")
            print(setup)
            print(punchline)
        else:
            print("Sorry, I couldn't fetch a joke right now.")
    except requests.exceptions.RequestException as e:
        print(f"Sorry, there was an error fetching a joke: {e}")
    except json.JSONDecodeError:
        print("Sorry, I received an invalid joke format.")
else:
    print(SORRY)

# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
# For example if the user enters the number 2 you would then print:
# 4 8 16 32 64 128

print("----------------------------------------------------------------")
print("01_double_until_100")
number: int = int(input("Enter a number: "))
while number < 100:
    print(number * 2,end=" ")
    number *= 2
print()

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

print("----------------------------------------------------------------")
print("02_litoff")
for i in range(10, 0, -1):
    print(i,end=" ")
print("Liftoff! \n")

# Guess My Number Game
print("----------------------------------------------------------------")
print("03_guess_my_number")

print("Welcome to the Guess My Number Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
print("Try to guess it!")
print("You have 7 attempts to guess the number.")
input("Press enter to continue...")
print("Let's begin!")
attempts = 0
while True:
    attempts += 1
    guess = int(input("Guess a number: "))
    if guess == random_number:
        print("Congratulations! You guessed the number correctly.")
        print(f"You guessed in {attempts} attempts")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    if attempts == 7:
        print("You've run out of attempts. The correct number is:", random_number)
        break

# Pront 10 random numbers in the range 1 to 100. Each time you run your program you should get different numbers

print("----------------------------------------------------------------")
print("04_random_numbers")
N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100
for _ in range(N_NUMBERS):
    print(random.randint(MIN_VALUE, MAX_VALUE),end=" ")
print()
