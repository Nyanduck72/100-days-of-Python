# Write a program that generates a random password
# The program will ask the user how many letters, numbers and symbols it wants on the password
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "l", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "L",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "+", "*"]

print("Welcome to PyPass!")
l = int(input("How many letters do you want in your password? "))
n = int(input("How many numbers do you want in your password? "))
s = int(input("How many symbols do you want in your password? "))

password = []
for letter in range(1, l + 1):
    password += random.choice(letters)
for number in range(1, n + 1):
    password += random.choice(numbers)
for symbol in range(1, s + 1):
    password += random.choice(symbols)
random.shuffle(password)
print(f"Your new password could be {"".join(password)}")
