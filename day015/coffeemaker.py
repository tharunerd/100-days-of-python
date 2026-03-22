# Coffee machine resources and menu
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
}


def check_resources(drink):
    """Check if there are enough resources to make the selected drink."""
    if resources["water"] < menu[drink]["water"]:
        print(f"Sorry there is not enough water.")
        return False
    if resources["milk"] < menu[drink]["milk"]:
        print(f"Sorry there is not enough milk.")
        return False
    if resources["coffee"] < menu[drink]["coffee"]:
        print(f"Sorry there is not enough coffee.")
        return False
    return True


def process_coins():
    """Prompt user to insert coins and return the total value."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total


def make_coffee(drink):
    """Make the selected coffee if resources are sufficient and process payment."""
    if not check_resources(drink):
        return

    cost = menu[drink]["cost"]
    inserted_money = process_coins()

    if inserted_money < cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return
    elif inserted_money > cost:
        change = round(inserted_money - cost, 2)
        print(f"Here is ${change} in change.")

    # Deduct resources and add money to the machine
    resources["water"] -= menu[drink]["water"]
    resources["milk"] -= menu[drink]["milk"]
    resources["coffee"] -= menu[drink]["coffee"]
    resources["money"] += cost

    print(f"Here is your {drink}. Enjoy!")


def print_report():
    """Print the current status of the coffee machine resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def run():
    """Main loop to keep the coffee machine running until 'off' is entered."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice == "report":
            print_report()
        elif choice in menu:
            make_coffee(choice)
        else:
            print("Invalid choice. Please select 'espresso', 'latte', or 'cappuccino'.")


# Run the coffee machine
# if __name__ == "__main__":

run()
