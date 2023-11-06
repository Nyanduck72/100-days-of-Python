# Write a program that calculates the highest score from a list of scores
scores = input("Write the scores of the tests separated by a single space\n").split()
high_score = 0
for n in range(0, len(scores)):
    score = int(scores[n])
    if score > high_score:
        high_score = score
print(f"The highest score of the class is: {high_score}")

