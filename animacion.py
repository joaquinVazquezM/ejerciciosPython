import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red",
         "blue",
         "yellow",
         "green",
         "orange",
         "purple",
         "white"]

for x in range(500):
    t.pensize(x/1000 + 1)
    t.pencolor(colors[x % 6])
    t.forward(x)
    t.left(59)

t.hideturtle()
turtle.done()