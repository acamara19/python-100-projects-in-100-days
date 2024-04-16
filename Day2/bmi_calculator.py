"""
Instructions:
-------------

BMI = weight (kg) / height2 (m2)

Note: You should convert the bmi to a whole number and print out a
whole number in order to pass the test
"""

# 1st input: enter heights in meters e.g: 1.65
height = input("Height: ")

# 2nd input: enter weight in kg e.g: 72
weight = input("Weight: ")


bmi = int(weight) / (float(height) ** 2)

print("-----------------")
print(f"bmi = {int(bmi)}")
