from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    is_on = True

    coffee_maker = CoffeeMaker()
    machine_menu = Menu()
    money_machine = MoneyMachine()

    while is_on:
        next_action = input(f"What would you like? ({machine_menu.get_items()}: ")

        if next_action == "off":
           is_on = False
           return
        elif next_action == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = machine_menu.find_drink(next_action)

            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

coffee_machine()