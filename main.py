from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_machine_on = True
while is_machine_on:
    drink_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if drink_choice == "off":
        is_machine_on = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(drink_choice):
        drink_choice = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink_choice):
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)
