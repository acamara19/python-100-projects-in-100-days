"""
Functions:

def my_functions():
    #Do this
    #Then do this
    #Finally does this
"""


#  Day 8 - Start
#  Simple functions
def greet():
    print("Hello World!")
    print("Welcome to the United States")
    print("How are you")


greet()


#  Functions that allow for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing today {name}")


greet_with_name("Ansoumane")

"""
With functions with input:
    ex: def greet(name) -> name = Parameter
        greet("name") -> name = Argument
"""


#  Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"{name} is from {location}")


greet_with("Ansoumane", "Germantown, MD")


#  Functions with keyword arguments
greet_with(location="Rockville, MD", name="Ansoumane")
