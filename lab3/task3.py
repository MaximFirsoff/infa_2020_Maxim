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
polygon(spaceship_light, (255, 255, 255), [(0, 170), (170, 170), (95, 0)])  # Light from spaceship
screen.blit(spaceship_light, (10, 240))

#spaceship
ellipse(screen, (153, 153, 153), (5, 200, 200, 70))
ellipse(screen, (204, 204, 204), (30, 195, 150, 50))

x = (12, 35, 68, 175, 152, 119) # illuminators
y = (230, 245, 252, 230, 245, 252)
for el in range(6):
    ellipse(screen, "white", (x[el], y[el], 25, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
