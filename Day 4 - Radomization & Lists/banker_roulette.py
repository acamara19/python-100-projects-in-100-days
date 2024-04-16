"""
BANKER ROULETTE:
----------------
Write a program that will select a random name from a list
of names. The person selected will have to pay for everybody's
food bill.

Important! You're not allowed to use choice() function

Line 1 splits the name_string into individual names and put them
inside a list called [names]. For this to work you must enter all
the names as names followed by comma and space. e.g. name, name, name

Note! don't worry about getting hold of the input(), we've done the work
behind the scene to import everything.

Hint! Assume the names look like this: input: x, y, z names = ["x", "y", "z"]
"""
import random

names = input("Please enter the names: ").split(", ")

length_of_names = random.randrange(len(names))

random_name = names[length_of_names]

print(f"{random_name} is going to buy the meal today!")
