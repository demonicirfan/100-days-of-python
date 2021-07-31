students_scores = input('input a list of students score').split()
for n in range(0, len(students_scores)):
    students_scores[0] = int(students_scores[n])
print(students_scores)
highest_score = 0
for score in students_scores:
    if score > highest_score:
       highest_score = score

print(f'the highest score in the class is: {highest_score}')