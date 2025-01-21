"""
GRADING PROGRAMM
Write a program that converts their scores to grades.

By the end of your program, you should have a new dictionary called
student_grades that should contain student names as keys
and their assessed grades for values.

This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 

"""


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for i in student_scores:
    #I needed to first get a hodl of the score in each variable!!
    score = student_scores[i]

    #Now I get the score, and add it to the new dictionary
    if score >= 91:
        student_grades[i] = 'Outstanding'
    elif score >= 81:
        student_grades[i] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[i] = 'Acceptable'
    else:
        student_grades[i] = 'Fail'

print(student_grades)





