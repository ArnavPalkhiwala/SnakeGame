import turtle
import time
import random

delay = 0.1

score = 0

high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=1000, height=1000)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("orange")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 450)
pen.write("Current Score: 0        High Score: 0", align="center", font=("Gill Sans", 24, "normal"))


def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def left():
    if head.direction != "right":
        head.direction = "left"


def right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")

while True:
    wn.update()

    if head.xcor() > 490 or head.xcor() < -490 or head.ycor() > 490 or head.ycor() < -490:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for seg in segments:
            seg.goto(1000, 1000)

        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Current Score: {}        High Score: {}".format(score, high_score), align="center", \
                  font=("Gill Sans", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-490, 490)
        y = random.randint(-490, 490)
        food.goto(x, y)
        newSeg = turtle.Turtle()
        newSeg.shape('square')
        newSeg.color("black")
        newSeg.penup()
        segments.append(newSeg)

        delay -= 0.001

        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Current Score: {}        High Score: {}".format(score, high_score), align="center", \
                  font=("Gill Sans", 24, "normal"))

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Current Score: {}        High Score: {}".format(score, high_score), align="center", \
                      font=("Gill Sans", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
