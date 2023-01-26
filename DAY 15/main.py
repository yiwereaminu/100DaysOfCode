import resources

# print(resources.MENU)
# print(resources.resources)

# TODO 1 prompt the user to chose what they want


user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()


#  TODO 2 check if there is enough resources to serve the user
def check_for_sufficient_resource(choice):
    """this function checks if there are enough resources to make the beverage of choice"""
    choice = user_choice
    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        water = resources.MENU[user_choice]['ingredients']['water']
        coffee = resources.MENU[user_choice]['ingredients']['coffee']
        available_water = resources.resources['water']

        available_coffee = resources.resources['coffee']

        if choice == 'latte' or choice == 'cappuccino':
            available_milk = resources.resources['milk']
            if available_water < water:
                print(f"Sorry there is not enough water")
                return True
            elif available_coffee < coffee:
                print('Sorry there is not enough coffee')
                return True
            elif available_milk < resources.MENU[user_choice]['ingredients']['milk']:
                print("Sorry there is not enough milk")
                return True
        elif choice == 'espresso':
            if available_water < water:
                print("Sorry there is not enough water")
                return True
            elif available_coffee < coffee:
                print("Sorry there is not enough coffee")
                return True
    return False


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_coins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    cost = resources.MENU[user_choice]['cost']
    if total_coins < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_coins > cost:
        print(f"Here is ${round((total_coins - cost), 2)} in change.")
        return True


def make_beverage(choice):
    total_money_made = 0.0

    choice = user_choice
    if check_for_sufficient_resource(choice) and process_coins():
        total_money_made += resources.MENU[choice]['cost']
    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        water = resources.MENU[user_choice]['ingredients']['water']
        coffee = resources.MENU[user_choice]['ingredients']['coffee']
        available_water = resources.resources['water']

        available_coffee = resources.resources['coffee']
        if choice == 'espresso':
            print("Here is your espresso. Enjoy!")
            resources.resources['water'] = available_water - water
            resources.resources['coffee'] = available_coffee - coffee
        elif choice == 'latte':
            print('Here is your latte. Enjoy!')
            available_milk = resources.resources['milk']
            resources.resources['water'] = available_water - water
            resources.resources['coffee'] = available_coffee - coffee
            resources.resources['milk'] = available_milk - resources.MENU[user_choice]['ingredients']['milk']
        elif choice == 'cappuccino':
            print('Here is your cappuccino. Enjoy!')
            available_milk = resources.resources['milk']
            resources.resources['water'] = available_water - water
            resources.resources['coffee'] = available_coffee - coffee
            resources.resources['milk'] = available_milk - resources.MENU[user_choice]['ingredients']['milk']
    elif user_choice == 'report':
        print(f"Water: {resources.resources['water']}ml")
        print(f"Milk: {resources.resources['milk']}ml")
        print(f"Coffee: {resources.resources['coffee']}g")
        print(f"Money: ${total_money_made}")


# def print_report():
#     money = 0.0
#     money += resources.MENU[user_choice]['cost']
#     print(f"Water: {resources.resources['water']}ml")
#     print(f"Milk: {resources.resources['milk']}ml")
#     print(f"Coffee: {resources.resources['coffee']}g")
#     print(f"Money: ${money}")

#

# check_for_sufficient_resource(user_choice)
# process_coins()
# make_beverage(user_choice)
def execute():
    if user_choice == 'report':
        make_beverage(user_choice)
        execute()
    check_for_sufficient_resource(user_choice)
    process_coins()
    make_beverage(user_choice)


#
# while not check_for_sufficient_resource(user_choice):
#     execute()
execute()
