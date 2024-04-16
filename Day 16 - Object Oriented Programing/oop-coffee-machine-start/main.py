##########################################################################
#  COFFEE MAKER MACHINE PROGRAM USING OBJECT ORIENTED PROGRAMING (OOP)  ##
##########################################################################


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def main():
    machine_state = True

    while machine_state:
        options = menu.get_items()
        user_choice = input(f"\nWhat would you like? ({options}): ")
        if user_choice == 'off':
            machine_state = False
        elif user_choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_choice)

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    main()
