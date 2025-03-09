
import streamlit as st
import random

st.title("🎯 Number Guessing Game")

if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False


with st.sidebar:
    st.header("Settings ⚙️")
    min_range = st.number_input("Minimum Number", value=1)
    max_range = st.number_input("Maximum Number", value=100)
    difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])

    if difficulty == "Easy":
        max_attempts = 10
    elif difficulty == "Medium":
        max_attempts = 7
    else:
        max_attempts = 5

    st.write(f"You have {max_attempts} attempts.")

def reset_game():
    st.session_state.target_number = random.randint(min_range, max_range)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Game logic
st.write(f"**Guess a number between {min_range} and {max_range}.**")
guess = st.number_input("Enter your guess:", min_value=min_range, max_value=max_range)

if st.button("Submit Guess"):
    print(st.session_state)
    if st.session_state.game_over:
        st.warning("The game is over. Please reset the game to play again.")
    else:
        st.session_state.attempts += 1
        if guess < st.session_state.target_number:
            st.error("Too low! 📉")
        elif guess > st.session_state.target_number:
            st.error("Too high! 📈")
        else:
            st.success(f"Congratulations! 🎉 You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

        if st.session_state.attempts >= max_attempts and not st.session_state.game_over:
            st.error(f"Game over! 😢 The number was {st.session_state.target_number}.")
            st.session_state.game_over = True

st.write(f"Attempts: {st.session_state.attempts}")

if st.button("Reset Game"):
    reset_game()