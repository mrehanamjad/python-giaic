# 01_add_two_numbers

print("---------------------------------")
print("01_add_two_numbers")
num1:int = int(input("Enter first number"))
num2:int = int(input("Enter second number"))
result: int = num1 + num2
print(f"{num1} + {num2} = {result}")

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
print("---------------------------------")
print("02_favorite_animal")
favorite_animal: str = input("What is your favorite animal?: ")
print(f"My favorite animal is also {favorite_animal}!")

# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
print("---------------------------------")
print("03_fahrenheit_to_celsius")
fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
celsius: float = (fahrenheit - 32) * 5.0/9.9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Problem Statement
# Write a program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

print("---------------------------------")
print("04_age_riddle")
anton: int = 21
beth: int = anton + 6
chen: int = beth + 20
drew: int = chen + anton
ethan: int = chen

print(f"Anton is {anton} years old.")
print(f"Beth is {beth} years old.")
print(f"Chen is {chen} years old.")
print(f"Drew is {drew} years old.")
print(f"Ethan is {ethan} years old.")

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

print("---------------------------------")
print("05_triangle_perimeter")
side1: float = float(input("Enter the length of side 1: "))
side2: float = float(input("Enter the length of side 2: "))
side3: float = float(input("Enter the length of side 3: "))
perimeter: float = side1 + side2 + side3
print(f"The perimeter of the triangle is {perimeter:.2f} units.")

# Ask the user for a number and print its square

print("---------------------------------")
print("06_square_number")
number: int = int(input("Enter a number: "))
square: int = number * number
print(f"The square of {number} is {square}.")