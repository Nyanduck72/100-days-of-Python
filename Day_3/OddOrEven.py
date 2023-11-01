# Write a program that works out whether a number is even or odd
print("Odd Or Even?")
num = int(input("Write a number: "))

res = num % 2

if res != 0:
    print("The number is odd")
else:
    print("The number is even")
