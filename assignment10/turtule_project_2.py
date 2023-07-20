import turtle

x = turtle.Turtle()
x.color("red", "yellow")
x.speed(100)
x.fd(-150)

x.begin_fill()

for i in range(90):
    x.forward(300)
    x.left(170)

x.end_fill()

turtle.mainloop()