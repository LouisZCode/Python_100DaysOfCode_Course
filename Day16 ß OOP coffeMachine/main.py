"""We got access to 4 Classes"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#just preping for the while loop
coffe_machine_on = True

"""I forgot to activate the class using the ()! """
"""Also, good to make all the classes, Objects at the beginning, so you can tap onto them later"""
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()
menu_item = MenuItem


while coffe_machine_on:

    decision = input(f'What would you like to drink?\nwe have {my_menu.get_items()}!\n')

    if decision == 'off':
        exit()

    elif decision == 'report':
        coffe_maker.report()
        money_machine.report()
        print('')

    elif decision in my_menu.get_items():
        drink = my_menu.find_drink(decision)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
                print('')
    else:
        print('Sorry I did not understand that, please try again\n')
