import turtle

t = turtle.Turtle()

# turtle.setup(1280, 960)
# turtle.screensize(400, 300)
t.speed("slow")
t.shape("turtle")
t.turtlesize(2)
t.color("green")
t.pencolor("blue")
t.screen.bgcolor("aqua")

for j in range(8):
    for i in range(4):
        t.forward(200)
        t.left(90)

    t.left(45)


turtle.done()
