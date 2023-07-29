from art import logo
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

is_game_on = True
money_inserted = 0


def process_order(choice):
    # TODO: 1. Get the coffee data from the MENU based on the user's choice.
    coffee_data = MENU.get(choice)
    if coffee_data is None:
        return "Please select the right coffee name"

    water_needed = coffee_data["ingredients"].get("water", 0)
    milk_needed = coffee_data["ingredients"].get("milk", 0)
    coffee_needed = coffee_data["ingredients"].get("coffee", 0)
    # TODO: 2. Check if there are enough resources to make the selected drink.
    if water_needed > resources["water"] or coffee_needed > resources["coffee"] or milk_needed > resources["milk"]:
        return "Sorry, there are not enough resources to make this drink. Please try again."

    # Calculate the change, if any, after deducting the ingredients' cost
    change = money_inserted - coffee_data["cost"]

    # TODO: 3. Check if the user has inserted enough money for the selected drink.
    if change < 0:
        return "Sorry, that's not enough money. Money refunded."

    # Deduct the ingredients' cost from the resources.
    resources["water"] -= water_needed
    resources["coffee"] -= coffee_needed
    resources["milk"] -= milk_needed

    # TODO: 4. Prepare the message to display based on the transaction.
    return f"Your {choice.capitalize()} is on the way! Here is ${change:.2f} in change. Enjoy!"


while is_game_on:
    print(logo)
    # TODO: 5. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed,
    # e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
    coffee_choice = input("What Would you like? (espresso/latte/cappuccino)?: ").lower()

    if coffee_choice == "off":
        # TODO: 6. Turn off the Coffee Machine by entering “off” to the prompt.
        # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
        # Your code should end execution when this happens.
        is_game_on = False
    elif coffee_choice == "report":
        # TODO: 7. Print report.
        # a. When the user enters “report” to the prompt, a report should be generated
        # that shows the current resource values. e.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        print(
            f"Our current resources are:\nWater: {resources['water']} ml\nCoffee: {resources['coffee']} g\nMilk:"
            f" {resources['milk']} ml\nMoney: {money_inserted:.2f}")
    else:
        # TODO: 8. Check resources sufficient?
        # a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
        # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
        # It should not continue to make the drink but print: “Sorry there is not enough water.”
        # c. The same should happen if another resource is depleted, e.g. milk or coffee.
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies: "))
        money_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

        # TODO: 9. Process coins.
        # a. If there are sufficient resources to make the drink selected,
        # then the program should prompt the user to insert coins.
        # b. Remember that quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted.
        # E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        result = process_order(coffee_choice)

        # TODO: 10. Check transaction successful?
        # a. Check that the user has inserted enough money to purchase the drink they selected.
        # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should
        # say “Sorry that's not enough money. Money refunded.”
        # b. But if the user has inserted enough money,
        # then the cost of the drink gets added to the machine as the profit and
        # this will be reflected the next time
        # “report” is triggered. E.g. Water: 100ml, Milk: 50ml, Coffee: 76g, Money: $2.5
        # c. If the user has inserted too much money, the machine should offer change.
        # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
        print(result)
