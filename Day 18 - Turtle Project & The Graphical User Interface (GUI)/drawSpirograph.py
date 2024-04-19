import random
import turtle as t
from turtle import Screen


tim = t.Turtle()
t.colormode(255)
tim.pensize(2)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)
    tim.hideturtle()


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
