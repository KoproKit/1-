import turtle

turtle.shape('turtle')
n = 0
while n < 50:
    turtle.forward(5 + 5*n)
    turtle.left(90)
    n = n + 1
