# Write a program that calculates the tip of the waiter at a restaurant
# The program welcomes the user
print("Welcome to the Tip Calculator!")
# Then, it asks the total bill
subtotal = float(input("Subtotal bill: "))
# After that, it asks what percentage tip will be given
tip = int(input("What percentage tip would you like to give?\n10%, 12% or 15%\n"))
# Finally, it asks how many people are splitting the bill
people = int(input("How many people will split the bill? "))
# The program will show how much money each person will pay (only showing up to 2 decimals)
percentage = tip / 100
waiter_tip = subtotal * percentage
total = round((subtotal + waiter_tip), 2)
split = round((total / people), 2)

print(f"\nTotal bill: ${"%.2f" % total}\nEach person pays ${"%.2f" % split}")
