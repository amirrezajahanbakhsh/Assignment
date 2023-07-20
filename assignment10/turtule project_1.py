import turtle
x = turtle.Screen()
turtle.speed(70)

for i in range(40):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()