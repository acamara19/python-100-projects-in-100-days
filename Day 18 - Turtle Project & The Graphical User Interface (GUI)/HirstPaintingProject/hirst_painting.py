"""
Hirst Painting Generator

This script uses the turtle module to create a dot painting in the style of
Damien Hirst. The painting is composed of a grid of colored dots.

Attributes:
    number_of_dots (int): Number of dots in length (default 10 x 10).
    Dot Size (int): Diameter of each dot (default 20).
    Space Between Dots (int): Distance between centers of adjacent dots (default 50).
"""

import turtle as t
from turtle import Screen
from colors import random_color  # Importing random_color from colors.py


def setup_turtle():
    """Sets up the turtle environment."""
    tim = t.Turtle()
    t.colormode(255)
    tim.penup()
    tim.hideturtle()
    tim.speed("fastest")
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    return tim


def paint_hirst_painting(tim):
    """Paints a grid of colored dots using the turtle module."""
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random_color())
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


def main():
    tim = setup_turtle()
    paint_hirst_painting(tim)
    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
