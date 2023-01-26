import resources

print(resources.MENU)
print(resources.resources)

# TODO 1 prompt the user to chose what they want

user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
water = resources.MENU[user_choice]['ingredients']['water']
coffee = resources.MENU[user_choice]['ingredients']['coffee']
available_water = resources.resources['water']
available_milk = resources.resources['milk']
available_coffee = resources.resources['coffee']


#  TODO 2 check if there is enough resources to serve the user
def check_for_sufficient_resource(choice):
    """this function checks if there are enough resources to make the beverage of choice"""
    choice = user_choice

    if choice == 'latte' or choice == 'cappuccino':

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
    choice = user_choice

    if choice == 'espresso':
        print("Here is your espresso. Enjoy!")
        resources.resources['water'] = available_water - water
        resources.resources['coffee'] = available_coffee - coffee
    elif choice == 'latte':
        print('Here is your latte. Enjoy!')
        resources.resources['water'] = available_water - water
        resources.resources['coffee'] = available_coffee - coffee
        resources.resources['milk'] = available_milk - resources.MENU[user_choice]['ingredients']['milk']
    elif choice == 'cappuccino':
        print('Here is your cappuccino. Enjoy!')
        resources.resources['water'] = available_water - water
        resources.resources['coffee'] = available_coffee - coffee
        resources.resources['milk'] = available_milk - resources.MENU[user_choice]['ingredients']['milk']


print(resources.resources['water'])
process_coins()
check_for_sufficient_resource(user_choice)
make_beverage(user_choice)
print(resources.resources['water'])
