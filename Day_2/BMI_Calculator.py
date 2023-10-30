# Write a program that calculates a persons BMI index based on their height and weight
# BMI = weight/height^2
print("Welcome to the BMI index calculator!")
weight = int(input("Please write your weight in kilos: "))
height = float(input("Please write your height in meters: "))

bmi = str(weight/(height**2))

print("Your BMI index is " + bmi)

