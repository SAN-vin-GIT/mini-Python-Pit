import turtle
import pandas

guessed = []
screen = turtle.Screen()
screen.title("Guss the State")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


while len(guessed) < 50:
    answer = screen.textinput(title=f" Guess a State, Guessed: {len(guessed)}/60",prompt="What's another state's name?").title()

    if answer == "Exit":
        missing = []
        for stat in states:
            if stat not in guessed:
                missing.append(stat)
        print(missing)
        break

    if answer in states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

        print(f"Your answer {answer} is in the table.")


