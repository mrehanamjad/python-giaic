import hashlib
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information
print('----------------------------------------------------------------')
print('04_count_nums')
inps = [int(input('Enter a number: ')) for i in range(1,11)]
unique_nums = {}
for num in inps:
  if(num in unique_nums):
    unique_nums[num] += 1
  else:
    unique_nums[num] = 1

for k,v in unique_nums.items():
  print(f"{k} appears {v} times.")


# In this program we show an example of using dictionaries to keep track of information in a phonebook.

print('----------------------------------------------------------------')
print('05_phonebook')
phonebook = {}

def get_phonebook():
    while True:
        name = input('Enter a name (or press Enter to stop): ')
        if name == '':
            break
        phone_number = input('Enter phone number: ')
        phonebook[name] = phone_number

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def SearchPhoneNum():
    while True:
        name = input("Enter Name to search for phone number (or press Enter to stop):")
        if name == '':
            break
        if name in phonebook:
            print(f"{name}'s phone number is: {phonebook[name]}")
        else:
            print(f"{name} not found in the phonebook.")
    
get_phonebook()
print_phonebook(phonebook)
SearchPhoneNum()

# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.
print('----------------------------------------------------------------')
print('06_pop_up_shop')
fruit_prices = {
   'apple': 200,
   'banana': 80,
   'orange': 150,
   'watermelom': 100,
   'grape': 120,
   'kiwi': 180,
   'mango': 250,
   'pineapple': 150,
  'strawberry': 220,
   }

def calculate_total_cost():
   total_cost = 0
   for fruit in fruit_prices:
       quantity = int(input(f'How many {fruit}s would you like to buy? '))
       total_cost += quantity * fruit_prices[fruit]
   print(f'total cost: {total_cost}')

calculate_total_cost()


# # You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

print('----------------------------------------------------------------')

print('07_powerfull_passwords')

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def login(email, password_to_check, stored_logins):
    if email in stored_logins:
        hashed_input_password = hash_password(password_to_check)
        if hashed_input_password == stored_logins[email]:
            return True
    return False

# Example Usage:
stored_logins_data = {
    "user1@mail.com":"2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",  
    "user2@mail.com":"486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7",
    "user3@mail.com":"15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225", 
}

print(login("user1@mail.com", "hello", stored_logins_data))
print(login("user1@mail.com", "world", stored_logins_data))
print(login("user2@mail.com", "world", stored_logins_data))
print(login("user3@mail.com", "1234", stored_logins_data))
print(login("user3@mail.com", "123456789", stored_logins_data))
print(login("user32@mail.com", "123456789", stored_logins_data))


