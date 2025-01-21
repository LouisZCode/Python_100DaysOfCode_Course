import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

#add an image to the turtle shapes list:
image = "blank_states_img.gif"
screen.addshape(image)

#Now we can load that image as a shape for a turtle:
turtle.shape(image)

game_on = True
score = 0

#Turtle that writes
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()


states_data = pandas.read_csv("50_states.csv")
states_column = states_data.state
states_list = states_column.to_list()
#print(states_list)

guessed_states = []


while game_on:
    answer_state = (screen.textinput(title=f"Guess the State {score}/{len(states_column)}", prompt= "Whats another state Name?")).title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in states_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn_these.csv")
        break

    if answer_state in states_list:
        score += 1
        print(f"its here!, your score is {score}/{len(states_column)}")
        guessed_states.append((answer_state))
        states_list.remove(answer_state)
        #write a turtle in there, turtle that writes!

        """Get a hold of the x and y of the .csv"""
        state_row = states_data[states_data.state == answer_state]
        # print(state_row)
        state_x = int(state_row.x.iloc[0])
        state_y = int(state_row.y.iloc[0])
        #You can also use .item() to take the item form the series, meaning, the number of the coordinate
        turtle.goto(state_x, state_y)
        turtle.write(f"{answer_state}")

    elif answer_state in guessed_states:
        print("You already guessed that one!")
    else:
        print("Sorry, not a state")

