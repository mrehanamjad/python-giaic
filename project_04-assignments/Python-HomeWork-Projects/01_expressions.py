import random
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

print("----------------------------------------------------------------")
print("01_dicesimulator")
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

die1: int = 10
print("die1 in root starts as: " + str(die1))
roll_dice()
roll_dice()
roll_dice()
print("die1 in root is: " + str(die1))


# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
#E = m * c**2

print("----------------------------------------------------------------")
print("02_energy_converter: e=mc^2")

m: float = float(input("enter mass in kg: ")) 
c: int = 299792458
e: float = m * c**2

print("e = "+ str(m) + " kg")
print("c = "+ str(c) + " m/s")
print("energy = " + str(e) + " Joules")

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

print("----------------------------------------------------------------")
print("03_foot_to_inches")
feet: float = float(input("Enter number of feet: "))
inches: float = feet * 12
print(str(feet) + " feet is equal to " + str(inches) + " inches")

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

print("----------------------------------------------------------------")
print("04_pythagorean_theorem")
side1: float = float(input("Enter the length of the first side: "))
side2: float = float(input("Enter the length of the second side: "))
hypotenuse: float = (side1**2 + side2**2) ** 0.5
print("The length of the hypotenuse is: " + str(hypotenuse))

# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

print("----------------------------------------------------------------")
print("05_divmod_calculator")
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))
result: float = num1 // num2
remainder: float = num1 % num2
print("The result of the division is " + str(result) + " with a remainder pf " + str(remainder))

# Simulate rolling two dice, and prints results of each roll as well as the total.

print("----------------------------------------------------------------")
print("06_dice_roller")
total_sides: int = 6
die_1: int = random.randint(1, total_sides)
die_2: int = random.randint(1, total_sides)
total = die_1+ die_2
print("Dice have "+ str(total_sides) + " sides each.")
print("First Die : " + str(die_1))
print("Second Die : " + str(die_2))
print("total of two die" + str(total))

# Use Python to calculate the number of seconds in a year
print("----------------------------------------------------------------")
print("07_seconds_in_a_year")
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60
total_seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
print("There are " + str(total_seconds_in_year) + " seconds in a year!")

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
print("----------------------------------------------------------------")
print("08_mad_libs")
SENTENCE_START: str = "Code in Governor house is fun. I learned to program and used Python to "
adjective: str = input("Please type an adjective and press enter: ")
noun: str = input("Please type a noun and press enter: ")
verb: str = input("Please type a verb and press enter: ")
mad_lib_sentence: str = SENTENCE_START + adjective + " " + noun + " " + verb + "!"
print(mad_lib_sentence)












