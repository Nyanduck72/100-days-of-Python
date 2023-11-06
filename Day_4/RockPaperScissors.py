# Write a program that plays rock paper scissors with the user
import random
# index 0 = rock, 1 = paper, 2 = scissors
options = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
           ]
print("Welcome to solo rock, paper, scissors!")
i = int(input("What do you choose?\n1.- Rock\n2.- Paper\n3.- Scissors\n"))
player_choice = i - 1
computer_choice = random.randint(0, 2)
# Tie
if player_choice == computer_choice:
    print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nIt´s a tie!")
else:
    # Rock vs Paper
    if player_choice == 0 and computer_choice == 1:
        print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nComputer wins!")
    # Rock vs Scissors
    if player_choice == 0 and computer_choice == 2:
        print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nYou win!")
    # Paper vs Rock
    if player_choice == 1 and computer_choice == 0:
        print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nYou win!")
    # Paper vs Scissors
    if player_choice == 1 and computer_choice == 2:
        print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nComputer wins!")
    # Scissors vs Rock
    if player_choice == 2 and computer_choice == 0:
        print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nComputer wins!")
    # Scissors vs Paper
    if player_choice == 2 and computer_choice == 1:
        print(f"You played: {options[player_choice]}\nComputer played: {options[computer_choice]}\nYou win!")
