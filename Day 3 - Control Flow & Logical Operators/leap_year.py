"""
Instructions:
-------------

Write a program that works out whether if a given year is a leap year. A
normal year has 365 days, leap years have 366 days, with an extra day in
February.

This is how you work out whether if a particular year is a leap year.
- On every year that is divisible by 4 with no remainder
- Except every year this is evenly divisible by 100 with no remainder
- unless the year is also divisible by 400 with no remainder
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a leap year")
        else:
            print(f"Year {year} is not a leap year")
    else:
        print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
