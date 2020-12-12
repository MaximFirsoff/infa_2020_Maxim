import math
import turtle

#  Начальное положение шарика
turtle.shape("circle")
turtle.speed("slowest")
turtle.shapesize(0.5, 0.5, 1)
coords = turtle.home()

turtle.goto(300, 0)
turtle.goto(-300, 0)

x = y = 0
Vx = 1000
while Vx > 50:
    # noinspection PyBroadException
    try:
        Vx = int(input("Введите силу броска (не более 50) - "))
    except:
        print("Значение должно быть числом")
Ugl = 91 
while Ugl > 90 or Ugl < 0:
    try:
        Ugl = int(input("Введите угол броска (в диапазоне от 0 до 90 градусов) - "))
    except:
        print("Значение должно быть числом")
Ugl = Ugl*math.pi/180

while Vx > 2:
    px = y = 0
    while y >= 0:
        turtle.goto(x*2-300, y*5)
        px += 1
        x += 1        
        y = px*math.tan(Ugl) - (9.8*px**2)/(2*Vx**2*math.cos(Ugl)*math.cos(Ugl))
    Vx /= 1.2
