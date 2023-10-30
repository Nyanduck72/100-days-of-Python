# Data Types in Python

# Strings
word = "Hello"  # This is a string
print(word[1])  # A string behaves like an array, so each letter can be obtained separately (called "subscripting")

# Integers
number = 123  # This is an integer (or a whole number)
large = 111_222  # The computer reads this as 111222, the underscores only help the developer read it correctly

# Floats
decimal = 123.45  # This is a decimal number. They're called floats because of the "floating" point

# Booleans
boolean = True  # This is a boolean. It can only be true or false

# Some functions don´t work with certain data types, so it's useful to know what type is a variable
print(type(word))  # This returns a String type

# A variable's type can be changed with a function. This is called "Casting"
new_decimal = str(decimal)  # This turns the decimal variable into a string
print(word+new_decimal)  # It can be concatenated with another string without any errors


