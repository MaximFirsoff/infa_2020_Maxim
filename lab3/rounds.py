import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
ballsnamber = 5 # namber of balls

# get screen dimensions
screenInfo = pygame.display.Info()

# displey's coordinate
xcoord = screenInfo.current_w - 400
ycoord = screenInfo.current_h - 100

py = [1]*ballsnamber # delta for x moving
px = [1]*ballsnamber # delta for y moving

# angel of fly`s ball
for n in range (ballsnamber):
    px[n] = randint(-10, 10)
    py[n] = randint(-10, 10)

screen = pygame.display.set_mode((xcoord, ycoord))

score = 0 # Score

COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 0, 255), (0, 255, 255)]

r = [0]*ballsnamber # radius for each ball
x = [0]*ballsnamber # x for each ball
y = [0]*ballsnamber # y for each ball
color = [0]*ballsnamber # color for each ball


def new_ball(cx):
    '''рисует новый шарик '''
    global x, y, r, color
    r[cx] = randint(5, 50)
    x[cx] = randint(r[cx], xcoord-r[cx])
    y[cx] = randint(r[cx], ycoord-r[cx])
    color[cx] = COLORS[randint(0, 5)]
    circle(screen, color[cx], (x[cx], y[cx]), r[cx])

def click(event):
    global score
    print(x, y, r)
    for cx in range(ballsnamber):
        if abs(x[cx] - event.pos[0]) < r[cx] and abs(y[cx] - event.pos[1]) < r[cx]:
            print("Ooopsssss")
            score += int(1/r[cx]*100*(x[cx]+y[cx]))
            new_ball(cx)

clock = pygame.time.Clock()
finished = False

# generating of balls
for cx in range(ballsnamber):
    new_ball(cx)

while not finished:
    clock.tick(FPS + 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    for cx in range(ballsnamber):
        circle(screen, color[cx], (x[cx], y[cx]), r[cx])
        x[cx] += px[cx]
        y[cx] += py[cx]
        if abs(x[cx]) - r[cx] < 0 or x[cx] + r[cx] > xcoord: # if our ball is near the wall
            px[cx] *= -1
        if abs(y[cx]) - r[cx] < 0 or y[cx] + r[cx] > ycoord: # if our ball is near the wall
            py[cx] *= -1

    # for Score displaied
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Score: " + str(score), 0, (180, 120, 120))
    screen.blit(text1, (10, 50))

    pygame.display.update()
    screen.fill("BLACK")

pygame.quit()
