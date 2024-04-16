"""
Instructions:
-------------
Write a program that adds the digits in a 2 digits number. e.g. if the input
was 35, then the output should be: 3 + 5 = 8

Warning. Do not change the code on line 1. Your program should work
for different inputs. e.g. any two-digit-number.

The last line of your program should print the result.
"""
print("Provide a two digit number:")
print("---------------------------")
two_digit_number = input()

sum_of_digit = int(two_digit_number[0]) + int(two_digit_number[1])
print("---------------------------")
print(f"The sum of {two_digit_number[0]} + {two_digit_number[1]} = {sum_of_digit}")
