import turtle
from turtle import Turtle,Screen
import random

race = False
screen = Screen()
screen.setup(width=600,height=400)
bet = screen.textinput(title="Make a Bet", prompt="Which color will win the race?? Enter your Choice: ")
colors = ["Red","Blue","Green","Purple","Orange","Magenta"]
vertical_positions = [-70, -40, -10, 20, 50, 80]
all_the_turtles = []


for starting_turtles in range(0,6):
    terry_and_bros = Turtle(shape ="turtle")
    terry_and_bros.color(colors[starting_turtles])
    terry_and_bros.penup()
    terry_and_bros.goto(x=-230, y = vertical_positions[starting_turtles])
    all_the_turtles.append(terry_and_bros)


if bet:
    race = True

while race:
    for turtle in all_the_turtles:
        if turtle.xcor() > 270:
            race = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"Your {winner} turtle has won the race. Congratulations!!!")
            else:
                print(f"{winner} turtle has won the race. You Lose!!!")


        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()