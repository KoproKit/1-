from random import *
import turtle

turtle.shape('turtle')
n = 0
while n < 100:
    turtle.forward(randint(0, 50))
    turtle.left(randint(0, 360))
    n = n + 1
