from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()
# money.make_payment()


flag = True

while flag:
    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if user_choice == 'off':
        flag = False
    elif user_choice == 'report':
        make_coffee.report()
        money.report()
    else:
        cost = menu.menu[0].cost
        ingredient = menu.menu[0].ingredients
        menu_item = MenuItem(user_choice, ingredient['water'], ingredient['milk'], ingredient['coffee'], cost)
        if make_coffee.is_resource_sufficient():
            make_coffee.make_coffee(user_choice)

