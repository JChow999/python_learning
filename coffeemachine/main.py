MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01,
    }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_check(drink, resource_list):
    """Checks if there are enough resources to make drink, returns TRUE if there is enough"""
    # TODO 4. Check if resources are sufficient
    for resource_required in drink["ingredients"]:
        if drink["ingredients"][resource_required] > resource_list[resource_required]:
            print(f"Sorry there is not enough {resource_required}.")
            return False
    print("There is enough")
    return True


def process_coins():
    """Asks the user to enter amount of coins, and returns the total amount of cash"""
    # TODO 5. Process coins
    total_cash = 0
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }
    global COIN_VALUE

    print("Please insert coins.")
    for coin in coins:
        coins[coin] = int(input(f"How many {coin} do you have?: "))
        total_cash += COIN_VALUE[coin] * coins[coin]
    return total_cash


def coin_check(drink, cash):
    """Checks to see if the user has provided enough cash for the transaction. Returns True if there is enough cash"""
    # TODO 6. Check if transaction is successful
    enough_cash = True
    if cash < drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        enough_cash = False
    return enough_cash


def make_coffee(drink, resource_list):
    """Returns the resource list with updated values, from deducting the amount needed to create the drink."""
    # TODO 7. Make Coffee
    for key in drink["ingredients"]:
        if key in resource_list:
            resource_list[key] -= drink["ingredients"][key]
    return resource_list


def coffee_machine():
    """Start the entire coffee machine function"""
    profits = 0
    turn_off = False
    while not turn_off:
        # TODO 1. Prompt user by asking "what would you like?"
        choice = input(" What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            # TODO 3. Print report with resource values
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profits}")
        elif choice == "off":
            # TODO 2. allow machine ot turn off
            turn_off = True
        elif choice in MENU:
            if resource_check(MENU[choice], resources):
                user_cash = process_coins()
                if user_cash >= MENU[choice]["cost"]:
                    make_coffee(MENU[choice], resources)
                    profits += MENU[choice]["cost"]
                    user_cash -= MENU[choice]["cost"]
                    print(f" Here is your ${user_cash:.2f} in change.")
                    print(f" Here is your {choice} ☕️. Enjoy!")
                else:
                    print(" You do not have enough cash.")
            else:
                print(" There is not enough resources to make the drink.")
        else:
            print(" Invalid entry, please type another choice.")


coffee_machine()

