from turtle import Turtle, Screen


def draw_shape(turtle, sides, length, color):
    """
    Draw a regular polygon with the given number of sides, length, and color.

    Args:
    turtle (Turtle): the turtle object to draw with.
    Sides (int): number of sides of the polygon.
    Length (int): the length of each side.
    Color (str): the color of the polygon.
    """
    angle = 360 / sides
    turtle.color(color)
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)


def main():
    screen = Screen()
    tim = Turtle()

    # Define shapes to draw: (sides, length, color)
    shapes = [
        (3, 100, 'magenta'),  # Triangle
        (4, 100, 'crimson'),  # Square
        (5, 100, 'chartreuse'),  # Pentagon
        (6, 100, 'goldenrod'),  # Hexagon
        (7, 100, 'coral'),  # Heptagon
        (8, 100, 'aqua'),  # Octagon
        (9, 100, 'lime'),  # Nonagon
        (10, 100, 'turquoise')
    ]

    for sides, length, color in shapes:
        draw_shape(tim, sides, length, color)

    screen.exitonclick()


if __name__ == "__main__":
    main()
