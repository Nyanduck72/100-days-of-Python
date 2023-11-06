# Write a program that calculates the sum of all even numbers from 1 to X
print("Welcome to the even number calculator")
print("Write a number and the program will add every even number from 1 to X")
target = int(input("Write a number: "))
even_sum = 0
for n in range(1, (target + 1)):
    if n % 2 == 0:
        even_sum += n
print(f"The sum of even numbers to {target} is: {even_sum}")
