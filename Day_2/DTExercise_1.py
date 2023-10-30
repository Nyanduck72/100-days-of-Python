# Write a program that adds the digits in a 2-digit number (e.g. 35 = 3+5 = 8)
num = input("Enter a 2 digit number: ")
add = int(num[0]) + int(num[1])  # The input gets split into two separate numbers
print(num[0] + " + " + num[1] + " = " + str(add))
