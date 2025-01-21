import pandas
from tkinter import *
import turtle as t
import time

import random

def reset_values():
    global user_att, user_def, pc_att, pc_def
    user_def = 1
    user_att = 1
    pc_def = 1
    pc_att = 1

def action_calculation():
    global user_mana, user_def, user_att, user_lifes

    if user_choice == "D":
        if user_mana >= 1:
            user_def += 1
            user_mana -= 1
            print("you raised your defense +1")
            time.sleep(1)
        else:
            print("you dont have more mana!")

    elif user_choice == "C":
        if user_mana >= 2:
            user_lifes += 2
            user_mana -= 2
            print("you gain +2 lives")
        else:
            print("you dont have more mana!")

    elif user_choice == "B":
        if user_mana >= 1:
            user_att += 1
            user_mana -= 1
            print("you raised your attack +1")
        else:
            print("you dont have more mana!")

    time.sleep(1)


def damage_calculations():
    global user_att, user_def, pc_att, pc_def, user_damage, pc_damage

    if attack == computer_choice:
        user_att -= 1
        user_def -= 1
        pc_att -= 1
        pc_def -= 1
        print("its a DRAW!")

    elif attack == "R":
        # pc wins
        if computer_choice == "P":
            user_att -= 1
            user_def -= 1
            pc_att -= 0
            pc_def -= 1

        # user_wins
        elif computer_choice == "S":
            user_att -= 0
            user_def -= 1
            pc_att -= 1
            pc_def -= 1

    elif attack == "P":
        if computer_choice == "S":
            user_att -= 1
            user_def -= 1
            pc_att -= 0
            pc_def -= 1

        elif computer_choice == "R":
            user_att -= 0
            user_def -= 1
            pc_att -= 1
            pc_def -= 1


    elif attack == "S":
        if computer_choice == "R":
            user_att -= 1
            user_def -= 1
            pc_att -= 0
            pc_def -= 1

        elif computer_choice == "P":
            user_att -= 0
            user_def -= 1
            pc_att -= 1
            pc_def -= 1

    time.sleep(1)


att_options = ["R", "P", "S"]
act_options = ["C", "B", "D"]

user_damage: int
pc_damage: int

user_lifes = 5
user_def = 1
user_att = 1

pc_lifes = 5
pc_def = 1
pc_att = 1

user_stance = ''
pc_stance = ''

user_list = []

user_mana = 3

print("Welcome to Rock, Paper and Scissors!\n")
time.sleep(2)

while user_lifes > 0 or pc_lifes > 0:
    reset_values()

    print(f"You have {user_lifes} lives\nYour enemy has {pc_lifes} lives\n")
    time.sleep(2)

    if user_stance == "":
        user_choice = input("What do you choose as your first attack?\nType R for Rock, P for Paper or S for Scissors.\n").capitalize()
    else:
        user_choice = (input(
                             f"What do you choose? Type R for Rock, P for Paper or S for Scissors.\n"
                                "C for Cure, D for Defend, B for Buff ......(these ones require mana!)\n"
                             f"Current stance: {user_stance}    Current Mana {user_mana}\n"
                             )).capitalize()


    #NORMAL ATTACK
    #If the user chooses an attack:
    if user_choice == "R" or user_choice == "P" or user_choice == "S":
        attack = user_choice
        print(f"User used: {attack}")
        time.sleep(1)
        user_list.append(attack)
        user_stance = attack

        computer_choice = random.choice(att_options)
        print(f"Computer chose: {computer_choice}")
        time.sleep(1)

        damage_calculations()


    #ACTIONS
    #if the user chooses an action:

    elif user_choice == "C" or user_choice == "B" or user_choice == "D":
        attack == user_stance
        print(f"User used: {attack}")
        user_list.append(attack)


        computer_choice = random.choice(att_options)
        print(f"Computer chose: {computer_choice}")

        action_calculation()
        damage_calculations()



    #If the user messes up (only in python)
    else:
        print("not an attack, try again\n")
        continue

    user_damage = user_att - pc_def
    pc_damage = pc_att - pc_def

    #AFTER and END of TURN
    time.sleep(1)
    print(f"\nyour damage is: {user_damage}, enemy damage is {pc_damage}\n")

    pc_lifes -= user_damage
    user_lifes -= pc_damage

    #print(f"your attacks so far: {user_list}")
    #print(f"your current stance is: {user_stance}\n")
    time.sleep(1)

    #if attacks so far has 3 R, P, or S: Add a winner attack to the attack options
    rock_use = user_list.count("R")
    paper_use = user_list.count("P")
    scissor_use = user_list.count("S")

    if rock_use > 3:
        print("you are using ROCK too much... be careful")
        time.sleep(1)
        att_options.append("P")




    if user_lifes == 0:
        print("\nYOU DIED")

    elif pc_lifes == 0:
        print("\nYou WON!")
