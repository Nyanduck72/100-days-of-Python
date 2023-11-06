# A list is a way to store data in groups
list1 = ["Hi", 12, True]  # A list can hold various data types together

# For example, to store in variables the states of the USA, the program would have to declare a lot of variables
# With a list, one variable holds every state
USA = ["California", "Oregon", "Florida", "Texas", "Ohio"]  # And so on...
print(USA)  # The list can be entirely printed out

# Because of the ordered aspect of lists, each piece of data can be accessed separately
# The list´s index starts on 0, so to get a specific entry is n - 1
print(USA[0])  # This prints out California
print(USA[4])  # This prints out Ohio

print(USA[-1])  # This also prints out Ohio. If the index is negative, the count starts from the end of the list

USA.append("Pencilvania")  # Use the "append" function to add items to the end of the list
USA.extend(["Thequota", "Midnessota"])  # Use the "extend" function to add various items to the end

