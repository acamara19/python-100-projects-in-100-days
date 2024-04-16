"""
A Calculator Program:
---------------------
"""
import sys
from art import logo


# Function to add numbers
def add(n1, n2):
    return n1 + n2


# Function to Subtract numbers
def subtract(n1, n2):
    return n1 - n2


# Function to Multiply numbers
def multiply(n1, n2):
    return n1 * n2


# Function to Divide numbers
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_input = input(f"Type (y) to continue calculating with [{answer}], "
                           f"or type (n) to start a new operation, "
                           f"or type any other key to (exit): ").lower()
        if user_input == "y":
            num1 = answer
        elif user_input == "n":
            should_continue = False
            calculator()
        else:
            sys.exit()


calculator()
