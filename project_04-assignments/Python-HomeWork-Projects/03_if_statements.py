# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

print("----------------------------------------------------------------")
print("01_print_even_numbers")
for number in range(21):
    if number % 2 == 0:
        print(number, end=" ")
print()

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
print("----------------------------------------------------------------")

print("02_vote_age_checker")

age = int(input("How old are you? "))

if age >= 16:
    print("You can vote in Peturksbouipo where the voting age is 16.")
else: 
    print("You cannot vote in Peturksbouipo where the voting age is 16.")
if age >= 25:
    print("You can vote in Stanlau where the voting age is 25.")
else:
    print("You cannot vote in Stanlau where the voting age is 25.")
if age >= 48:
    print("You can vote in Mayengua where the voting age is 48.")
else:
    print("You cannot vote in Mayengua where the voting age is 48.")

# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

print("----------------------------------------------------------------")
print("03_leap_year_checker")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

print("----------------------------------------------------------------")
print("04_height_checker")

height = float(input("Enter your height (in centimeters): "))
minimum_height = 50

if height >= minimum_height:
    print("You are taller than the minimum height requirement.")
else:
    print("You are not taller than the minimum height requirement.")

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops.)

print("----------------------------------------------------------------")
print("05_tall_enough_extension")

while True:
    height = input("Enter your height (in centimeters) or nothing to quit: ")
    if height == "":
        break
    height = float(height)
    minimum_height = 50
    if height >= minimum_height:
        print("You are taller than the minimum height requirement.")
    else:
        print("You are not taller than the minimum height requirement.")

# Pront 10 random numbers in the range 1 to 100. Each time you run your program you should get different numbers

print("----------------------------------------------------------------")
print("06_random_numbers")

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100


import random

for _ in range(N_NUMBERS):
    print(random.randint(MIN_VALUE, MAX_VALUE),end=" ")
print()


