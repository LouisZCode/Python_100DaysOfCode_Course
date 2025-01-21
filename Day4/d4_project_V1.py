#Rock, Paper, Scissor GAME!

#But evolved with my idea:

import random

#We create a value for the total life of each other
player_life = 10
enemy_life = 10
#Note, important! life seems to be a BIG factor... to add values that make sense

#We also create that the game is on for the While loop..!
game_on = True

#The game will not end until the condition of life = 0 happens..! meanwhile it is true
while game_on == True:

#This will print after every Round, so you know how much life you have left...
    print(f'\nYou have {player_life} life points\n\nEnemy has {enemy_life} life points\n')

#Enemy attacks, so far basic R,P,S
    attacks = ["ROCK", "PAPER", 'SCISSOR']

#Here to choose the attack you will do: a simple choice, R,P,S?
    player_choice = input('choose one attack:\nRock "ROCK", Paper "PAPER" or Scissor "SCISSOR"\n').upper()
    print(f'Player chose {player_choice}')

#This one is a random one! so far it takes it random from a list... but would be fun to mess with the probabilities for the game..!
#This choses the 3 attacks, so there is 33% prob of each to be land...
    pc_choice = random.choice(attacks)
    print(f'Enemy chose {pc_choice}')

#What if I add things that change the probabilities? Taunts... learning form the computer... biases depending on sprite design, etc..
#Add another value, defense? we can do that on V2 Ex.  player defense = 1 and Enemy_health = 5 would be more "fun"

    if player_choice == pc_choice:
        print("Its a TIE!")

    elif player_choice == "ROCK" and pc_choice == "PAPER":
        print('You lose!')
        player_life -= 2

    elif player_choice == "ROCK" and pc_choice == "SCISSOR":
        print('You Win!')
        enemy_life -= 2

    elif player_choice == "PAPER" and pc_choice == "SCISSOR":
        print('You lose!')
        player_life -= 2

    elif player_choice == "PAPER" and pc_choice == "ROCK":
        print('You Win!')
        enemy_life -= 2

    elif player_choice == "SCISSOR" and pc_choice == "ROCK":
        print('You Lose!')
        player_life -= 2

    elif player_choice == "SCISSOR" and pc_choice == "PAPER":
        print('You Win!')
        enemy_life -= 2

    else:
        print('Not a valid value, you LOSE!')

    if enemy_life == 0:
        game_on = False
        print("You won!!")

    elif player_life == 0:
        game_on = False
        print('You lost!!')

#elif player_choice