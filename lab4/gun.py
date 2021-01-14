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


class ball():
    def __init__(self, x=40, y=450):
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
        if 800 < self.x + self.r or self.x + self.r < 0:  # if out of screen by x
            self.vx = -self.vx
        if 600 < self.y + self.r or self.y + self.r < 0:  # if out of screen by y
            self.vy = -self.vy
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


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = -1.55  # angel of gun
        self.x = 40
        self.y = 540
        self.new_gun()
    #       self.id = canv.create_line(20,450,50,420,width=7, tag="tank") # FIXME: don't know how to set it...

    def new_gun(self):
        """
        draw new tank
        @return:
        """
        self.id = canv.create_line(self.x, self.y, self.x+30, self.y-10, width=7, tag="tank")
        canv.create_line(self.x-50, self.y+30, self.x + 50, self.y+30, width=30, tag="tank", fill = "orange")  # body of tank
        canv.create_arc(self.x-20, self.y-2, self.x + 20, self.y+50, start=180, extent=-180, tag="tank", fill = "green")  # tower of tank
        canv.create_oval(self.x-35, self.y+40, self.x-5, self.y+60, tag="tank", fill = "black")  # track of tank
        canv.create_oval(self.x+5, self.y+40, self.x+35, self.y+60, tag="tank", fill = "black")  # another track of tank
        self.tank = canv.gettags("tank")  #  lebel of tank for destroying


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
                self.an = math.pi + math.atan(mouse_y/ (event.x - self.x))
            elif event.x - self.x > 0:  # for left part of targeting (adding PI 3.14..)
                self.an = math.atan(mouse_y / (event.x - self.x))
            else:  # for 0 (divide zero error)
                self.an = math.pi + math.atan(mouse_y/ (event.x - self.x-1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )


    def move_of_tank(self, event=0):
        """
        moving of gun
        @param event: keys by moving
        @return:
        """
        if event.keysym == "d" and self.x < 760:  # if press 'd' and not a border
            canv.move("tank", 1, 0)  # move the target right
        elif event.keysym == "a" and self.x > 40: # if press 'a' and not a border
            canv.move("tank", -1, 0)  # move the target left
        listtankcoord = canv.coords(self.id)  # get the coordinates of tank
        self.x, self.y = listtankcoord[:2]  # new x and y after moving

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class bomb():
    bombs = []
    def targets_bomb(self):
        """
        TODO
        Bombing a gun
        self.x_bomb - x position of bomb
        self.y_bomb - y position of bomb
        @return:
        """
    #    print(time.time() - self.creatingtime )
        t1.creatingtime += 5  # for only one bomb in 5 seconds
        self.x_bomb = t1.x
        self.y_bomb = t1.y
        self.new_bomb()

 #       self.bombs += [self.new_bomb()]


    def new_bomb(self):
        """
        draw new bomb of target
        @return:
        """
        self.id_bomb1 = canv.create_oval(self.x_bomb, self.y_bomb, self.x_bomb+10, self.y_bomb+27, \
                         fill="black", tag="targetbomb")
        self.id_bomb2 = canv.create_polygon((self.x_bomb-4, self.y_bomb-5), (self.x_bomb+5, self.y_bomb), \
                            (self.x_bomb+12, self.y_bomb-5), (self.x_bomb+5, self.y_bomb+10), \
                            fill="black", tag="targetbomb")
        self.bombs.append(self.id_bomb1)


    def bombmove(self):
        """
        moving bombs
        @return:
        """
        canv.move("targetbomb", 0, 1)   # move the bomb
#        self.y_bomb += 1
#        print(self.y_bomb)
#        print(bool(canv.coords("targetbomb")))
 #       print(canv.coords(self.id_bomb1))
        print (len(self.bombs))
        for i in self.bombs:  # for all bombs
            print (canv.coords(i)[1])

            if canv.coords(i)[1] > 600:  # deleting if bomb out of screen
                canv.delete(i)  # deleting bomb
                self.bombs.remove(i)  # deleting element of list

    def tankhit(self):
        """
        controls for tank hitting
        @return:
        """
        print(canv.coords("tank"))
        print(canv.coords("targetbomb"))


class target():
    def __init__(self):
        self.live = 1
        # FIXME: - fixed fixed don't work!!! How to call this functions when object is created?
#        canv.create_oval(0, 0, 50, 50, outline="white", fill="white") # clear old points. TODO - change the method
#        self.id_points = canv.create_text(30,30,text = "0",font = '28')
        self.vx = 1
        self.vy = 1


    def new_target(self):
        self.id = canv.create_oval(0, 0, 0, 0)
        r = self.r = rnd(5, 50)
        self.x2 = self.x = rnd(r, 799-r)
        y = self.y = rnd(r, 599-r)
        color = self.color = 'red'
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


    def destroybombs(self):
        """
        deleting all objects of target
        @return:
        """
        canv.delete("targetbomb")


    def hit(self, points):
        """Попадание шарика в цель."""
        id_points = canv.create_text(30, 30, text=points-1, font='28', fill = "white")
        canv.itemconfig(id_points, fill = "white")
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
points = 1
canv.create_text(30, 30, text=points-1, font='28')

def new_game(event=''):
    global gun, t1, screen1, balls, bullet, points
#    t1.new_target()

    g1 = gun()
    targets = [] # list of targetx
    bullet = 0
    balls = []
    targets_number = 3  #  how many targets needs
    canv.bind_all('<KeyPress>', g1.move_of_tank) # meFIXME
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)


    z = 0.03

    for i in range(targets_number):  # in this cicle we get all our targets
        news_target = target()
        targets += [news_target]
        news_target.new_target()

    while targets_number > 0:
        for t1 in targets:  # moving of targets
            t1.targetmove()
            bomb().bombmove()
        for b in balls:
            b.move()
            for t1 in targets:  # if some of the targets is hits
                if b.hittest(t1) and t1.live:
                    t1.live = 0
                    t1.hit(points)
                    bomb().tankhit()
                    points += 1
                    targets_number -= 1  # one less target
                    if targets_number == 0: # if all targets destroyed
                        for bdestroy in balls:  # get all balls out of screen
                            canv.delete(bdestroy.id)
                        t1.destroybombs()
                        canv.bind('<Button-1>', '')
                        canv.bind('<ButtonRelease-1>', '')
                        canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                        canv.update()
                        time.sleep(3)

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(g1.tank)
    root.after(750, new_game)


new_game()
canv.delete(all)  # clear all screen (canvas)

tk.mainloop()
