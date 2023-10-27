# The input() function is very similar to the print() function

# These functions can be placed inside of one another to shorten the code
# This line will first throw the message inside the input() function to get the name of the user
# Then, it will show on screen the message "Hello, ", followed by the stored name#
# print("Hello, " + input("What's your name? "))

# Exercise 1 - Character Counter
# Write a program that prints the number of characters in a name
# The len() function is used to measure the length of the string captured, then that number gets printed out to console
# print(len(input("What's your name? ")))

# The value of an input can be saved inside a variable
# name = input("What's your name? ")
# This name can be printed out whenever
# print("Hi, " + name)

# Exercise 2 - Data Swap
# The program takes two inputs, then it swaps the value from the first one to the second one and vice-versa
# By creating a "swap" variable, it stored the first value and then changed the second
# value to the first variable. Finally, the value stored in swap went into the second variable
a = input("First input: ")
b = input("Second input: ")

swap = a
a = b
b = swap

print("\nSwapped values: \nFirst value: " + a + "\nSecond value: " + b)
