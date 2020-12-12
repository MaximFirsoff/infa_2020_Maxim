from random import randint
import numpy as np
import turtle

number_of_turtles = 100
turteletrace = int(number_of_turtles/10)
turtle.tracer(turteletrace)
steps_of_time_number = 100

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(-200, 200)
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)
turtle.hideturtle()

for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.shapesize(0.5, 0.5, 1)
    unit.goto(randint(-190, 190), randint(-190, 190))
    unit.left(randint(0, 360))

while True:
    for i in range(steps_of_time_number):
        for unit in pool:
            if abs(unit.xcor()) > 194.0:
                turtle.tracer(5)
                unit.left(180-2*unit.heading())
                turtle.tracer(turteletrace)
                unit.forward(2)

            if abs(unit.ycor()) > 194.0:
                turtle.tracer(5)
                unit.left(360-2*unit.heading())
                turtle.tracer(turteletrace)
                unit.forward(2)
                
            for unit2 in pool:
                if unit != unit2 and unit2.xcor() - 10 < unit.xcor() < unit2.xcor() + 10:
                    if unit2.ycor()-10 < unit.ycor() < unit2.ycor()+10:
                        turtle.tracer(5)
                        unit.left(180-2*unit.heading())
                        unit2.left(360-2*unit2.heading())
                        turtle.tracer(turteletrace)
            unit.forward(1)
