import turtle as tur
import numpy as np

tur.shape('turtle')

def mnug(n):
    m = (n-2)/n*180
    tur.left(180 - m/2)
    for i in range (1, n):
        tur.forward(b)
        tur.left(180 - m)
    tur.forward(b)
    tur.right(m/2)

n = 3
a = 15

for j in range (0, 10):
    r = a*(n-2)
    b = 2*r*np.sin(np.pi/n)
    mnug(n)
    tur.penup()
    tur.goto(a*(n-2), 0)
    tur.pendown()
    n += 1
    j += 1
