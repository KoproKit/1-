import turtle

turtle.shape('turtle')
i = 0
while i < 10:
    turtle.forward(5 + 10*i)
    turtle.left(90)
    turtle.forward(5 + 10*i)
    turtle.left(90)
    turtle.forward(5 + 10*i)
    turtle.left(90)
    turtle.forward(5 + 10*i)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.pendown()
    i = i + 1
