# Write a program that tests the compatibility between two people
# The program will grab both names and search for the letters T,R,U,E and L,O,V,E
# The sum of the first letters and the sum of the second letters will be placed together and show a score
# e.g. Arthur Martha = 60 because 2+3+1 = 6 and there are no matching letters in the second phrase

print("Welcome to the Love Calculator!")
name_1 = input("Please insert a name: ")
name_2 = input("Please insert a second name: ")

combined_names = f"{name_1}{name_2}"
total_1 = 0
total_2 = 0

total_1 += combined_names.count("t")
total_1 += combined_names.count("r")
total_1 += combined_names.count("u")
total_1 += combined_names.count("e")

total_2 += combined_names.count("l")
total_2 += combined_names.count("o")
total_2 += combined_names.count("v")
total_2 += combined_names.count("e")

total = str(total_1) + str(total_2)
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif 40 <= total <= 50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")
