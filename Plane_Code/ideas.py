import random

options = ["R", "P", "S"]

"""LOGIC"""
"R" < "P"
"P" < "S"
"S" < "R"

while True:
    player = input('your choice:')
    pc = random.choice(options)
    print(pc)

    if player > pc:
        print("you win")
    elif player < pc:
        print("you lose")
    else:
        print("draw")