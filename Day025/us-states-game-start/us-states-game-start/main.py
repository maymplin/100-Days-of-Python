# https://www.sporcle.com/games/g/states
# Replicating the sporcle quiz
import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Ariel", 7, "normal")

states = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
state_text = turtle.Turtle()
state_text.hideturtle()
state_text.penup()

all_states_list = []

for state in states.state:
    all_states_list.append(state)

# print(all_states_list)
game_over = False
while not game_over:
    answer_state = screen.textinput("Guess the Sate", "What's another state's name?").title()
    if answer_state in all_states_list:
        correct_state = states[states["state"] == answer_state]
        state_text.goto(int(correct_state.x), int(correct_state.y))
        state_text.write(answer_state, align=ALIGNMENT, font=FONT)
        all_states_list.remove(answer_state)
        print(all_states_list)
    game_over = True if len(all_states_list) == 0 else False
    if game_over:
        state_text.goto(0, 0)
        state_text.color("red")
        state_text.write("GAME OVER", align=ALIGNMENT, font=("Ariel", 40, "normal"))


# https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle
# def get_mouse_click_coor(x, y):
#     # turtle.onscreenclick(None)
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

screen.exitonclick()
