import random
# Guess My Number Game

print("----------------------------------------------------------------")

print("01_guess_my_number")

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

# Write a program to print terms in the Fibonacci sequence up to a maximum value.

print("----------------------------------------------------------------")
print("09_fibonacci")
def fibonacci(max_value):
    a = 0
    b = 1
    while a <= max_value:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
    print()

fibonacci(100)

# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

print("----------------------------------------------------------------")
print("02_print_even_numbers")
for number in range(21):
    if number % 2 == 0:
        print(number, end=" ")
print()

# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

print("----------------------------------------------------------------")
print("03_affirmation_program")
affirmation = "i am capable of doing anything i put my mind to"
while True:
    affirmation_input = input("Please type the following affirmation: {} ".format(affirmation))
    if affirmation_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Sorry, that's not the affirmation. Please try again.")

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

print("----------------------------------------------------------------")
print("04_spaceship_launch")
for i in range(10, 0, -1):
    print(i,end=" ")
print("Liftoff!")

# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

print("----------------------------------------------------------------")
print("05_double_number")
number = int(input("Enter a number to start: "))
while True:
    print(number,end=" ")
    if number >= 100:
        break
    number *= 2
    
    