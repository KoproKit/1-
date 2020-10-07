import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

cWhite = (255, 255, 255)
cRed = (255, 0, 0)
cGreen = (0, 255, 0)
cBlue = (0, 0, 255)
cBlack = (0, 0, 0)

cGrey = (50, 50, 50)
cPink = (255, 120, 120)
cIcecream = (150, 0, 0)

cHooman = (240, 240, 30)

def wline (xb, yb, xe, ye, color, width):
    '''
функция рисует отрезок
xb, yb - координаты 1 конца
xe, ye - координаты 2 конца
color - цвет
width - толщина
    '''
    line(screen, color, (xb, yb), (xe, ye), width)
    
def wrect (xLU, yLU, xRD, yRD, color, width):
    '''
функция рисует прямоугольник
xLU, yLU - координаты верхнего левого угла
xRD, yRD - ширина и высота
color - цвет
width - толщина контура (0 - сплошной)
    '''
    rect(screen, color, (xLU, yLU, xRD - xLU, yRD - yLU), width)
    
def wpolygon (xLU, yLU, xLD, yLD, xRD, yRD, xRU, yRU, color, width):
    '''
функция рисует четырехугольник
xLU, yLU - координаты 1
xLD, yLD - координаты 2
xRD, yRD - координаты 3
xRU, yRU - координаты 4
color - цвет
width - толщина контура (0 - сплошной)
    '''
    polygon(screen, color, [(xLU,yLU), (xLD,yLD), (xRD,yRD), (xRU,yRU)], width)
    
def wcircle (x, y, R, color, width):
    '''
функция рисует круг
x, y - координаты центра
R - радиус
color - цвет
width - толщина контура (0 - сплошной)
    '''
    circle(screen, color, (x, y), R, width)

def background (x0_back, y0_back, x_back, y_back, col_ground, col_sky):
    '''
функция рисует фон
x0_back, y0_back - координаты верхнего левого угла
x_back, y_back - ширина и высота фона
col_sky - цвет неба
col_ground - цвет земли
    '''
    wrect(x0_back, y0_back + y_back//2, x_back, y_back, col_sky, 0)
    wrect(x0_back, y0_back, x_back, y_back//2, col_ground, 0)
    pass

def m_legs (x0, y0, l):
    '''
функция рисует ноги парня
x0, y0 - координаты начала первой ноги
l - длина ноги (без ступни)
    '''
    wline(x0, y0, x0, y0 + l, cBlack, 2)
    wline(x0, y0 + l, x0 - int(l/5), y0 + l, cBlack, 2)
    wline(x0 + int(l/5), y0, x0 + int(l/5), y0 + l, cBlack, 2)
    wline(x0 + int(l/5), y0 + l, x0 + int(2*l/5), y0 + l, cBlack, 2)
    pass

def m_arms (x0, y0, l):
    '''
функция рисует руки парня
x0, y0 - координаты начала второй руки
l - длина второй руки
    '''
    wline(x0 , y0, x0, y0 + l, cBlack, 2)
    wline(x0 - int(10*l/7), y0, x0 - int(12*l/7), y0 + l, cBlack, 2)
    pass

def m_body (x0, y0, R):
    '''
функция рисует тело парня
x0, y0 - координаты центра нижнего круга
R - радиус кругов
    '''
    wcircle(x0, y0, R, cGrey, 0)
    wcircle(x0, y0 - int(8*R/5), R, cGrey, 0)
    pass

def m_head (x0, y0, R):
    '''
функция рисует голову парня
x0, y0 - координаты центра головы
R - радиус головы
    '''
    wcircle(x0, y0, R, cHooman, 0)

def guy (x0, y0, R):
    '''
функция рисует парня
x0, y0 - координаты центра головы
R - радиус головы
    '''
    m_legs(x0 - int(R/3), y0 + int(R*14/3), int(11*R/3))
    m_arms(x0 + int(5*R/3), y0 + 2*R, int(7*R/3))
    m_body(x0, y0 + int(14*R/3), int(5*R/3))
    m_head(x0, y0, R)
    pass

def w_legs (x0, y0, l):
    '''
функция рисует ноги девушки
x0, y0 - координаты начала первой ноги
l - длина ноги (без ступни)
    '''
    wline(x0, y0, x0, y0 + l, cBlack, 2)
    wline(x0, y0 + l, x0 - int(2*l/11), y0 + int(12*l/11), cBlack, 2)
    wline(x0 + int(2*l/11), y0, x0 + int(2*l/11), y0 + l, cBlack, 2)
    wline(x0 + int(2*l/11), y0 + l, x0 + int(4*l/11), y0 + int(12*l/11),
          cBlack, 2)
    pass

def w_arms (x0, y0, l):
    '''
функция рисует руки девушки
x0, y0 - координаты начала первой руки
l - длина руки (по оси y)
    '''
    wline(x0, y0, x0 - int(2*l/5), y0 + l, cBlack, 2)
    wline(x0 + int(l/5), y0, x0 + int(3*l/5), y0 + l, cBlack, 2)
    pass

def w_body (x0, y0, h):
    '''
функция рисует тело девушки
x0, y0 - координаты вершины
h - длина тела
    '''
    wpolygon(x0, y0, x0 - int(h/4), y0 + h, x0 + int(h/4), y0 + h, x0, y0,
             cPink, 0)

def w_bashka (x0, y0, R):
    '''
функция рисует башку девушки
x0, y0 - координаты центра башки
R - радиус башки
    '''
    wcircle(x0, y0, R, cHooman, 0)

def defffka (x0, y0, R):
    '''
функция рисует девушку
x0, y0 - координаты центра башки девушки
R - радиус башки
    '''
    w_legs(x0 - int(R/3), y0 + int(R*14/3), int(11*R/3))
    w_arms(x0 - int(R/3), y0 + R, int(10*R/3))
    w_body(x0, y0, int(20*R/3))
    w_bashka(x0, y0, R)
    pass

def ice (x0, y0, R):
    '''
функция рисует мороженку (грустную)
x0, y0 - координаты шарика мороженки (грустной)
R - радиус шарика мороженки (грустной)
    '''
    wpolygon(x0 + int(3*R/2), y0 + 4*R, x0 - int(R/2), y0 + R, x0 + int(R/2),
             y0 - 4*R, x0 + int(3*R/2), y0 + 4*R, cIcecream, 0)
    wcircle(x0, y0, R, cRed, 0)
    pass

def baloon (x0, y0, R):
    '''
функция рисует шарик
x0, y0 - координаты первого полупопия
R - радиус полупопий
    '''
    wline(x0 - 2*R, y0 + 18*R, x0 + R, y0 + 4*R, cWhite, 2)
    wpolygon(x0 + R, y0 + 4*R, x0 - R, y0, x0 + 3*R, y0, x0 + R, y0 + 4*R, cRed,
             0)
    wcircle(x0, y0, R, cRed, 0)
    wcircle(x0 + 2*R, y0, R, cRed, 0)

background(0, 0, 400, 400, cBlue, cGreen)
guy(150, 100, 30)
defffka (250, 100, 30)
ice(70, 190, 10)
baloon(310, 60, 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
