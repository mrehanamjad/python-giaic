# Project 5: Hangman Python Project

import random

# Word bank
word_list = ["python", "programming", "hangman", "developer", "computer"]
word = random.choice(word_list)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("\nWelcome to Hangman!")
print("Guess the word letter by letter.")
print("You have", attempts, "incorrect attempts before losing.")

while attempts > 0:
    print("\nCurrent word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for index, letter in enumerate(word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
        break
else:
    print("\nYou lost! The word was:", word)