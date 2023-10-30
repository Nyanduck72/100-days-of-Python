# Using maths and f-strings, write a program that tells you how many weeks you have left
# Assuming you will live until 90 years of age
print("Life in Weeks")
age = int(input("How old are you? "))

years_until_death = 90 - age

weeks_until_death = years_until_death * 52

print(f"You have {years_until_death} years or {weeks_until_death} weeks left... Until you hit 90!")
