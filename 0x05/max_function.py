# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
