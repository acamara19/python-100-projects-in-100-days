"""
THE COFFEE MACHINE PROGRAM:
"""

from coffeeItems import MENU, resources


def print_report():
    # Headers for resources and menu
    resource_headers = "Resource    | Amount"
    menu_headers = "Drink       | Cost  | Ingredients"

    # Generate resource info lines
    resources_info = [
        f"{'Water💧':<10} | {resources['water']}ml",
        f"{'Milk 🥛':<10} | {resources['milk']}ml",
        f"{'Coffee ☕️':<11} | {resources['coffee']}g",
        f"{'Money 🏦':<10} | ＄{resources['profit']:.2f}"
    ]

    # Determine the maximum length for resource and menu headers
    max_length_resources = max(len(line) for line in resources_info + [resource_headers])

    print("\nCurrent Machine Resources:")
    print('-' * max_length_resources)
    print(resource_headers)
    print('-' * max_length_resources)
    for line in resources_info:
        print(line)
    print('-' * max_length_resources + '\n')

    # Collecting all menu lines to ensure columns align properly
    menu_lines = []
    for drink, details in MENU.items():
        ingredients = ', '.join([f"{k}: {v}g/ml" for k, v in details['ingredients'].items()])
        line = f"{drink.capitalize():<10}  | ＄{details['cost']:<4} | {ingredients}"
        menu_lines.append(line)

    max_length_menu = max(len(line) for line in menu_lines + [menu_headers])

    print("Menu:")
    print('-' * max_length_menu)
    print(menu_headers)
    print('-' * max_length_menu)
    for line in menu_lines:
        print(line)
    print('-' * max_length_menu)


def check_resources(drink_name, drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"\nSorry there is not enough {item} to make {drink_name}")
            print_report()
            return False
        return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


def check_transaction(inserted_money, drink_cost):
    if inserted_money >= drink_cost:
        change = round(inserted_money - drink_cost, 2)
        if change > 0:
            print(f"Here's ＄{change} in change.")
        resources['profit'] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here's your {drink_name} ☕️. Enjoy!")


def main():
    resources['profit'] = 0
    machine_state = True

    while machine_state:
        user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")
        if user_choice == 'off':
            machine_state = False
        elif user_choice == 'report':
            print_report()
        elif user_choice in MENU:
            drink = MENU[user_choice]
            if check_resources(user_choice.capitalize(), drink['ingredients']):
                payment = process_coins()
                if check_transaction(payment, drink['cost']):
                    make_coffee(user_choice, drink['ingredients'])
        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()
