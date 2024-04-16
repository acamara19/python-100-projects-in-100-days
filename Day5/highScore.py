"""
Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e.

The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
"""
student_scores = input("Please enter the student scores: ").split()  # [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):  # N = 7 elements
    student_scores[n] = int(student_scores[n])

highest_score = 0  # Initialize to 0
for score in student_scores:  # Iterate through each element in the list
    if score > highest_score:  # compare the current score with the highest score
        highest_score = score  # Assign the current score to the highest score variable
print(f"The highest score in the class is: {highest_score}")  # Print the highest score after all iterations
