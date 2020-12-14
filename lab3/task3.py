import pygame
from pygame.draw import *

pygame.init()

def clouds_draw(cloudscolor, cloudskoordinate):
    """
    Clouds drawing
    :rtype: object
    :param cloudscolor: The color of cloud
    :param cloudskoordinate: The x, y of cloud
    :return:
    """
    ellipse(screen, cloudscolor, (cloudskoordinate[0], cloudskoordinate[1], 450, 70))

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


spaceship_light = pygame.Surface((170, 170), pygame.SRCALPHA)
spaceship_light.set_alpha(128)
polygon(spaceship_light, (255, 255, 255), [(0, 170), (170, 170), (85, 0)])  # Light from spaceship
screen.blit(spaceship_light, (10, 240))

ellipse(screen, (153, 153, 153), (5, 200, 200, 70))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
