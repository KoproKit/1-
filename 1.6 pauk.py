import turtle

turtle.shape('turtle')
n = 12
i=0
while i < n:
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(360/n)
    turtle.left(180)
    i = i + 1
