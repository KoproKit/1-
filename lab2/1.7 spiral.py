import turtle

turtle.shape('turtle')
n = 0
while n < 10000:
    turtle.forward((n**2+1)**(1/2)*(1/1000))
    turtle.left(1)
    n = n + 1
