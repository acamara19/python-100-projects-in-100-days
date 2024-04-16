"""
Instructions:
------------
Create a program using maths and "f-strings" that tells us how many
weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our
 time left in this format: 'You have x weeks left.'

 Where (x) is replaced with the actual calculated number of weeks the input
 age has left until age 90.

 Warning! Your output should match the example output format exactly,
 even the positions of the commas and full stops.

 Notes:
-------
1yr = 52 weeks
"""

age = input("Your age: ")
print("----------------")

max_week = 90 * 52
print(f"90 years = {max_week} weeks")

age_in_weeks = int(age) * 52
print(f"{age} years = {age_in_weeks} weeks")

total_weeks_left = max_week - age_in_weeks
print("---------------------------")
print(f"You have {total_weeks_left} weeks left.")
