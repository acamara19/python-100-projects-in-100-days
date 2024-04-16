"""
Instructions:
-------------
The modulo is written as a percentage sign (%) in Python. it gives you
the remain after a division
e.g. 6 / 2 = 3 with no remainder.
therefore: 6 % 2 = 0
5 / 2  = 2 x 2 + 1, remainder is 1.
therefore: 5 % 2 = 1
14 / 4 = 3 x 4 + 2, remainder is 2.
therefore: 14 % 4 = 2

Warning! your output should match the Example output format exactly,
even the positions fo the commas and full stops.
"""

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"{number} is an Even number")
else:
    print(f"{number} is an Odd number")
