"""
Instructions:
-------------
You have access to a database of student_scores in the format of a dictionary.
The keys in student_scores are the names of the students and the values are
their exam scores.

Write a program that converts their scores to grades. By the end of the program,
you should have a new dictionary called student_grades that should contain student
names for keys and their grades for values

Note! Do not write any print statements.

Scoring criteria:
    - Scores 91 - 100: Grade = "Outstanding"
    - Scores 81 - 90: Grade = "Exceeds Expectations"
    - Scores 71 - 80: Grade = "Acceptable"
    - Scores 70 - lower: Grade = "Fail"
"""

student_scores = {
    "Hary": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Create an empty dictionary called `student_grades`.
student_grades = {}

for key in student_scores:
    grade = student_scores[key]
    if 91 <= grade <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= grade <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= grade <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


print('\n', student_grades)
