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

on = True
water = 500
milk = 350
coffee = 150
money = 0.0




def report():
    print(f"Water:{water}")
    print(f"Milk:{milk}")
    print(f"Coffee:{coffee}")
    print(f"Money:{money}")

def process_coins():
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))

    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    total_value = (quarters * quarter_value) + (dimes * dime_value) + (nickels * nickel_value) + (pennies * penny_value)

    return total_value


def check(drink):
    """Checks if there are enough ingredients for the selected drink."""
    ingredients = MENU[drink]["ingredients"]
    if water >= ingredients["water"] and coffee >= ingredients["coffee"]:
        if "milk" in ingredients:
            if milk >= ingredients["milk"]:
             return True
            else:
             print("Insufficient Milk")
             return False
        else:
            return True

    elif water <= ingredients["water"]:
        print("Insufficient Water")
        return False
    elif coffee <= ingredients["coffee"]:
        print("Insufficient coffee")
        return False



def update_resources(drink):
    """Deducts the ingredients from the resources after making a drink."""
    ingredients = MENU[drink]["ingredients"]
    global water, coffee, milk
    water -= ingredients["water"]
    coffee -= ingredients["coffee"]
    if "milk" in ingredients:
        milk -= ingredients["milk"]


def espresso():
    global money
    drink = "espresso"
    total_value = process_coins()

    if check(drink):
        if total_value >= MENU[drink]["cost"]:
            excess = total_value - MENU[drink]["cost"]


            money += MENU[drink]["cost"]

            if excess > 0:
                print(f"Excess money refunded: ${excess:.2f}")
                total_value -= excess

            update_resources(drink)
            print(f"Money collected: ${money:.2f}")

        else:
            print("Insufficient Funds, Money Refunded")
    else:
        print("Sorry Insufficient Resources")

def latte():
    global money
    drink = "latte"
    total_value = process_coins()

    if check(drink):
        if total_value >= MENU[drink]["cost"]:
            excess = total_value - MENU[drink]["cost"]


            money += MENU[drink]["cost"]

            if excess > 0:
                print(f"Excess money refunded: ${excess:.2f}")
                total_value -= excess

            update_resources(drink)
            print(f"Money collected: ${money:.2f}")

        else:
            print("Insufficient Funds, Money Refunded")
    else:
        print("Oops Looks Like We Forgot To Restock. Your Cash Is Refunded")

def cappuccino():
    global money
    drink = "cappuccino"
    total_value = process_coins()

    if check(drink):
        if total_value >= MENU[drink]["cost"]:
            excess = total_value - MENU[drink]["cost"]


            money += MENU[drink]["cost"]

            if excess > 0:
                print(f"Excess money refunded: ${excess:.2f}")
                total_value -= excess

            update_resources(drink)
            print(f"Money collected: ${money:.2f}")

        else:
            print("Insufficient Funds, Money Refunded")
    else:
        print("Oops Looks Like We Forgot To Restock. Your Cash Is Refunded")


def main():
    global on,milk,water,money,coffee
    while on is True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            on = False
        elif choice == "report":
            report()
        elif choice in MENU:
            if choice == "espresso":
                espresso()
            if choice == "latte":
                latte()
            if choice == "cappuccino":
                cappuccino()
        else:
            print("Invalid choice, please select espresso, latte, or cappuccino.")

main()







