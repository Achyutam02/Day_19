import random
from turtle import Turtle, Screen

# def move_forward():
#     turtle.forward(10)
#
# def move_back():
#
#     turtle.backward(10)
#
# def move_left():
#     turtle.left(10)
#
# def move_right():
#     turtle.right(10)
#
# def clear():
#     turtle.reset()


# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear)
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Guess the Winner ")
print(f"your choice is {user_bet}")
colors = ["red", "blue", "yellow", "green", "orange", "purple"]
y_position = [100, 70, 40, 10, -20, -50]

is_race_on = False
all_turtle = []

for i in range(0, 6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won the winning turtle is {winning_color}")
            else:
                print(f"you lost winning turtle is {winning_color}")


        distance = random.randint(0, 10)
        turtle.forward(distance)



screen.exitonclick()
