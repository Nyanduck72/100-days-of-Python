# Write a program that calculates the BMI of a person based on it´s height and weight
# The program will tell the user if it´s underweight, normal, slightly overweight, obese or clinically obese

print("Welcome to the new and improved BMI index calculator!")
weight = int(input("Please write your weight in kilos: "))
height = float(input("Please write your height in meters: "))

bmi = (weight/(height**2))

print(f"Your BMI index is {bmi}")
if bmi < 18.5:
    print("You are underweight")

if bmi >= 18.5:
    if bmi < 25:
        print("You have a normal weight")

if bmi >= 25:
    if bmi < 30:
        print("You are slightly overweight")

if bmi >= 30:
    if bmi < 35:
        print("You are obese")

if bmi >= 35:
    print("You are clinically obese, idk how you´re alive")
