# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum = 0

for height in student_heights:
    sum += height

lenght = 0
for size in student_heights:
    lenght += 1

result = round(sum / lenght)
print(result, end=" ")
