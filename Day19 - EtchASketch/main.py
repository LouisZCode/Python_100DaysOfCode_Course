import turtle as t

turtle = t.Turtle()
screen = t.Screen()

def move_forward():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def rotate_left():
    turtle.left(10)

def rotate_right():
    turtle.right(10)

def reset():
    turtle.reset()


#this activates the input - Event listen
screen.listen()

#we create a function as an input!
screen.onkey(key="w", fun=move_forward)    #NOTE, if it is a parameter, a function do not use the ()
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=reset)

#this just so the screen does not exit without us doing so
screen.exitonclick()