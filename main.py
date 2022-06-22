MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def drink():
    money = 0
    x = True
    while x:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "report":
            for resource in resources:
                if resource == "coffee":
                    print(f"{resource}: {resources[resource]}g")
                else:
                    print(f"{resource}: {resources[resource]}ml")
            print(f"Money: ${money}")
        elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
            if MENU[drink]["ingredients"]["water"] > resources["water"]:
                print("Sorry, there is not enough water")
            if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry, there is not enough coffee")
            if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry, there is not enough milk")
            else:
                print("Please insert some coins.")
                quarter = int(input("How many quarters?: "))
                dime = int(input("How many dimes?: "))
                nickel = int(input("How many nickels?: "))
                penny = int(input("How many pennies?: "))
                payment = 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny
                if payment < MENU[drink]["cost"]:
                    print("Sorry, that is not enough money. Money refunded")
                else:
                    change = round(payment - MENU[drink]["cost"], 2)
                    print(f"Here is ${change} in change")
                    print(f"Here is your {drink}☕ Enjoy!")
                    money += MENU[drink]["cost"]
                    resources["water"] -= MENU[drink]["ingredients"]["water"]
                    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        elif drink == "turn off":
            print(turn_off())
            x = False


def turn_off():
    return "Turning off"


drink()
