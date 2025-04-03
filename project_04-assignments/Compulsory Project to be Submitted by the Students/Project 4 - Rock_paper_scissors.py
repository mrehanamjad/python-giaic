# Project 4: Rock, paper, scissors Python Project

import random
import time

def loader():

    print("\n\n  L O A D I N G . . .\n")

    loading_bar = "===" 

    for addition in ["=====", "=======", "========="]:  
        time.sleep(2)  
        loading_bar += addition  
        print("\r" + loading_bar, end="", flush=True)  

    print("\n\n")  # Final newline

print("Welcome to Rock, Paper, Scissors!")
print("We will play 5 rounds. The player who wins the most rounds will be the winner.")
input("Press enter to continue...")

loader()

your_score = 0
computer_score = 0

for i in range(0,5):
    print(f"Round {i}")
    your_choice = input("Enter your choice - rock(R), paper(P), or scissors(S): ").lower()
    computer_choice = random.choice(['r', 'p','s'])
    print(f'Your choice: {your_choice}')
    print(f"Computer's choice: {computer_choice}")
    if your_choice == computer_choice:
        print("It's a tie!")
    elif (your_choice == 'r' and computer_choice =='s') or (your_choice =='s' and computer_choice == 'p') or (your_choice == 'p' and computer_choice == 'r'):
        print("You win!")
        your_score += 1
    elif (computer_choice == 'r' and your_choice =='s') or (computer_choice =='s' and your_choice == 'p') or (computer_choice == 'p' and your_choice == 'r'):
        print("Computer wins!")
        computer_score += 1
    
    print(f"Your score: {your_score}, Computer's score: {computer_score}")

winner = 'Computer' if computer_score > your_score else 'You'
print(f"Final Score:\n Your Score: {your_score}, Computer: {computer_score}\n So {winner} won!")
