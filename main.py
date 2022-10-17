from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ".lower())
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-120, -70, -30, 30, 70, 120]
turtle_list = []
for n in range(0, 6):
    turtle_list.append(Turtle(shape="turtle"))
    turtle_list[n].color(colors[n])
    turtle_list[n].penup()
    turtle_list[n].goto(x=-240, y=y[n])

finish = 230


def is_at_finish():
    if turtle_list[n].xcor() == finish:
        return True
    else:
        return False


def turtle_race():
    race = False
    if user_bet:
        race = True

    color_of_the_winner = ""
    n = 0
    while race:
        if is_at_finish():
            color_of_the_winner = turtle_list[n].pencolor()
            race = False
        else:
            random_distance = random.randint(0, 10)
            if random_distance + turtle_list[n].xcor() > 230:
                turtle_list[n].goto(x=230, y=turtle_list[n].ycor())
                color_of_the_winner = turtle_list[n].pencolor()
                race = False
            else:
                turtle_list[n].forward(random_distance)

            if n == 5:
                n = 0
            else:
                n += 1

    if color_of_the_winner == user_bet:
        print(f"You win! The {user_bet} has won!")
    else:
        print(f"You loose! The {color_of_the_winner} has won!")


turtle_race()

screen.exitonclick()
