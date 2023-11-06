# Write a program that will select a random person from a list of names to pay for the whole meal
import random

print("Welcome to the Food Roulette!")
names_string = input("Please write everyone´s name separated by a comma and a single space after it\n")
names = names_string.split(", ")

bill_payer = random.randint(0, len(names) - 1)
print(f"The Bill Payer is {names[bill_payer]}!")
