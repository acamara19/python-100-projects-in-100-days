"""
You are painting a wall. The instructions on the paint can say that one can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

Number of cans = (wall height x wall width) ÷ coverage per can.

E.g., Height = 2, Width = 4, Coverage = 5

Number of cans = (2 \* 4) / 5
               = 1.6,
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

Example Input
3
9
Example Output
You'll need six cans of paint.
Hint
StackOverflow link on how to round up a number:
https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
"""
import math


def paint_calc(height, width, area):
    number_of_can = math.ceil((height * width) / area)
    print(f"You'll need to buy {number_of_can} cans of paint.")


test_h = int(input("Height of the wall (m): "))
test_w = int(input("Width of the wall (m): "))
coverage = 5
paint_calc(height=test_h, width=test_w, area=coverage)
