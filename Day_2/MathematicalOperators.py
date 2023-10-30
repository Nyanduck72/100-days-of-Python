# Basic math operators
addition = 3+1  # Add
subtraction = 3-1  # Subtract
multiplication = 3*1  # Multiplication
division = 3/1  # Division (This ALWAYS returns a float)
power = 3**2  # Exponential operations

# Hierarchy of operations
# It works in the same order of PEMDAS (Parenthesis, Exponents, Multiplication and Division, Addition and Subtraction)
print(3+2**2/4*(2-1))  # in order, 3 + (4/(4*1)) = 4

# Number manipulation and F-Strings
round(12/5)  # This rounds up or down de decimals in a float to fit an integer
round(1.2345678, 2)  # It can also be used to reduce the number of decimals if given a parameter

floor = 8 // 3  # The // operator can be used to truncate a division and CONVERTING a float into an integer


# There are operators that add work with a variable directly
example = 10
example += 1  # Instead of example = example + 1, it just adds 1 to the existing value
example -= 1  # Instead of example = example - 1, it just subtracts 1 to the existing value
example *= 2  # Instead of example = example * 2, it just multiplies it´s value by 2
example /= 2  # Instead of example = example / 2, it just divides it´s value by 2

# F-Strings
# Suppose that you have to print out a bunch of different variables that have different data types
d1 = 12
d2 = "Hi"
d3 = 1.23
d4 = False
# An F-String allows the conversion to a string type without casting each variable
print(f"{d1}{d2}{d3}{d4}")  # It´s called an f-string because it has an "f" before it



