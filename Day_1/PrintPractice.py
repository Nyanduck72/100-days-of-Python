# Day 1 - Coding Challenge #1

print("Hello World!")  # The print function shows on the console whatever is inside the parenthesis

# Exercise 1- Printing the exact same way in console the message included in the class
print('Day 1 - Python Print Function\nThe function is declare like this:\nprint("what to write")')
# The \n indicates a new line

# Exercise 2 - Concatenation
print("Hello" + " Alex")  # Different strings can be shown together by putting a + sign in between them

# Exercise 3 - Debugging
# Given a series of print functions, fix the syntax errors in them to show the message on screen
# -- UNFIXED CODE --
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")#

# -- FIXED CODE --
print("Day 1 - String Manipulation")  # The string didn't start with a double quote
print("String Concatenation is done with the '+' sign.")
# The + sign had to be inside single quotes (or the whole string in single quotes and the + sign in double quotes)
print('e.g. print("Hello " + "world")')  # There had to be no indentation on this line
print("New lines can be created with a backslash and n.")  # There was an extra parenthesis on the beginning of the line
