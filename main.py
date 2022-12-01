from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# TODO 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#  repeat it until turn off the 'machine'
is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    # TODO 2.Turn off the Coffee Machine by entering “off” to the prompt
    if choice == "off":
        is_on = False
    # TODO 3. Print report.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            # TODO 4.Check resources sufficient and transaction successful
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                # TODO 5.Make Coffee
                coffee_maker.make_coffee(drink)







