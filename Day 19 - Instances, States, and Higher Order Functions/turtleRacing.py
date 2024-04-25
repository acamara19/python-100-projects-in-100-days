from turtle import Turtle, Screen
import random


class RacingTurtle(Turtle):
    """A class representing a racing turtle, inheriting from Turtle class."""

    def __init__(self, name, color, start_pos):
        super().__init__(shape="turtle")
        self.penup()
        self.color(color)
        self.name = name
        self.goto(start_pos)

    def race(self):
        """Move the turtle forward by a random distance."""
        rand_distance = random.randint(0, 10)
        self.forward(rand_distance)


def setup_screen(width, height, title):
    """Setup the main screen for the race with padding for start and finish."""
    screen = Screen()
    screen.title("NINJA TURTLES RACING GAME")
    screen.setup(width, height)
    user_bet = screen.textinput(title=title, prompt="Which Ninja Turtle will win the race? "
                                                    "Leonardo, Michelangelo, Raphael, Donatello")
    return screen, user_bet


def create_racers(names, colors, start_x, y_positions):
    """Create multiple RacingTurtle instances based on names, colors, and y positions."""
    return [RacingTurtle(name, color, (start_x, y)) for name, color, y in zip(names, colors, y_positions)]


def check_winner(turtles, user_bet):
    """Check if any turtle has won the race, and print the result."""
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_name = turtle.name
            winning_color = turtle.pencolor()
            if winning_name == user_bet:
                print(f"You've won! {winning_name}, the {winning_color} turtle, is the winner.")
            else:
                print(f"You've lost! {winning_name}, the {winning_color} turtle, is the winner.")
            return True, winning_name
    return False, None


def main():
    # Constants for setup
    width = 600
    height = 400
    title = "Choose a Ninja Turtle"
    padding = 20
    turtle_names = ["Leonardo", "Michelangelo", "Raphael", "Donatello"]
    turtle_colors = ["blue", "orange", "red", "purple"]
    start_x = -width // 2 + padding  # Start line with padding

    # Calculate evenly spaced y positions
    interval = height // (len(turtle_names) + 1)
    y_positions = [(-height // 2 + (i + 1) * interval) for i in range(len(turtle_names))]

    # Setup game
    screen, user_bet = setup_screen(width, height, title)
    racers = create_racers(turtle_names, turtle_colors, start_x, y_positions)

    # Start race if user made a bet
    race_on = bool(user_bet)

    # Main race loop
    while race_on:
        for racer in racers:
            racer.race()
            race_over, winner = check_winner(racers, user_bet)
            if race_over:
                race_on = False
                break

    screen.exitonclick()


if __name__ == "__main__":
    main()
