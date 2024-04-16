"""
Instructions:
-------------
Write a virtual coin toss program. It will randomly tell the
user "Heads" or "tails".

Important, the first letter should be capitalized and spelt exactly like in
the example e.g. "Heads", not "heads".
"""
import random

choice = input("'Heads' or 'Tails'? ").title()

random_choice = random.randint(0, 1)

if random_choice == 1:
    print("Heads")
else:
    print("Tails")

