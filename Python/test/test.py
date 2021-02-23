import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(-200, 0)
turtle.pendown()

axiom = "F"
tempAx = ""
iterable = 4

logic = {
    'F': 'F+F−F−F+F'
}

for i in range(iterable):
    for j in axiom:
        if j in logic:
            tempAx += logic[j]
            print(tempAx)
        else:
            tempAx += j
    axiom, tempAx = tempAx, ''

for k in axiom:
    if k == '+':
        turtle.right(-90)
    elif k == '−':
        turtle.left(-90)
    else:
        turtle.forward(5)

turtle.update()
turtle.mainloop()

