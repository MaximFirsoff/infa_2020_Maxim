import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

green = (0, 250, 40)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
leafgreen = (100,190,80)

# И создать окно:
screen = pygame.display.set_mode((500, 700))
screen.fill([20,105,20])

polygon(screen, (5,25,100),[(0,0),(0,400),(500,400),(500,0)])
#0 layout
circle(screen,(250,240,246),(280,170),70)
# 1 layout
ellipse(screen, (50,55,50),(340, -30, 800, 90))
ellipse(screen, (50,55,50),(-200, 30, 500, 120))
ellipse(screen, (50,55,50),(200, 100, 500, 90))
ellipse(screen, (50,55,50),(-110, 190, 400, 80))
ellipse(screen, (50,55,50),(200, 200, 470, 100))
#2 layout
ellipse(screen, (20,35,30),(130, 50, 500, 80))
ellipse(screen, (20,35,30),(-100, 140, 300, 90))
ellipse(screen, (20,35,30),(130, 270, 500, 80))
#3 layout
x = 250
y = 370
size =100
#polygon(screen, (20 + 50, 105 + 50, 20 + 50),
#        [(x - size * 2.5 / 2, y - size / 2), (x - size + 17, 450), (x + size + 140, 450)])
#polygon(screen, (5 + 50, 25 + 50, 100 + 50), [(x - size * 2.5 / 2, y - size / 2), (x - size, 400), (x + size, 400)])
def ufo(size,x,y):
    surf01 = pygame.Surface((size*3, size), pygame.SRCALPHA)
    polygon(surf01, (255,255,255,127), ((size*0.75, 0), (size*1.5, size*1.5), (0, 1.5*size)))
    surf01.set_alpha(0)
    screen.blit(surf01, (x - size * 2, y - size / 2))
    ellipse(screen,(140,180,190),(x-size*2.5,y-size,size*2.5,size))
    ellipse(screen,(200,210,250),(x-size*2.5+size*2.5/5,y-size-4,size*2.5*3/5,size/1.5))
    ellipse(screen,(230,230,230),(x-size*2.5*0.95,y-size/2,size*2.5/10,size/10))
    ellipse(screen,(230,230,230),(x-size*2.5*0.95+size*2,y-size/2,size*2.5/10,size/10))
    ellipse(screen,(230,230,230),(x-size*2.5*0.79,y-size/2+size*0.2,size*2.5/10,size/10))
    ellipse(screen,(230,230,230),(x-size*2.5*0.79+size*1.1,y-size/2+size*0.2,size*2.5/10,size/10))
    ellipse(screen,(230,230,230),(x-size*2.5*0.65,y-size/2+size*0.25,size*2.5/10,size/10))
    ellipse(screen,(230,230,230),(x-size*2.5*0.55+size*0.15,y-size/2+size*0.25,size*2.5/10,size/10))
ufo(100,250,370)

def alien(size,x1,y1):
    ellipse(screen, green,(x1,y1,size/2.5,size))
    circle(screen,green,(int(x1+size/2.5),int(y1+size/10)),int(size/9))
    circle(screen,green,(int(x1),int(y1+size/10)),int(size/9))
    ellipse(screen, green, (x1+size/20+size/2.5,y1+size/8,size/5,size/8))
    ellipse(screen, green, (x1 + size / 5 + size / 2.5, y1 + size / 6, size / 8, size / 10))
    circle(screen,red,(int(x1+size/5+size/1.8),int(y1+size/5.9)),int(size/11))
    ellipse(screen,green,(x1-size/6,y1+size/5.65,size/7,size/11))
    ellipse(screen,green,(x1-size/5.1,y1+size/3.8,size/13,size/10))
    surf0= pygame.Surface((size/7.5, size/7.5), pygame.SRCALPHA)
    ellipse(surf0, leafgreen,(0,0,size/15,size/22.5))
    surf0 = pygame.transform.rotate(surf0,110)
    screen.blit(surf0, (x1+size/7.2+size/1.8,y1+size/6-size/3.9))
    line(screen, black, [int(x1+size/5+size/1.8),int(y1+size/5.9-size/11)],[int(x1+size/5+size/1.8)+size/15,int(y1+size/5.9 -size/11)-size/15])
    ellipse(screen,green,(x1,y1+size/1.3,size/7,size/4))
    ellipse(screen,green,(x1+size/3.8,y1+size/1.18,size/7,size/4))
    ellipse(screen,green,(x1-size/20,y1+size/1.08,size/9,size/3.8))
    ellipse(screen, green, (x1 +size / 3.1, y1 + size *(1.05), size / 9, size / 3.8))
    ellipse(screen,green,(x1-size/9,y1+size*(1.1),size/8,size/8))
    ellipse(screen,green,(x1+size/2.7,y1+size*(1.2),size/7.5,size/7.5))
    ellipse(screen, green, (x1+size/2.5,y1-size/2.3,size/9,size/9))
    ellipse(screen, green, (x1+size/2.2,y1-size/1.91,size/15,size/6))
    ellipse(screen, green, (x1+size/2.01,y1-size/1.7,size/11,size/11))
    ellipse(screen, green, (x1+size/1.75,y1-size/1.5,size/9,size/11))
    ellipse(screen, green, (x1+size/1.55,y1-size/1.56,size/7,size/5))
    ellipse(screen, green, (x1-size/13,y1-size/1.95,size/14,size/10))
    ellipse(screen, green, (x1 - size / 10, y1 - size / 1.62, size / 11, size / 10))
    ellipse(screen, green, (x1 - size / 7.5, y1 - size / 1.42, size / 8, size / 15))
    ellipse(screen, green, (x1 - size / 7, y1 - size / 1.22, size / 7, size / 8))





    surf1 = pygame.Surface((size/1.5, size/1.5), pygame.SRCALPHA)
    # surf2 = pygame.Surface((50, 50), pygame.SRCALPHA)
    ellipse(surf1, green, (10, 10, size/5, size/2))
    # ellipse(surf2, black, (10, 10, 20, 20))
    surf2 = pygame.Surface((size/1.5,size/1.5), pygame.SRCALPHA)
    ellipse(surf2, green, (10, 10, size / 5, size / 2))
    surf3 = pygame.transform.rotate(surf1, -30)
    # surf4 = pygame.transform.rotate(surf2, 0)
    surf4 = pygame.transform.rotate(surf1, 30)
    surf5 = pygame.transform.rotate(surf1,98)
    surf6 = pygame.transform.rotate(surf2,55)
    # surf3.blit(surf4, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(surf3, (x1, y1-size/2))
    screen.blit(surf4, (x1-size/4, y1 - size/1.4 ))
    screen.blit(surf5, (x1-size/6,y1-size/1.2))
    screen.blit(surf6, (x1 - size / 4.4, y1 - size / 1.19))
    circle(screen,green,(int(x1+size/6),int(y1-size/8)),int(10))


    circle(screen, black, (int(x1 + size / 3), int(y1 - size / 6)), int(size / 15))
    circle(screen, black, (int(x1 + size / 8), int(y1 - size / 6)), int(size / 11))
    circle(screen, white, (int(x1 + size / 8 + size / 25), int(y1 - size / 7)), int(size / 40))
    circle(screen, white, (int(x1 + size / 2.8), int(y1 - size / 7)), int(size / 45))
alien(150,350,400)
















pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()