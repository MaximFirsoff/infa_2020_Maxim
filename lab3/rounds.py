import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
ballsnumber = 5  # number of balls

# get screen dimensions
screenInfo = pygame.display.Info()

# display's coordinate
xcoord = screenInfo.current_w - 400
ycoord = screenInfo.current_h - 100

py = [1] * ballsnumber  # delta for x moving
px = [1] * ballsnumber  # delta for y moving

# angel of fly`s ball
for n in range(ballsnumber):
    px[n] = randint(-10, 10)
    py[n] = randint(-10, 10)

screen = pygame.display.set_mode((xcoord, ycoord))

score = 0  # Score

COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 0, 255), (0, 255, 255)]

r = [0] * ballsnumber  # radius for each ball
x = [0] * ballsnumber  # x for each ball
y = [0] * ballsnumber  # y for each ball
color = [0] * ballsnumber  # color for each ball


def new_ball(cx):
    """рисует новый шарик """
    global x, y, r, color
    r[cx] = randint(5, 50)
    x[cx] = randint(r[cx], xcoord - r[cx])
    y[cx] = randint(r[cx], ycoord - r[cx])
    color[cx] = COLORS[randint(0, 5)]
    circle(screen, color[cx], (x[cx], y[cx]), r[cx])


def click(event):
    global score
    for cx in range(ballsnumber):
        if abs(x[cx] - event.pos[0]) < r[cx] and abs(y[cx] - event.pos[1]) < r[cx]:

            score += int(1 / r[cx] * 100 * (x[cx] + y[cx]))
            new_ball(cx)
        else:
            score -= 410



def filescore(score):
    fileline = []
    with open('ballscore.txt') as file:
        for line in file:
            fileline.append(line.split(" "))
        fileline.append([score, 'YOU,\n'])
        fileline.sort(key=lambda x: int(x[0]))

    filescore = open('ballscore.txt', "w")
    print(fileline, file = filescore)
    filescore.close()


clock = pygame.time.Clock()
finished = False

# generating of balls
for cx in range(ballsnumber):
    new_ball(cx)

while not finished:
    clock.tick(FPS + 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            filescore(score)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    for cx in range(ballsnumber):
        circle(screen, color[cx], (x[cx], y[cx]), r[cx])
        x[cx] += px[cx]
        y[cx] += py[cx]
        if abs(x[cx]) - r[cx] < 0 or x[cx] + r[cx] > xcoord:  # if our ball is near the wall
            px[cx] *= -1
        if abs(y[cx]) - r[cx] < 0 or y[cx] + r[cx] > ycoord:  # if our ball is near the wall
            py[cx] *= -1

    # for Score displayed
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Score: " + str(score), True, (180, 120, 120))
    screen.blit(text1, (10, 50))

    pygame.display.update()
    screen.fill("BLACK")

pygame.quit()
