student_heights = input('input list of student heights ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0   
for n in range(0, len(student_heights)):
    height=student_heights[n]
    total_height+=height
total_elements_in_array = 0
for i in range(0, len(student_heights)):
   total_elements_in_array += i
avg = total_height / total_elements_in_array
print(avg)
