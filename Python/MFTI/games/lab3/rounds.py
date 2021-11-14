try:  # control exist of pygame module
    import pygame
    from pygame.draw import *
except ImportError:
    print("This program requires pygame!")
    print("Please press Win+R enter 'pip install pygame' and install it")
    print("before running this program.")
    exit(1)

try:  # control exist of random module
    from random import randint
except ImportError:
    print("This program requires random")
    print("Please press Win+R enter 'pip install random' and install it")
    print("before running this program.")
    exit(1)

try:  # control exist of urllib module
    import requests
except ImportError:
    print("This program requires requests")
    print("Please press Win+R enter 'pip install requests' and install it")
    print("before running this program.")
    exit(1)

try:  # check file if no images
    f = open('trusy2.bmp')
    f.close()
    f = open('trusy-emporio-armani-siniy-545498-1.bmp')
    f.close()
except IOError:
	r = requests.get('https://github.com/MaximFirsoff/infa_2020_Maxim/raw/main/Python/MFTI/games/lab3/trusy-emporio-armani-siniy-545498-1.bmp')
	with open('trusy-emporio-armani-siniy-545498-1.bmp','wb') as f:
  		f.write(r.content)
	r = requests.get('https://github.com/MaximFirsoff/infa_2020_Maxim/raw/main/Python/MFTI/games/lab3/trusy2.bmp')
	with open('trusy2.bmp','wb') as f:
  		f.write(r.content)
#    urllib.request.urlretrieve("https://github.com/MaximFirsoff/infa_2020_Maxim/raw/main/lab3/trusy-emporio-armani-siniy-545498-1.bmp", "trusy-emporio-armani-siniy-545498-1.bmp")
#    urllib.request.urlretrieve("https://github.com/MaximFirsoff/infa_2020_Maxim/raw/main/lab3/trusy2.bmp", "trusy2.bmp")

pygame.init()

FPS = 30
ballsnumber = 5  # number of balls

# get screen dimensions
screenInfo = pygame.display.Info()

# display's coordinate
xcoord = screenInfo.current_w - 400
ycoord = screenInfo.current_h - 100

py = [1] * ballsnumber  # delta for x moving
px = [1] * ballsnumber  # delta for y moving
newball = [1] * ballsnumber  # list of surfaces what contain our balls and images

screen = pygame.display.set_mode((xcoord, ycoord))  # main screen

score = 0  # Score

COLORS = ["RED", "BLUE", "YELLOW", "GREEN", "MAGENTA", "CYAN"]  # colors of balls

r = [0] * ballsnumber  # radius for each ball
x = [0] * ballsnumber  # x for each ball
y = [0] * ballsnumber  # y for each ball
color = [0] * ballsnumber  # color for each ball


def new_ball(cxindex):
    """ draw a new ball """
    global x, y, r, color
    r[cxindex] = randint(5, 50)
    x[cxindex] = randint(1, xcoord - r[cxindex]*2)
    y[cxindex] = randint(1, ycoord - r[cxindex]*2)
    color[cxindex] = COLORS[randint(0, 5)]
    # angel of fly`s ball
    px[cxindex] = randint(-10, 10)
    py[cxindex] = randint(-10, 10)

    if randint(1, 5) == 3  and score > 100:
        r[cxindex] = 51
        x[cxindex] = randint(1, xcoord - r[cxindex] * 3)
        y[cxindex] = randint(1, ycoord - r[cxindex] * 3)
        newball[cxindex] = pygame.image.load('trusy-emporio-armani-siniy-545498-1.bmp')
        newball[cxindex] = pygame.transform.smoothscale(newball[cxindex], (r[cxindex]*2, r[cxindex]*2))
    else:
        newball[cxindex] = pygame.Surface((r[cxindex] * 2, r[cxindex] * 2), pygame.SRCALPHA)  # container for ball
        circle(newball[cxindex], color[cxindex], (r[cxindex], r[cxindex]), r[cxindex])
    screen.blit(newball[cxindex], ((x[cxindex], y[cxindex])))

def click(ourevent, score):
    """
    in case pressing mouse button
    """
    for cxindex in range(ballsnumber):
        if x[cxindex] <= ourevent.pos[0] <= x[cxindex]+r[cxindex]*2 and \
            y[cxindex] <= ourevent.pos[1] <= y[cxindex]+r[cxindex]*2:
            score += 100/r[cxindex] + 100/(x[cxindex] + y[cxindex]) + 4
            score = int(score) #  for linux
            if r[cxindex] == 51:
                r[cxindex] = 50
                newball[cxindex] = pygame.image.load('trusy2.bmp')
                newball[cxindex] = pygame.transform.smoothscale(newball[cxindex], (r[cxindex] * 2, r[cxindex] * 2))
            else:
                new_ball(cxindex)
        else:
            score -= 1
    return(score)


def filescore(ourgamername, score):
    """
    reading file of score and writing new
    """
    fileline = []
    try:  # check file excist
        open('ballscore.txt')
    except IOError:
        open('ballscore.txt', "w")
    with open('ballscore.txt') as file:
        for lineinfile in file:
            if lineinfile != "\n":
                fileline.append(lineinfile.split("----->"))
        fileline.append([score, ourgamername + "\n"])
        fileline.sort(reverse=True, key=lambda x: int(x[0]))
    filescore = open('ballscore.txt', "w")
    for i in fileline:
        filescore.write(
            str(i[0]) + "----->" + str(i[1])[:-1] + "\n")  # '-1' need for delete "\n" what excist in the end of a line

    filescore.close()


def scoredisplayed(score):
    """
    displaying the score
    """
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Score: " + str(score), True, (180, 120, 120))
    screen.blit(text1, (10, 50))


def gamername(gamername=""):
    """
    To get name of gamer
    """
    blockname = pygame.Surface((480, 360))  # questioning of name
    blockwelcome = pygame.Surface((480, 360))  # writing of name

    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha() and len(gamername) < 20:
                    gamername += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    gamername = gamername[:-1]
                elif evt.key == pygame.K_RETURN:
                    return gamername
            elif evt.type == pygame.QUIT:
                return gamername
        screen.fill((0, 0, 0))
        blockwelcome = font.render("Enter Your name", True, (255, 255, 255))
        blockname = font.render(gamername, True, (255, 255, 255))
        rect = screen.get_rect().center
        screen.blit(blockwelcome, (rect[0]/2 + 100, rect[1] - rect[1]/2))
        screen.blit(blockname, (rect[0]- len(gamername) * 10, rect[1]))
        pygame.display.flip()


clock = pygame.time.Clock()
finished = False

gamername = gamername()

# generating of balls
for cx in range(ballsnumber):
    new_ball(cx)

# main circle
while not finished:
    clock.tick(FPS)

    # if something pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            filescore(gamername, score)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = click(event, score)

    for cx in range(ballsnumber):
 #       circle(newball[cx], color[cx], (r[cx], r[cx]), r[cx])
        x[cx] += px[cx]
        y[cx] += py[cx]
        if x[cx] <= 0 or x[cx] + r[cx]*2 >= xcoord:  # if our ball is near the wall
            px[cx] *= -1
        if y[cx] <= 0 or y[cx] + r[cx]*2 >= ycoord:  # if our ball is near the wall
            py[cx] *= -1
        screen.blit(newball[cx], ((x[cx], y[cx])))

    scoredisplayed(score)
    pygame.display.update()
    screen.fill("BLACK")

pygame.quit()
