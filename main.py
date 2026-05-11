from pprint import isreadable
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=900, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["indigo", "red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [210, 140, 70, 0, -70, -140, -210]
all_turtles = []

for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-435, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 415:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.forward(random.randint(1, 10))


screen.exitonclick()