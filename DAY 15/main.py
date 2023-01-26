import resources

print(resources.MENU)
print(resources.resources)
# TODO 1 prompt the user to chose what they want

user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

#  TODO 2 check if there is enough resources to serve the user
def check_for_sufficient_resource(choice):
    """this function checks if there are enough resources to make the beverage of choice"""
    choice = user_choice
    water = resources.MENU[choice]['ingredients']['water']
    coffee = resources.MENU[choice]['ingredients']['coffee']
    available_water = resources.resources['water']
    available_milk = resources.resources['milk']
    available_coffee = resources.resources['coffee']

    if choice == 'latte' or choice == 'cappuccino':
        milk = resources.MENU[choice]['ingredients']['milk']
        if available_water < water:
            print(f"Sorry there is not enough water")
        elif available_coffee < coffee:
            print('Sorry there not enough coffee')
        elif available_milk < milk:
            print("Sorry there is not enough milk")
    elif choice == 'espresso':
        if available_water < water:
            print("Sorry there is not enough water")
        elif available_coffee < coffee:
            print("Sorry there is not enough coffee")


check_for_sufficient_resource(user_choice)
