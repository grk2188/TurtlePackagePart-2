import random
from turtle import Turtle, Screen


t = Turtle()
screen = Screen()
#t.colormode(255)
colors = ["gold", "darkolivegreen", "red", "indigo", "coral", "yellow", "blue", "orange"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

directions = [0, 90, 100, 270]
t.pensize(15)
t.speed("slow")

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))

screen.exitonclick()

