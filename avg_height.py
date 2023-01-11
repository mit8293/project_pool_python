
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

j=0
k=0
for i in student_heights:
    j=i+j
    k+=1
avg = round(j / k)
print(avg)

