import turtle
import random

t = turtle.Turtle()
t.pensize(30)
t.shape("turtle")
t.color("green")
t.speed(5)
colors =["red", "orange", "yellow", "green", "blue", "purple", "grey", "black"]
while True:
    t.color(random.choice(colors))
    t.forward(random.randint(0, 360))
    t.left(random.randint(0, 360))
    t.right(random.randint(0, 360))
    t.backward(random.randint(0, 360))
turtle.done