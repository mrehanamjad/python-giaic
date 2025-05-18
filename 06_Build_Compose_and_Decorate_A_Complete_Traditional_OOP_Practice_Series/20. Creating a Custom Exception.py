class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    print("Age is valid.")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)

