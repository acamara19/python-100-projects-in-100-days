"""
Instructions:
-------------

Write a program that interprets the Body Mass Index (BMI) based on a user's
weight and height.

It should tell them the interpretation of their BMI based on the BMI values:
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- above 35 they are clinically obese
"""

# Get user's height
height = float(input("Enter your height in meters (e.g., 1.55): "))
# Get user's weight
weight = int(input("Enter your weight in kilograms (e.g., 72): "))

bmi = weight / height ** 2
print(int(bmi))

if bmi < 18.5:
    print(f"For a BMI of {bmi}, you're underweight")
elif bmi >= 18.5 or bmi <= 25:
    print(f"For a BMI of {bmi}, you have a normal body weight!")
elif bmi > 25 or bmi <= 30:
    print(f"For a BMI of {bmi}, you're slightly overweight")
elif bmi > 30 or bmi <= 35:
    print(f"For a BMI of {bmi}, you're obese")
else:
    print(f"For a BMI of {bmi}, you're clinically obese")
