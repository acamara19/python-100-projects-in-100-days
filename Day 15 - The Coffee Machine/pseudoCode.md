# Pseudocode for Coffee Machine Program

Pseudocode outline for the Coffee Machine program, breaking down the process into logical steps:

```plaintext
Initialize resources with starting values (water, milk, coffee, money)

Function MAIN:
    Loop indefinitely until the user decides to turn off the machine:
        Display a prompt asking what the user would like to order (espresso, latte, cappuccino)
        
        If the input is "off":
            Terminate the program
        
        Else if the input is "report":
            Call the PRINT_REPORT function to display current resource levels and money collected
        
        Else if the input matches one of the drinks in the menu:
            Call CHECK_RESOURCES with selected drink's ingredients
                If resources are sufficient:
                    Prompt user to insert coins
                    Call PROCESS_COINS to calculate total money inserted
                    Call CHECK_TRANSACTION to verify if the inserted amount covers the drink cost
                        If transaction is successful:
                            Deduct the ingredients from resources
                            Update money
                            Inform the user that their drink is ready
                        Else:
                            Refund the money and inform the user
        
        Else:
            Inform the user that the selection was invalid and prompt again

Function PRINT_REPORT:
    Print the current state of resources and money in a tabular format

Function CHECK_RESOURCES (ingredients):
    Check if each required ingredient is available in sufficient amount
    Return true if all ingredients are sufficient, else false and notify the user

Function PROCESS_COINS:
    Prompt the user to enter the number of each type of coin
    Calculate and return the total amount of money inserted

Function CHECK_TRANSACTION (inserted_money, drink_cost):
    Compare inserted money with the drink cost
    If sufficient, calculate change if any and update the money resource
    Return true if successful, else refund money and return false

Function MAKE_COFFEE (drink_name, drink_ingredients):
    Deduct the required ingredients from the resources
    Notify the user that their drink is prepared

MAIN
```