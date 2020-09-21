tur.color('green')
tur.speed(10)

def f(x):
    for i in range (0, 360):
        tur.left(1)
        tur.forward(x)
        i += 1

def g(x):
    for i in range (0, 360):
        tur.right(1)
        tur.forward(x)
        i += 1

a = 0.5
tur.left(90)
for j in range (0, 8):
    a += 0.25
    f(a)
    g(a)
    j += 1
