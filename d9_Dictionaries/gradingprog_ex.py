student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}
# Write your code below to add the grades to student_grades.👇
for i in student_scores:
    score = student_scores[i]
    if score >= 91:
        student_grades[i] = 'Outstanding'
    if 81 <= score <= 90:
        student_grades[i] = 'Exceeds Expectations'
    if 71 <= score <= 80:
        student_grades[i] = 'Acceptable'
    if score <= 70:
        student_grades[i] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)
