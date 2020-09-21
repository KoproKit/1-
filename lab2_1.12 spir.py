import turtle as tur

tur.shape('turtle')
tur.color('green')
tur.speed(10)

def f(x):
    if x>0.5 :
        for i in range (0, 180):
            tur.right(1)
            tur.forward(x)
        i += 1
    else:
        for i in range (0, 180, 2):
            tur.right(2)
            tur.forward(x)
        i += 1

a = 1
b = 0.3
tur.penup()
tur.goto(-300, 0)
tur.pendown()
tur.left(90)
for j in range (0, 5):
    f(a)
    f(b)
    j += 1
f(a)
