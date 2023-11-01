# Build an automatic pizza order program!
# The program will ask the user for the size (Small ($15), Medium ($20) or Large ($25))
# The program will ask to add pepperoni (+$2 on small pizza, +$3 on medium and large pizzas)
# The program will ask to add extra cheese (+$1 on any pizza)

print("Thanks for choosing our pizza place!")
size = input("What size do you want?\nSmall (S) | Medium (M) | Large (L)\n")
pepperoni = input("Do you wish to add pepperoni to your pizza?\nYes (Y) | No (N)\n")
extra_cheese = input("Do you wish to add extra cheese to your pizza?\nYes (Y) | No (N)\n")

price = 0
if size.lower() == "s":
    print("Small Pizza: $15")
    price += 15
elif size.lower() == "m":
    print("Medium Pizza: $20")
    price += 20
elif size.lower() == "l":
    print("Large Pizza: $25")
    price += 25

if pepperoni.lower() == "y":
    if size.lower() == "s":
        print("Pepperoni on Small Pizza: $2")
        price += 2
    else:
        print("Pepperoni on Medium/Large Pizza: $3")
        price += 3

if extra_cheese.lower() == "y":
    print("Extra Cheese: $1")
    price +=1

print(f"Your total will be ${price}")