MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    },
}
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1 prompt the user to chose what they want
def is_resource_sufficient(selected_drink, resources_available):
    selected_drink = MENU[user_choice]['ingredients']
    resources_available = resources
    for item in resources:
        if selected_drink[item] > resources_available[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def make_coffee(user_drink):
    user_drink = MENU[user_choice]['ingredients']
    print(f"Here is your {user_choice}. Enjoy!")
    for item in user_drink:
        resources[item] -= user_drink[item]


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_coins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total_coins >= MENU[user_choice]['cost']:
        print(f"Here is ${round(total_coins - MENU[user_choice]['cost'], 2)} dollars in change.")
        global profit
        profit += MENU[user_choice]['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


flag = True
while flag:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    # print(MENU[user_choice]['ingredients'])
    if user_choice == 'off':
        flag = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[user_choice]['ingredients']
        if is_resource_sufficient(drink, resources):
            if process_coins():
                make_coffee(drink)
