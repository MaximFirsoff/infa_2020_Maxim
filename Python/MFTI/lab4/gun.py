from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball:
    def __init__(self, x=-40, y=-450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        gravitation = 9.8
        self.vy += 0.5*gravitation
        self.x += self.vx
        self.y += self.vy
        if 800 < self.x + self.r:  # if out of screen by x
            self.x = 800 - self.r
            self.vx = -self.vx*0.8  # after wall bump force of ball is less
        if 0 > self.x - self.r:  # if out of screen by x
            self.x = self.r
            self.vx = -self.vx*0.8  # after wall bump force of ball is less
        if 600 < self.y + self.r or self.y + self.r < 0:  # if out of screen by y
            self.vy = -self.vy*0.9
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r)**2:
            return True
        else:
            return False

    def superball(self):
        """
        megabomb from tank
        @return:
        """
        for i in balls:  # for each ball
            print(i.x)


class gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = -1.55  # angel of gun
        self.x = 40
        self.y = 540
        self.new_gun()

    def new_gun(self):
        """
        draw new tank
        @return:
        """
        # body of tank
        canv.create_line(self.x-50, self.y+30, self.x + 50, self.y+30, width=30, tag="tank", fill="orange")
        self.id = canv.create_line(self.x, self.y, self.x+30, self.y-10, width=7, tag="tank")
        # tower of tank
        canv.create_arc(self.x-20, self.y-2, self.x + 20, self.y+50, start=180, extent=-180, tag="tank", fill="green")
        canv.create_oval(self.x-35, self.y+40, self.x-5, self.y+60, tag="tank", fill="black")  # track of tank
        canv.create_oval(self.x+5, self.y+40, self.x+35, self.y+60, tag="tank", fill="black")  # another track of tank
        self.tank = canv.gettags("tank")  # label of tank for destroying

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        vx = self.f2_power * math.cos(self.an)
        vy = self.f2_power * math.sin(self.an)
        new_ball = ball(vx + self.x, vy + self.y)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = vx
        new_ball.vy = vy
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.y < self.y:  # for NOT moving the gun down the tank
                mouse_y = event.y - self.y
            else:
                mouse_y = 0
            if event.x - self.x < 0:  # for right part of targeting
                self.an = math.pi + math.atan(mouse_y / (event.x - self.x))
            elif event.x - self.x > 0:  # for left part of targeting (adding PI 3.14..)
                self.an = math.atan(mouse_y / (event.x - self.x))
            else:  # for 0 (divide zero error)
                self.an = math.pi + math.atan(mouse_y / (event.x - self.x-1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def presskey(self, event=0):
        """
        choice function depend pressing keys
        @return:
        """
        self.event = event
        if event.keycode == 83:  # if pressed "s"
            ball().superball()
        else:
            self.move_of_tank(self.event)

    def move_of_tank(self, event=0):
        """
        moving of gun
        @param event: keys by moving
        @return:
        """
        if event.keycode == 68 and self.x < 760:  # if press 'd' and not a border
            canv.move("tank", 1, 0)  # move the target right
        elif event.keycode == 65 and self.x > 40:  # if press 'a' and not a border
            canv.move("tank", -1, 0)  # move the target left
        listtankcoord = canv.coords(self.id)  # get the coordinates of tank
        if listtankcoord != []:  # if tank exist
            self.x, self.y = listtankcoord[:2]  # new x and y after moving

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class bomb:
    bombs = []

    def targets_bomb(self):
        """
        TODO
        Bombing a gun
        self.x_bomb - x position of bomb
        self.y_bomb - y position of bomb
        @return:
        """
        t1.creatingtime += 5  # for only one bomb in 5 seconds
        self.x_bomb = t1.x
        self.y_bomb = t1.y
        self.new_bomb()

    def new_bomb(self):
        """
        draw new bomb of target
        @return:
        """
        tagnom = rnd(1, 1000)  # for rantom 'tag' indicator
        tagnom = "tag_" + str(tagnom)
        while self.bombs.count(tagnom) > 0:  # if name exist in list of bomb
            tagnom = "tag_" + str(rnd(1, 1000))
        self.bombs.append(tagnom)
        self.id_bomb1 = canv.create_oval(self.x_bomb, self.y_bomb, self.x_bomb+10, self.y_bomb+27, \
                                         fill="black", tag=self.bombs[len(self.bombs)-1])
        self.id_bomb2 = canv.create_polygon((self.x_bomb-4, self.y_bomb-5), (self.x_bomb+5, self.y_bomb), \
                                            (self.x_bomb+12, self.y_bomb-5), (self.x_bomb+5, self.y_bomb+10), \
                                            fill="black", tag=self.bombs[len(self.bombs)-1])

    def bombmove(self):
        """
        moving bombs
        and
        controls hit the tank
        @return:
        """
        for i in self.bombs:  # for all bombs
            canv.move(i, 0, 1)  # move the bomb
            if canv.coords(i)[1] > 600:  # deleting if bomb out of screen
                canv.delete(i)  # deleting bomb
                self.bombs.remove(i)  # deleting element of list

    def tankhit(self):
        """
        controls for tank hitting
        @return: False or True if tank is destroyed
        """
        boolem = False
        for i in self.bombs:  # for all bombs
                   # x coordinate left
                   # x coordinate right
                   # y coordinate bottom
            if     canv.coords("tank")[0] <= canv.coords(i)[2] and \
                   canv.coords("tank")[2] >= canv.coords(i)[0] and \
                   canv.coords("tank")[1] - 30 <= canv.coords(i)[3]:
                return True
        return boolem

    def deleteallbombs(self):
        """
        deleting all bombs
        @return:
        """
        for i in self.bombs:  # for all bombs
            canv.delete(i)  # deleting bomb
            self.bombs.remove(i)  # deleting element of list
        self.bombs = []


class target:
    def __init__(self):
        self.live = 1
        # FIXME: - fixed fixed don't work!!! How to call this functions when object is created?
        self.vx = 1
        self.vy = 1

    def new_target(self):
        self.id = canv.create_oval(0, 0, 0, 0)
        r = self.r = rnd(5, 50)
        self.x2 = self.x = rnd(r, 799-r)
        self.y = rnd(r, 599-r)
        self.color = 'red'
        self.creatingtime = time.time()  # time creating of target
        if choice([True, False]):  # random choosing target`s type
            self.new_target_type1()
        else:
            self.new_target_type2()

    def new_target_type1(self):
        """
        First type of targets
        @return:
        """
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x2+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)

    def new_target_type2(self):
        """
        Targets - type2
        @return:
        """
        self.r2 = self.r + 50  # oval - new shape of targets
        self.x = rnd(self.r2, 799-self.r2)  # else part of target will be out of screen
        self.vy = 0  # this is moving by x-coordinate
        canv.coords(self.id, self.x-self.r2, self.y-self.r, self.x+self.r2, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)
        self.r = self.r2  # for check touch with borders

    def double_of_target(self):
        """
        TODO
        return four target if two of targets is connecting
        @return:
        """
        pass

    def hit(self, points):
        """Попадание шарика в цель."""
        id_points = canv.create_text(30, 30, text=points-1, font='28', fill="white")
        canv.itemconfig(id_points, fill="white")
        canv.create_text(30, 30, text=points, font='28')
        self.new_target = None
        canv.delete(self.id)

    def targetmove(self):
        """Переместить мяч-цель по прошествии единицы времени.
        """
        self.x += self.vx
        self.y += self.vy
        if 800 < self.x + self.r or self.x - self.r < 0:  # if out of screen by x
            self.vx = -self.vx
        if 600 < self.y + self.r or self.y - self.r < 0:  # if out of screen by y
            self.vy = -self.vy
        canv.move(self.id, self.vx, self.vy)  # move the target
        if self.new_target != None and (round(time.time() - self.creatingtime)) % 9 == 0 \
                                   and self.vy == 0:  # if target exist and targets`s type is 2 and 3sec is went out
            bomb().targets_bomb()


t1 = target()
screen1 = canv.create_text(400, 300, text='', font='28')

bullet = 0
balls = []
targets = []  # list of targetx
points = 1
canv.create_text(30, 30, text=points-1, font='28')


def gameover():
    bomb().deleteallbombs()
    for bdestroy in balls:  # get all balls out of screen
        canv.delete(bdestroy.id)
    for tdestroy in targets:  # get all targets out of screen
        canv.delete(tdestroy.id)

    canv.bind('<Button-1>', '')
    canv.bind('<ButtonRelease-1>', '')
    canv.update()
    time.sleep(3)
    canv.update()


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, points, targets
#    t1.new_target()

    g1 = gun()
    bullet = 0
    targets_number = 3  # how many targets needs
    speedofbombsmoving = 5  # how speed bombs must drop

    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind_all('<KeyPress>', g1.presskey)  # meFIXME
    z = 0.03

    for i in range(targets_number):  # in this circle we get all our targets
        news_target = target()
        targets += [news_target]
        news_target.new_target()

    while targets_number > 0 and not bomb().tankhit():
        for i in range(speedofbombsmoving):  # moving of bombs
            bomb().bombmove()
        for t1 in targets:  # moving of targets
            t1.targetmove()
        for b in balls:
            if b.x < 0 or b.x > 800 or b.y > 600:  # for all balls out of screen
                canv.delete(b.id)
                balls.remove(b)  # deleting elements of list
            b.move()
            for t1 in targets:  # if some of the targets is hits
                if b.hittest(t1) and t1.live:
                    t1.live = 0
                    t1.hit(points)
                    bomb().tankhit()
                    points += 1
                    targets_number -= 1  # one less target
                    if targets_number == 0:  # if all targets destroyed
                        canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                        gameover()

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    gameover()
    targets = []
    balls = []
    canv.itemconfig(screen1, text='')
    canv.delete(g1.tank)
    root.after(750, new_game)


new_game()
canv.delete(all)  # clear all screen (canvas)

tk.mainloop()
