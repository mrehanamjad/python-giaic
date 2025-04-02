# Write a function that takes a list of numbers and returns the sum of those numbers.
print("----------------------------------------------------------------")
print("01_add_many_numbers")
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of all numbers in the list [1,2,3,5,7,99] is ", sum_numbers([1,2,3,5,7,99]))

# Write a program that doubles each element in a list of numbers.

print("----------------------------------------------------------------")
print("02_double_numbers")
def double_numbers(numbers):
    return [x*2 for x in numbers]

print("Doubled numbers in the list [1,2,3,5,7,99] are ", double_numbers([1,2,3,5,7,99]))


# 04_flowing_with_data_structure

print("----------------------------------------------------------------")
print("04_flowing_with_data_structure")
def add_three_copies(data, original_list):
    for _ in range(3):
        original_list.append(data)

original_list = []
add_three_copies("giaic", original_list)
print("Original list after adding three copies of 'giaic': ", original_list)
print("Original list after adding three copies of 'giaic': ", original_list)

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

print("----------------------------------------------------------------")
print("05_get_first_element")
def get_first_element(lst):
    print("Enter the elements of the list one by one (hit Enter after each input):")
    lst = [input(f"{i+1} element: ") for i in range(int(input("Enter the number of elements: ")))]
    print("The first element in the list is: ", lst[0])
    return lst[0]

get_first_element([])


# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

print("----------------------------------------------------------------")
print("06_get_last_element")
def get_last_element(lst):
    print("Enter the elements of the list one by one (hit Enter after each input):")
    lst = [input(f"{i+1} element: ") for i in range(int(input("Enter the number of elements: ")))]
    print("The last element in the list is: ", lst[-1])
    return lst[-1]

get_last_element([])

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

print("----------------------------------------------------------------")
print("07_continuously_adding_values")
def continuously_adding_values():
    values = []
    while True:
        value = input("Enter a value (or press Enter to stop): ")
        if value == "":
            break
        values.append(value)
    print("The entered values are: ", values)
    return values

continuously_adding_values()

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

print("----------------------------------------------------------------")
print("08_shorten")
MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        print("Removing: ", lst.pop())
    return lst
    
iftar_list = ["Date", "Samosa", "Roll", "Pakora", "Fruitchart", "Dahibarhe"]
print("Original list: ", iftar_list)
print("Shortened list: ", shorten(iftar_list))
print("Original list: ", iftar_list)

