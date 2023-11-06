# Write a program that automatically prints the solution to the FizzBuzz Game
# Say Fizz every multiple of 3
# Say Buzz every multiple of 5
# Say FizzBuzz if they match up
# Every other number must be printed out as normal
print("Fizz-Buzz Game Chart")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


