import turtle as tur

tur.shape('turtle')
tur.color('green')
tur.speed(10)

def f(x):
    for i in range (0, 360):
        tur.left(1)
        tur.forward(2)
        i += 1

def g(x):
    for i in range (0, 360):
        tur.right(1)
        tur.forward(2)
        i += 1

for j in range (0, 3):
    f(j)
    g(j)
    tur.left(60)
    j += 1
