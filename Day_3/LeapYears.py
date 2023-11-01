# Write a program that tells the user if the given year was/will be a leap year
# It is a leap year when:
# - The number is divisible by 4 with no remainder
# - EXCEPT every year which is divisible by 100 with no remainder
# - UNLESS the year is also divisible by 400 with no remainder#
print("Welcome to the Leap Year Calculator!")
year = int(input("Which year do yo want to verify? "))

if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
        is_leap_year = False
        if year % 400 == 0:
            is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print("It´s a leap year!")
else:
    print("It´s not a leap year...")
