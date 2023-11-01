# IF STATEMENT
condition = True  # Here we declare a variable that acts as the condition
if condition:  # The "if" condition reads if something is true. If it´s true, it will do something
    print("Yes")
# If the condition is not true, it will skip it
if condition:
    print("Yes")
else:
    print("No")  # The "else" statement works as another condition. If the first condition wasn't true, the program will
    #  do something else

# COMPARISON OPERATORS
a = 0
b = 1  # This is just assigning a value to the variable
if b == a:  # This compares if a numerical variable is equal to another one
    print("Equal")
if a < 0:
    print("Less Than")
if a <= 0:
    print("Less or equal than")
if a > 0:
    print("More than")
if a >= 0:
    print("More or equal than")
if a != 0:
    print("Not equal to")

# NESTED STATEMENTS
condition1 = True
condition2 = False
if condition1:  # A conditional statement can be inside another
    print("True")
    if condition2:
        print("This will not appear")
elif a == 0:  # A condition can be placed if the first one fails with the "elif" statement
    print("This is true")

# LOGICAL OPERATORS
# These can be used to evaluate 2 or more conditions in one statement
if a and b:
    print("A and B are True")  # Both return a True
if a or b:
    print("Either A or B is True")  # Only one returns a True
if not a:
    print("A is False")  # This is used to know if a condition is not True, essentially inverting the result

