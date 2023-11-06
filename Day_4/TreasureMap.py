# Write a program that will mark a spot on a map with an X
# A list called map will be created. Inside it, three lists called line1, line2 and line3
# The program will ask for a coordinate (e.g. A1)
# It should print a 3x3 grid with an X on the coordinate assigned
list1 = ["[ ]", "[ ]", "[ ]"]
list2 = ["[ ]", "[ ]", "[ ]"]
list3 = ["[ ]", "[ ]", "[ ]"]
treasure_map = [list1, list2, list3]

print("Welcome to the Treasure map Creator!")
print(f"       A      B      C\n1 | {list1}\n2 | {list2}\n3 | {list3}")
pos = input("Write the coordinate where you would like the treasure to be buried (e.g. A1): ")

row = int(pos[1]) - 1
letter = pos[0].lower()
if letter == "a":
    column = 0
elif letter == "b":
    column = 1
elif letter == "c":
    column = 2
else:
    print("That coordinate doesn't exist!  We´ll use the default one")
    row = 0
    column = 0

treasure_map[row][column] = "[X]"
print(f"       A      B      C\n1 | {list1}\n2 | {list2}\n3 | {list3}")
print("Your treasure was hidden!")


