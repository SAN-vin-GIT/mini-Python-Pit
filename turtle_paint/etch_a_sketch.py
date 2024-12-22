from turtle import Turtle,Screen

terry = Turtle()
screen = Screen()


def move_forward():
    terry.forward(25)

def move_backward():
    terry.backward(25)

def turn_right():
    terry.right(25)
def turn_left():
    terry.left(25)
def clear():
    terry.reset()

screen.listen()
screen.onkey(key = "w",fun = move_forward)
screen.onkey(key = "s", fun = move_backward )
screen.onkey(key = "d", fun = turn_right )
screen.onkey(key = "a", fun = turn_left )
screen.onkey(key = "c", fun = clear )



screen.exitonclick()