import pygame
from pygame.draw import *
from pygame import gfxdraw

pygame.init()


def clouds_draw(cloudscolor, cloudskoordinate):
    """
    Clouds drawing
    :rtype: object
    :param cloudscolor: The color of cloud
    :param cloudskoordinate: The x, y of cloud
    :return:
    """
    gfxdraw.aaellipse(screen, cloudskoordinate[0] + 225, cloudskoordinate[1] + 35, 225, 35, cloudscolor)
    gfxdraw.filled_ellipse(screen, cloudskoordinate[0] + 225, cloudskoordinate[1] + 35, 225, 35, cloudscolor)

def spaseship(xcord, ycord):
    """
    drawing of spaceship
    :param xcord: x of surface of left top corner
    :param ycord: y of surface of left top corner
    :return: none
    """
    # Light of spaceship
    spaceship_light = pygame.Surface((190, 170), pygame.SRCALPHA)
    spaceship_light.set_alpha(128)
    gfxdraw.aatrigon(spaceship_light, 0, 168, 184, 170, 95, -20, (255, 255, 255)) # Light from spaceship
    gfxdraw.filled_trigon(spaceship_light, 0, 168, 184, 170, 95, -20, (255, 255, 255))
    screen.blit(spaceship_light, (xcord+5, ycord+60))

    # spaceship 5 200
    spaceship = pygame.Surface((200, 75), pygame.SRCALPHA)
    ellipse(spaceship, (153, 153, 153), (0, 5, 200, 70))
    ellipse(spaceship, (204, 204, 204), (25, 0, 150, 50))

    x = (7, 33, 67, 170, 142, 105)  # illuminators
    y = (34, 50, 58, 34, 50, 58)
    for el in range(6):
        ellipse(spaceship, "white", (x[el], y[el], 25, 10))
    screen.blit(spaceship, (xcord, ycord))


def green_man(xcord, ycord):
    """
    Drawing Green Man from UFO
    :param xcord: x of surface of left top corner
    :param ycord: x of surface of left top corner
    :return:
    """
    greenman = pygame.Surface((115, 190), pygame.SRCALPHA)
    aliencolor = (221, 233, 175) # color of alien

    # head
    circle(greenman, aliencolor, (20, 47), 5)
    circle(greenman, aliencolor, (70, 45), 5)
    gfxdraw.aapolygon(greenman, [(15, 49), (35, 80), (52, 83), (73, 47), (65, 40), (22, 42)], aliencolor)
    gfxdraw.filled_polygon(greenman, [(15, 49), (35, 80), (52, 83), (73, 47), (65, 40), (22, 43)], aliencolor)
    circle(greenman, (221, 233, 175), (45, 77), 10)

    # eyes
    circle(greenman, "black", (35, 57), 9)
    circle(greenman, "black", (57, 58), 7)
    circle(greenman, "white", (37, 58), 3)
    circle(greenman, "white", (60, 60), 2)

    ellipse(greenman, aliencolor, (25, 87, 33, 67)) # body of alien

    # left cuticula
    circle(greenman, aliencolor, (8, 7), 7)
    ellipse(greenman, aliencolor, (3, 13, 12, 7))
    circle(greenman, aliencolor, (15, 25), 5)
    ellipse(greenman, aliencolor, (17, 30, 6, 10))

    # right cuticula
    ellipse(greenman, aliencolor, (100, 15, 13, 16))
    ellipse(greenman, aliencolor, (87, 15, 10, 8))
    circle(greenman, aliencolor, (80, 25), 5)
    ellipse(greenman, aliencolor, (73, 29, 6, 7))
    circle(greenman, aliencolor, (73, 38), 5)

    # left hand
    circle(greenman, aliencolor, (24, 97), 9)
    ellipse(greenman, aliencolor, (10, 103, 14, 10))
    ellipse(greenman, aliencolor, (3, 113, 8, 10))

    # right hand
    circle(greenman, aliencolor, (58, 100), 10)
    ellipse(greenman, aliencolor, (60, 100, 15, 13))
    ellipse(greenman, aliencolor, (74, 106, 20, 10))

    # left leg
    ellipse(greenman, aliencolor, (15, 129, 17, 25))
    ellipse(greenman, aliencolor, (12, 150, 13, 27))
    circle(greenman, aliencolor, (7, 173), 8)

    # right leg
    ellipse(greenman, aliencolor, (44, 138, 17, 25))
    ellipse(greenman, aliencolor, (49, 158, 13, 27))
    circle(greenman, aliencolor, (66, 181), 8)



    screen.blit(greenman, (xcord, ycord))


FPS = 30
screen = pygame.display.set_mode((450, 620))
screen.fill((0, 34, 43))  # background
rect(screen, (34, 43, 0), (0, 320, 450, 320))  # ground
circle(screen, "white", (300, 150), 70)  # moon
line(screen, (46, 69, 68), (0, 320), (450, 320))  # Line between ground and sky

clouds_draw((102, 102, 102), (-225, 15))
clouds_draw((102, 102, 102), (-250, 45))
clouds_draw((102, 102, 102), (320, -15))
clouds_draw((102, 102, 102), (200, 80))
clouds_draw((102, 102, 102), (-120, 150))
clouds_draw((102, 102, 102), (150, 170))

clouds_draw((51, 51, 51), (80, 47))
clouds_draw((51, 51, 51), (-250, 125))
clouds_draw((51, 51, 51), (75, 220))

spaseship(5, 200)

green_man(270, 345)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
