import turtle as tur

tur.shape('turtle')
tur.color('blue')

print ('Введите n:')
n = int (input())
y = 180/n
a = 350

tur.left(180 - y/2)
for i in range (0, n):
    tur.forward (a)
    tur.left (180 - y)
