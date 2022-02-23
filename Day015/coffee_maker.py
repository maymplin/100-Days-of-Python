# -*- coding: utf-8 -*-
"""
Day 15: Coffee MAchine
https://replit.com/@appbrewery/coffee-machine-final?

"""

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def new_action():
    """ Prompts user to enter a choice for the coffee machine to process """

    return input("What would you like? (espresso/latte/cappuccino): ")


def prompt_payment():
    """ Prompts user to enter coins and return total amount in dollars """

    print("Please insert coins.")
    quarters = int(input("  How many quarters? "))
    dimes = int(input("  How many dimes? "))
    nickels = int(input("  How many nickels? "))
    pennies = int(input("  How many pennies? "))

    total_amount = process_coins(quarters, dimes, nickels, pennies)

    return total_amount


def print_report(dollar_amount):
    """ Prints resources amount """

    for resource in resources:
        print(f"  {resource.title()}: {resources[resource]}ml")

    print(f"  Money: ${dollar_amount}")


def check_resource(drink):
    """ Returns True if remaining resource is enough to make user-requested
        drink; otherwise, prints a message and returns False
    """

    message = "Sorry there is not enough "

    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print(message + ingredient + ".")
            return False

    return True


def use_resource(drink):
    """ Reduces machine resources by amount used to make user-requested drink
    """
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]


def process_coins(quarters, dimes, nickels, pennies):
    """ Adds coins and returns total amount in dollars """

    coins = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01,
        }

    total_amount = quarters*coins["quarter"] + dimes*coins["dime"] \
        + nickels*coins["nickel"] + pennies*coins["penny"]

    return total_amount


def check_payment(payment, drink):
    """ Returns difference between user payment and drink cost"""

    return payment - drink["cost"]


def coffee_machine():
    machine_operations = ["report", "off"]
    machine_drink_choices = ["espresso", "latte", "cappuccino"]

    profit = 0
    machine_on = True

    while machine_on:
        action = new_action().lower()

        if action in machine_drink_choices:
            if check_resource(MENU[action]):
                payment_amount = prompt_payment()
                change = check_payment(payment_amount, MENU[action])
                if change >= 0:
                    use_resource(MENU[action])
                    profit += (payment_amount - change)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {action} ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif action in machine_operations:
            if action == "report":
                print_report(profit)
            elif action == "off":
                machine_on = False
                break
        else:
            "Invalid choice.\n"


coffee_machine()
