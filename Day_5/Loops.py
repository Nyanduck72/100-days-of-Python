# Let´s say we have a bunch of items in a list
fruits = ["Apple", "Orange", "Pear", "Watermelon", "Pineapple", "Strawberry"]
# To print every single one of the elements in different rows, we need to use the print() function
# But this is too slow, uses a lot of code and is not flexible on the length of the list
# Here we can use a loop to make an action (print each fruit on screen) multiple times:
for fruit in fruits:
    print(fruit)

# The range() function
# Sometimes, loops don't always come tied to lists, so to define the times the loop is going to repeat, we use a numerical range
for num in range(1, 11):
    print(num)  # This prints from 1 to 10. The last number isn't counted

for num2 in range(0, 101, 5):
    print(num2)  # The third number adds a step, so this loop counts in fives
