import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character type must be selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the length.")

    print("\nSelect character types to include (yes/no):")
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    print(f"\nGenerated Password: {generated_password}")

    another = input("\nGenerate another password? (yes/no): ").lower()
    if another == 'yes':
        main()
    else:
        print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()