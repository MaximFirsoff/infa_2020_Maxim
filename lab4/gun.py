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
        self.an = 1
        self.x = 40
        self.y = 540
        self.id = canv.create_line(self.x, self.y, self.x+30, self.y-30, width=7, tag="tank")
    #       self.id = canv.create_line(20,450,50,420,width=7, tag="tank") # FIXME: don't know how to set it...


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
        new_ball = ball(vx + 20, vy + 450)
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
            try:
#                self.an = math.atan((event.y-450) / (event.x-20))
                self.an = math.atan((event.y-self.y) / (event.x-self.x))
            except ZeroDivisionError:
                self.an = math.atan((event.y - 450) / (event.x - 19))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )
        # canv.coords(self.id, 20, 450,
        #             20 + max(self.f2_power, 20) * math.cos(self.an),
        #             450 + max(self.f2_power, 20) * math.sin(self.an)
        #             )


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.live = 1
        # FIXME: fixed don't work!!! How to call this functions when object is created?
        canv.create_oval(0, 0, 50, 50, outline="white", fill="white")
        id_points = canv.create_text(30,30,text = "0",font = '28')
 #       self.id = id
        self.vx = 1
        self.vy = 1


    def new_target(self):
        self.id = canv.create_oval(0, 0, 0, 0)
        r = self.r = rnd(5, 50)
        self.x2 = self.x = rnd(r, 780)
        y = self.y = rnd(r, 550)
        color = self.color = 'red'
        if choice([True, False]):
            self.new_target_type1()
        else:
            self.new_target_type2()

    def new_target_type1(self):
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x2+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)

    def new_target_type2(self):
        self.r2 = self.r+50
        self.y = rnd(self.r2, 550)
        self.vy = 0
        canv.coords(self.id, self.x-self.r2, self.y-self.r, self.x+self.r2, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)
        self.r = self.r+50

    def double_of_target(self):
        """
        return four target if two of targets is connecting
        @return:
        """
        pass

    def targets_bomb(self):
        """
        Bobing a gun
        @return:
        """
        pass


    def hit(self, points):
        """Попадание шарика в цель."""
        canv.create_oval(0, 0, 50, 50, outline = "white", fill = "white")
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
        # canv.coords(
        #         self.id,
        #         self.x - self.r,
        #         self.y - self.r,
        #         self.x + self.r,
        #         self.y + self.r
        # )
        canv.move(self.id, self.vx, self.vy)

t1 = target()
screen1 = canv.create_text(400, 300, text='', font='28')

bullet = 0
balls = []
targets = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
#    t1.new_target()
    points = 1
    g1 = gun()
    targets = []
    bullet = 0
    balls = []
    targets_number = 3  #  how many targets needs
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03

    for i in range(targets_number):
        news_target = target()
        targets += [news_target]
        id = canv.create_oval(0, 0, 0, 0)  # picture of our target
        #news_target.new_target(canv.create_oval(0, 0, 0, 0))
        news_target.new_target()

    while targets_number > 0:
        for t1 in targets:
            t1.targetmove()
        for b in balls:
            b.move()
            for t1 in targets:
#               t1.targetmove()
                if b.hittest(t1) and t1.live:
                    t1.live = 0
                    t1.hit(points)
                    points += 1
                    targets_number -= 1
                    if targets_number == 0:
                        for bdestroy in balls:
                            canv.delete(bdestroy.id)
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
    canv.delete(g1.id)
    root.after(750, new_game)


new_game()
canv.delete(all)

tk.mainloop()
