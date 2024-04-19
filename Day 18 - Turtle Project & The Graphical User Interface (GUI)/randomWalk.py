import random
from turtle import Turtle, Screen


tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(12)
tim.speed("fastest")

for _ in range(500):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
