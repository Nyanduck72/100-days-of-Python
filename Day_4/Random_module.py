# THE RANDOM MODULE
import random
# Some functions of the language are not available from the start and are "imported" into the file.
random_integer = random.randint(1, 10)  # Generates a random whole number between the two parameters
print(random_integer)

random_float = random.random()  # Generates a random decimal number between 0.000... and 0.999..., but never 1
print(random_float)

random_float2 = random.random() * 5  # The float can be multiplied to reach a higher range
print(random_float2)

# This can also be done with other python files to pull variables and other values

