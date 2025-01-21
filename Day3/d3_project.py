print('''
________________Welcome to the Treasure Island!______________\n\nYour arrive to an Island, and you see a road and the jungle,"
      ''')

#First choice
choice1 = input("Do you want to take the ROAD or go trought the JUNGLE?\nType your answer here:\n").upper()

#If the valie of Chice 1 is X, aor if not, Y... any other answer goes to the else
if choice1 == "ROAD":
    print("\nYour find a lake... it looks peacefull!\nThere is a boat coming, but it looks like it will take too long!\n")
    choice2 = input("Do you want to WAIT for the boat, or try to SWIM trough the lake?\nType your answer here:\n").upper() #All upper so there is no issue with typing things
    #Here we get the value of choice 2. It is inside so it does not trigger later outside of the if/elses
    if choice2 == "WAIT":
        print("\nWell done!. You arrived to the cabin on the other side! Patience paid..!")
        choice3 = input("There are 3 doors in the cabin, which one do you choose?\nRed, Blue or Yellow?\n").upper()
                #Same with Choice3 now
        if choice3 == "BLUE":
            print("\nThat was it! You found the TREASUERE!!\n\n________YOU WON!!!_____\n\n")
        elif choice3 == "RED":
            print("\nOf course this was a fire!! dummy...you just burned to death")
            print("\n------------GAME OVER-------------\n\n")
        elif choice3 == "YELLOW":
            print("\nA light so strong comes out of the door, deintegrating your body to a cellular level\nYou died")
            print("\n------------GAME OVER-------------\n\n")
        else:
            print("Daaamn and just int he last choice you had to typo!! sorry.. back to the start :(")

    elif choice2 == "SWIM":
            print("You just arrived tot he island, do you think you have energy??...\nYou just drowned\n")
            print("\n------------GAME OVER-------------\n\n")

    else:
        print("Sorry I did not understand... lets start again!")


elif choice1 == "JUNGLE":
    print("A monkey attacked you, and killed you...")
    print("\n------------GAME OVER-------------\n\n")


else:
    print("Sorry I did not understand... lets start again!")

#if choice2 == "WAIT":
 #   print("You arrived to the cabin on the other side! Patience paid..!")