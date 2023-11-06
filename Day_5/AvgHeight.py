# Write a program that calculates the average student height from a list of heights
print("Welcome to the average height calculator!")
student_heights = input("Write the heights of the students in centimeters separated by a single space\n").split(" ")
sum_height = 0
avg_height = 0
count = 0
for i in student_heights:
    count += 1
print(f"Number of students: {count}")

for student in student_heights:
    height = int(student)
    sum_height += height
avg_height = sum_height / count
print(f"Total height: {sum_height}")
print(f"The average height of the class is {avg_height}")
