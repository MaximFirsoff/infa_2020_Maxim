import pygame
from pygame.draw import *
from pygame.transform import *
import numpy as np

pygame.init()


def layer_1():
    mntn = [[0, 330]]
    for i in range(10, 240):
        a = 280-(i-10)**2/400
        mntn.append([i, a])
    mntn.append([290, 130])
    mntn.append([310, 170])
    mntn.append([430, 250])
    mntn.append([500, 240])
    mntn.append([540, 270])
    mntn.append([590, 200])
    mntn.append([650, 220])
    for i in range(680, 800):
        a = 190 + (i-680)*(i-700)*(i-830)/4000
        mntn.append([i, a])
    mntn.append([860, 170])
    for i in range(900, 970):
        a = 160 + (i-900)**2/200
        mntn.append([i, a])
    mntn.append([1000, 180])
    mntn.append([1050, 213])

    polygon(screen, (252, 152, 49), mntn)


def layer_2():
    mntn = [[0, 470], [0, 350], [10, 350]]
    for i in range(35, 230):
        a = 370 + (i-35)*(i-200)/70
        mntn.append([i, a])
    mntn.append([280, 370])
    mntn.append([350, 420])
    mntn.append([390, 320])
    mntn.append([490, 350])
    mntn.append([560, 420])
    for i in range(650, 900):
        a = 400 + 450*((650/i)**12 - (650/i)**6)
        mntn.append([i, a])
    mntn.append([950, 280])
    mntn.append([1020, 295])
    mntn.append([1050, 230])
    mntn.append([1050, 450])

    polygon(screen, (172, 67, 52), mntn)


def layer_3():
    mntn = [[0, 700], [0, 340], [150, 380]]
    for i in range(250, 500):
        a = 530 - (i - 250)*(i - 650)/250
        mntn.append([i, a])
    mntn.append([650, 600])
    for i in range(700, 1050):
        a = 620 + (i - 700)*(i - 850)*(i - 1200)/50000
        mntn.append([i, a])
    mntn.append([1050, 700])

    polygon(screen, (48,  16, 38), mntn)


def bird(x, y, k):
    k /= 50
    scr = pygame.Surface([100*k, 150*k], pygame.SRCALPHA)
    brd = []
    for i in np.arange(0, 28*k):
        a = 20*k * (np.tan((i/k - 6*np.pi + 5)/12)**2)
        brd.append([i, a])
    for i in np.arange(28*k, 100*k):
        a = k * (102 + i/k*(i/k-50)/100)
        brd.append([i, a])

    polygon(scr, (66, 33, 11), brd)
    screen.blit(rotate(scr, 60), [x, y])


FPS = 30
screen = pygame.display.set_mode((1050, 700))
screen.fill((255, 207, 171))

# background
rect(screen, (254, 213, 196), (0, 150, 1050, 150))
rect(screen, (179, 134, 148), (0, 450, 1050, 250))

# sun
circle(screen, (252, 238, 33), (525, 140), 70)

# mountains
layer_1()
layer_2()
layer_3()

# birds
bird(500, 200, 20)
bird(400, 180, 20)
bird(500, 230, 20)
bird(420, 250, 20)

bird(750, 500, 40)
bird(800, 490, 20)
bird(670, 500, 20)
bird(610, 410, 25)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
