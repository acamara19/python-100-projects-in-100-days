"""
Instructions:
-------------
Write a program that estest the compatibility between two
people.
To work out the love score between two people:
    1. Take both people's names and check for the number of times the letters
       in the word 'TRUE' occurs.
    2. Then check for the number of times the letters in the word 'LOVE' occurs.
    3. Then combine these numbers to make a 2-digit number.
For Love score less than 10 or greater than 90, the message should be:
    "Your score is 'x', you go together like coke and mentos."
For Love scores between 40 and 50, the message should be:
    "Your score is 'y', you are alright together."
Otherwise, the message will just be their score. E.g.:
    "Your score is 'z'."
"""

name1 = input("What is your Fist & Last names? ")
name2 = input("What is their Fist & Last names? ")

combine_names = name1 + name2
print(combine_names)
lowercase_names = combine_names.lower()
print(lowercase_names)
t = lowercase_names.count("t")
print(f"T = {t}")
r = lowercase_names.count("r")
print(f"R = {r}")
u = lowercase_names.count("u")
print(f"U = {u}")
e = lowercase_names.count("e")
print(f"E = {e}")
first_digit = t + r + u + e
print(f"True Score: {first_digit}")

l = lowercase_names.count("l")
print(f"L = {l}")
o = lowercase_names.count("o")
print(f"O = {o}")
v = lowercase_names.count("v")
print(f"V = {v}")
e = lowercase_names.count("e")
print(f"E = {e}")
second_digit = l + o + v + e
print(f"Love Score: {second_digit}")

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
