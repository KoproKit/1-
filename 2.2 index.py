import turtle as tur
tur.shape('turtle')

def num(n):
    if n == 0:
        tur.forward(50)
        tur.left(90)
        tur.forward(100)
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(100)
        tur.left(90)
        tur.penup()
        tur.forward(60)
        tur.pendown()
        
    if n == 1:
        tur.penup()
        tur.forward(50)
        tur.left(90)
        tur.pendown()
        tur.forward(100)
        tur.left(135)
        tur.forward(70.71)
        tur.left(45)
        tur.penup()
        tur.forward(50)
        tur.left(90)
        tur.forward(60)
        tur.pendown()
        
    if n == 4:
        tur.penup()
        tur.forward(50)
        tur.left(90)
        tur.pendown()
        tur.forward(100)
        tur.left(180)
        tur.forward(50)
        tur.right(90)
        tur.forward(50)
        tur.right(90)
        tur.forward(50)
        tur.left(180)
        tur.penup()
        tur.forward(100)
        tur.left(90)
        tur.forward(60)
        tur.pendown()

    if n == 7:
        tur.left(90)
        tur.forward(50)
        tur.left(45)
        tur.right(90)
        tur.forward(70.71)
        tur.right(225)
        tur.forward(50)
        tur.penup()
        tur.left(90)
        tur.forward(100)
        tur.left(90)
        tur.forward(60)
        tur.pendown()

A = [1, 4, 1, 7, 0, 0]

num(A[0])
num(A[1])
num(A[2])
num(A[3])
num(A[4])
num(A[5])

    

