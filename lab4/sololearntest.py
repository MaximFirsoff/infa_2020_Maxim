import tkinter as tk

def show(event, p, tag):
    print(f"{p=}\n{tag=}")


centers = [[50, 50], [90, 50]]

root = tk.Tk()
canvas = tk.Canvas()
canvas.grid(row=0, column=0, sticky='news')

p1 = canvas.create_oval(20,10,30,20, fill='green',tags=('point_green_1', 'draw'))
p2 = canvas.create_oval(50,10,60,20, fill='green',tags=('point_green_2', 'draw'))
canvas.tag_bind(p1, '<Button-1>', lambda event: show(event, p1, ('point_green_1', 'draw')))
canvas.tag_bind(p2, '<Button-1>', lambda event: show(event, p2, ('point_green_2', 'draw')))

for idx, center in enumerate(centers):
    tag= f'point_{idx}'
    p=canvas.create_oval(center[0] - 5, center[1] - 5, center[0] + 5, center[1] + 5, fill='red',
                         tags=(tag, 'draw'))
    canvas.tag_bind(p, '<Button-1>', lambda event, p=p, tag=tag: show(event, p, tag))

root.mainloop()