# import streamlit as st

# def convert_length(value, from_unit, to_unit):
#     conversion_factors = {
#         "meters": 1,
#         "kilometers": 0.001,
#         "miles": 0.000621371,
#         "inches": 39.3701,
#         "feet": 3.28084,
#         "centimeters": 100,
#         "millimeters": 1000,
#         "yards": 1.09361,
#         "nautical miles": 0.000539957,
#         "micrometers": 1e6,
#         "nanometers": 1e9,
#     }
    
#     if from_unit not in conversion_factors or to_unit not in conversion_factors:
#         return "Invalid unit"
    
#     value_in_meters = value / conversion_factors[from_unit]
#     converted_value = value_in_meters * conversion_factors[to_unit]
    
#     return converted_value

# def convert_weight(value, from_unit, to_unit):
#     conversion_factors = {
#         "grams": 1,
#         "kilograms": 0.001,
#         "pounds": 0.00220462,
#         "ounces": 0.035274,
#         "milligrams": 1000,
#         "micrograms": 1e6,
#         "tons": 1e-6,
#         "stone": 0.000157473
#     }
    
#     if from_unit not in conversion_factors or to_unit not in conversion_factors:
#         return "Invalid unit"
    
#     value_in_grams = value / conversion_factors[from_unit]
#     converted_value = value_in_grams * conversion_factors[to_unit]
    
#     return converted_value

# def convert_temperature(value, from_unit, to_unit):
#     if from_unit == to_unit:
#         return value

#     if from_unit == "Celsius":
#         if to_unit == "Fahrenheit":
#             return (value * 9/5) + 32
#         elif to_unit == "Kelvin":
#             return value + 273.15
    
#     elif from_unit == "Fahrenheit":
#         if to_unit == "Celsius":
#             return (value - 32) * 5/9
#         elif to_unit == "Kelvin":
#             return (value - 32) * 5/9 + 273.15

#     elif from_unit == "Kelvin":
#         if to_unit == "Celsius":
#             return value - 273.15
#         elif to_unit == "Fahrenheit":
#             return (value - 273.15) * 9/5 + 32

#     return "Invalid unit"


# def convert_mass(value, from_unit, to_unit):
#     conversion_factors = {
#         "grams": 1,
#         "kilograms": 0.001,
#         "milligrams": 1000,
#         "micrograms": 1e6,
#         "metric tons": 1e-6,
#         "pounds": 0.00220462,
#         "ounces": 0.035274,
#         "stones": 0.000157473,
#         "carats": 5,  # 1 gram = 5 carats
#         "atomic mass units": 6.022e23  # Approx. 1 gram in AMU
#     }

#     if from_unit not in conversion_factors or to_unit not in conversion_factors:
#         return "Invalid unit"

#     value_in_grams = value / conversion_factors[from_unit]
#     converted_value = value_in_grams * conversion_factors[to_unit]

#     return converted_value

# def convert_time(value, from_unit, to_unit):
#     conversion_factors = {
#         "seconds": 1,
#         "minutes": 1 / 60,
#         "hours": 1 / 3600,
#         "days": 1 / 86400,
#         "weeks": 1 / 604800,
#         "months": 1 / 2.628e6,  # Approximate (30.44 days in a month)
#         "years": 1 / 3.154e7,   # Approximate (365.25 days in a year)
#         "milliseconds": 1000,
#         "microseconds": 1e6,
#         "nanoseconds": 1e9
#     }

#     if from_unit not in conversion_factors or to_unit not in conversion_factors:
#         return "Invalid unit"

#     value_in_seconds = value / conversion_factors[from_unit]
#     converted_value = value_in_seconds * conversion_factors[to_unit]

#     return converted_value

# def convert_area(value, from_unit, to_unit):
#     conversion_factors = {
#         "square meters": 1,
#         "square kilometers": 1e-6,
#         "square centimeters": 1e4,
#         "square millimeters": 1e6,
#         "square miles": 3.861e-7,
#         "square yards": 1.19599,
#         "square feet": 10.7639,
#         "square inches": 1550.0031,
#         "hectares": 1e-4,
#         "acres": 0.000247105
#     }

#     if from_unit not in conversion_factors or to_unit not in conversion_factors:
#         return "Invalid unit"

#     value_in_square_meters = value / conversion_factors[from_unit]
#     converted_value = value_in_square_meters * conversion_factors[to_unit]

#     return converted_value


# def convert_energy(value, from_unit, to_unit):
#     conversion_factors = {
#         "joules": 1,
#         "kilojoules": 0.001,
#         "calories": 0.239006,  # Small calorie (cal)
#         "kilocalories": 0.000239006,  # Large calorie (kcal)
#         "watt-hours": 0.000277778,
#         "kilowatt-hours": 2.7778e-7,
#         "electronvolts": 6.242e18,
#         "BTU": 0.000947817,  # British Thermal Unit
#         "foot-pounds": 0.737562
#     }

#     if from_unit not in conversion_factors or to_unit not in conversion_factors:
#         return "Invalid unit"

#     value_in_joules = value / conversion_factors[from_unit]
#     converted_value = value_in_joules * conversion_factors[to_unit]

#     return converted_value



# # Streamlit UI
# st.title("The Unit Converter")

# categories = {
#     "Length": convert_length,
#     "Weight": convert_weight,
#     "Temperature": convert_temperature,
#     "Time": convert_time,
#     "Area": convert_area,
#     "Energy": convert_energy
# }

# category = st.selectbox("Select Conversion Type", list(categories.keys()))

# # Define units for each category
# units = {
#     "Length": ["meters", "kilometers", "miles", "inches", "feet", "centimeters", "millimeters", "yards", "nautical miles"],
#     "Weight": ["grams", "kilograms", "pounds", "ounces", "milligrams", "micrograms", "tons", "stone"],
#     "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
#     "Time": ["seconds", "minutes", "hours", "days", "weeks", "months", "years", "milliseconds", "microseconds", "nanoseconds"],
#     "Area": ["square meters", "square kilometers", "square centimeters", "square millimeters", "square miles", "square yards", "square feet", "square inches", "hectares", "acres"],
#     "Energy": ["joules", "kilojoules", "calories", "kilocalories", "watt-hours", "kilowatt-hours", "electronvolts", "BTU", "foot-pounds"]
# }

# from_unit = st.selectbox("From Unit", units[category])
# to_unit = st.selectbox("To Unit", units[category])
# value = st.number_input("Enter Value", min_value=0.0, format="%.6f")

# if st.button("Convert"):
#     try:
#         result = categories[category](value, from_unit, to_unit)
#         st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
#     except Exception as e:
#         st.error(f"Conversion Error: {e}")





import re
import streamlit as st
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength and get suggestions.")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    if feedback:
        st.write("### Suggestions to Improve Your Password:")
        for tip in feedback:
            st.write(f"- {tip}")
    
    st.write("### Generate a Strong Password:")
    if st.button("Generate Password"):
        st.code(generate_strong_password(), language="python")
