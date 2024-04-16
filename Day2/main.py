"""
Tip Calculator Project:
-----------------------
"""

print("Welcome to the tip calculator")
print("-----------------------------------")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

calculated_tip = (total_bill * (tip_percentage / 100))

bill_per_person = (total_bill + round(calculated_tip, 2)) / number_of_people
final_amount = "{:.2f}".format(bill_per_person)

print("-----------------------------------")
print(f"Each person should pay: ${final_amount}")
