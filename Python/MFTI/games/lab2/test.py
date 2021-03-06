import turtle
from random import *
import pygame 

#turtle.shape('turtle')
#turtle.speed(0)

def SqareSpin():
    for i in range(10):
        turtle.forward(50 + i*8)
        turtle.left(90)
        turtle.forward(50 + i*8)
        turtle.left(90)
        turtle.forward(25 + i*8)

        
def Sqare():
    for i in range(10):
        turtle.penup()
        turtle.goto(10 - i*4, 10 - i*4)
        turtle.pendown()
        for a in range(4):
            turtle.forward(50 + i*8)
            turtle.left(90)
        
          
def Spider():
    for i in range(12):
        turtle.goto(1, 1)
        turtle.left(360/12)
        turtle.forward(50)
        turtle.backward(50)

        
def Spin(): 
    for a in range(1, 360, 1):
        turtle.forward(1)
        turtle.left(1 + 360/a)

        
def Round(step, angle, duga=1):
    line = int(360/abs(angle)/duga)
    for a in range(line):
        turtle.forward(step)
        turtle.left(angle)

        
def Angle():
    turtle.penup()
    turtle.goto(10, 10)
    turtle.pendown()
    for a in range(3, 8, 1):
        turtle.penup()
        turtle.goto(10 + a*10, 10)
        turtle.setheading(25 + a)
        turtle.pendown()

        for i in range(1, a + 1, 1):   
            turtle.left(360/a)
            turtle.forward(20 + a*10)


def Flower():
    for i in range(3):
        Round(1,1)
        Round(1,-1)
        turtle.left(60)


def Buterf():        
    for i in range(5, 1, -1):
        Round(1,i)
        Round(1,-i)


def Arcangle(step, angle):
    line = int(360/abs(angle)/2)
    for a in range(line):
        turtle.forward(step)
        turtle.left(angle)


def Spin():
    t = (1,1),(1,20)
    for step, angle in 5*t:
        Arcangle (step, angle)


def  Smile():
    turtle.color("black", "yellow")
    turtle.begin_fill()
    Round(1, 0.6)
    #turtle.circle(100)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-40, 120)
    turtle.pendown()

    turtle.color("black", "blue")
    turtle.begin_fill()
    Round(1, 5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(40, 120)
    turtle.pendown()
    turtle.begin_fill()
    Round(1, 5)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 80)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.pensize(10)
    turtle.forward(30)

    turtle.penup()
    turtle.goto(60, 75)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.left(180)
    Round(1, -1, 2)

def Star511 ():
    a = 9
    for i in range(a):
        turtle.forward(150)
        turtle.left(180-180/a)
    turtle.goto(0, 0)

def Turtrnd():
    a = randint(1, 1000)
    print(a)
    for i in range(a): 
        turtle.forward(randint(0, 30))
        turtle.left(randint(0, 360))


def Zero(a):
    for i in range (2):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a*3)
        turtle.left(90)
"""
# содержимое файла index.txt
L = [(0,0,0,0,0,0,1,1,1),
     (1,0,0,1,1,1,1,1,0),
     (0,1,0,0,1,1,0,1,1),
     (1,1,1,0,1,1,0,0,0),
     (1,0,0,1,0,1,1,0,1),
     (0,0,1,0,0,1,1,0,1),
     (0,0,1,1,1,0,1,0,0),
     (1,1,1,0,1,0,1,1,0),
     (0,0,0,0,0,0,1,0,1),
     (1,1,0,0,0,1,0,0,1)]
"""
with open('index.txt') as L: 
    L = L.readlines()

strin = input("Введите значение индекса - ")
for a in strin:
    ak = tuple(map(float,(L[int(a)].split(","))))
    angle = 90
    turtle.pencolor((ak[0]*1.0, ak[0]*1.0, ak[0]*1.0))
    turtle.forward(17)
    turtle.left(90)
    turtle.pencolor((ak[1]*1.0, ak[1]*1.0, ak[1]*1.0))
    turtle.forward(17)
    turtle.pencolor((ak[2]*1.0, ak[2]*1.0, ak[2]*1.0))
    turtle.forward(17)
    turtle.left(90)
    turtle.pencolor((ak[3]*1.0, ak[3]*1.0, ak[3]*1.0))
    turtle.forward(17)
    turtle.left(90)
    turtle.pencolor((ak[4]*1.0, ak[4]*1.0, ak[4]*1.0))
    turtle.forward(17)
    turtle.pencolor((ak[5]*1.0, ak[5]*1.0, ak[5]*1.0))
    turtle.forward(17)
    turtle.left(135)
    turtle.pencolor((ak[6]*1.0, ak[6]*1.0, ak[6]*1.0))
    turtle.forward(24)
    turtle.left(135)
    turtle.pencolor((ak[7]*1.0, ak[7]*1.0, ak[7]*1.0))
    turtle.forward(17)
    turtle.left(225)
    turtle.pencolor((ak[8]*1.0, ak[8]*1.0, ak[8]*1.0))
    turtle.forward(24)
    turtle.pu()
    turtle.right(135)
    turtle.forward(34)
    turtle.left(90)
    turtle.forward(5)
    turtle.pendown()

Buterf()














