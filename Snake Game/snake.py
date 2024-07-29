## LetsGrowMore Python Developer Virtual Internship Program

## Task-II

## Creating a Snake Game using Turtle and Random Module


import turtle
import time
import random

delay, score, high_score = 0.1, 0, 0

# Screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)

# Border
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.penup()
border.goto(-300, 300)
border.pendown()
border.color("aqua")
border.width(5)
for _ in range(2):
    border.forward(600)
    border.right(90)
    border.forward(600)
    border.right(90)

# Snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("pink")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

# Score Display
score_board = turtle.Turtle()
score_board.speed(0)
score_board.shape("square")
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Title
title = turtle.Turtle()
title.speed(0)
title.shape("square")
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 300)
title.write("Snake Game", align="center", font=("Courier", 36, "bold"))

# Movement
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    directions = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}
    if head.direction in directions:
        head.setx(head.xcor() + directions[head.direction][0])
        head.sety(head.ycor() + directions[head.direction][1])

win.listen()
win.onkeypress(move_up, "w")
win.onkeypress(move_down, "s")
win.onkeypress(move_left, "a")
win.onkeypress(move_right, "d")

# Main Game loop along with Collisions and Movement
squares = []
while True:
    win.update()
    
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for square in squares:
            square.goto(1000, 1000)
        squares.clear()
        score = 0
        score_board.clear()
        score_board.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_square = turtle.Turtle()
        new_square.speed(0)
        new_square.shape("square")
        new_square.color("grey")
        new_square.penup()
        squares.append(new_square)
        score += 1
        high_score = max(high_score, score)
        score_board.clear()
        score_board.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    for i in range(len(squares) - 1, 0, -1):
        squares[i].goto(squares[i-1].xcor(), squares[i-1].ycor())

    if squares:
        squares[0].goto(head.xcor(), head.ycor())

    move()

    for square in squares:
        if square.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for square in squares:
                square.goto(1000, 1000)
            squares.clear()
            score = 0
            score_board.clear()
            score_board.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
