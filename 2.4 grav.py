import turtle as tur
tur.shape('turtle')

x = 0
y = 0
dt = 0.1
t = 0
Vx = 10
Vy = 50
ay = -9.81

while t < 500:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy = ay*dt + Vy
    tur.goto(x, y)
    t = t + dt
    if y < 0:
        Vy = -Vy
    


