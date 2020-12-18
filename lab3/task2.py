import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill("gray")  # background

circle(screen, "yellow", (200, 175), 100)  # face
circle(screen, "black", (200, 175), 100, 1)  # countor
circle(screen, "black", (160, 150), 21)  # pupil
circle(screen, "black", (240, 150), 16)  # pupil
circle(screen, "red", (160, 150), 20, 10)  # eye
circle(screen, "red", (240, 150), 15, 6)  # eye
arc(screen, "black", [130, 110, 60, 100], 0, 3.14, 5)  # brow
arc(screen, "black", [210, 120, 60, 80], -0.5, 2.9, 5)  # brow
rect(screen, (255, 255, 255), (200, 210, 10, 15))  # tooth
polygon(screen, "black", [(150, 220), (240, 200), (230, 240)], 5)  # month

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
