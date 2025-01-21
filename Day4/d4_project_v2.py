#Rock, Paper, Scissor GAME!

#Version with Defense on player and less health on enemy

import random

player_life = 10
enemy_life = 7
player_defense = 1
enemy_defense = 0
damage = 2

game_on = True

while game_on == True:

    print(f'\nYou have {player_life} life points\nYou have {player_defense} defense Points\n\nEnemy has {enemy_life} life points\n')

    attacks = ["ROCK", "PAPER", 'SCISSOR']

    player_choice = input('choose one attack:\nRock "ROCK", Paper "PAPER" or Scissor "SCISSOR"\n').upper()
    print(f'Player chose {player_choice}')


    pc_choice = random.choice(attacks)
    print(f'Enemy chose {pc_choice}')


    if player_choice == pc_choice:
        print("Its a TIE!")

    elif player_choice == "ROCK" and pc_choice == "PAPER":
        print('You lose!')
        player_life -= damage - player_defense

    elif player_choice == "ROCK" and pc_choice == "SCISSOR":
        print('You Win!')
        enemy_life -= damage - enemy_defense

    elif player_choice == "PAPER" and pc_choice == "SCISSOR":
        print('You lose!')
        player_life -= damage - player_defense

    elif player_choice == "PAPER" and pc_choice == "ROCK":
        print('You Win!')
        enemy_life -= damage - enemy_defense

    elif player_choice == "SCISSOR" and pc_choice == "ROCK":
        print('You Lose!')
        player_life -= damage - player_defense

    elif player_choice == "SCISSOR" and pc_choice == "PAPER":
        print('You Win!')
        enemy_life -= damage - enemy_defense

    else:
        print('Not a valid value, you LOSE!')

#Had to change this to lower/equal to 0, if not, it stays on -1 etc..
    if enemy_life <= 0:
        game_on = False
        print("\n\n__________ENEMY DIES / YOU WON_________________\n\n")

#Will do the same for the player, even if in this sintance, its hard to lose
    elif player_life == 0:
        game_on = False
        print("\n\n__________ENEMY WINS / YOU DIED_________________\n\n")

#elif player_choice

#NOTE: What if I player with turns? There coul eb a condition (Rock TIE) for example) that if triggered,
#reduces your shield for a turn..! something like this...