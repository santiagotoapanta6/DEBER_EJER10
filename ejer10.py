from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 60, 60, fill='blue')
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        lblcoo = Label(canvas, text = pos).place(x = 10, y = 40)
  
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

lblTitle = Label(canvas, text="coordenadas").place(x=10, y=20)
#lblTitle = Label(canvas, text="Tiempo de juego").place(x=10, y=60)


def reloj():
    #lblT = Label(canvas, text="Reloj").place(x=120, y=75)
    lblT = Label(canvas, text="Tiempo de juego").place(x=10, y=100)
    t = time.localtime()
    hora = t[3]
    minutos =t[4]
    segundos = t[5]
    lblHour = Label(canvas, text = str(hora)).place(x = 10, y = 120)
    lblC = Label(canvas, text = ":").place(x = 30, y = 120)
    lblMin = Label(canvas, text = str(minutos)).place(x = 40, y = 120)
    lclC2 = Label(canvas, text = ":").place(x = 60, y = 120)
    lblSec = Label(canvas, text = str(segundos)).place(x = 70, y = 120)

ball = Ball(canvas, 'red')
while 1:
    ball.draw()
    reloj()
    #timer2()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
#canvas.mainloop()

#Bucle infinito
s = 0
while s == 0:
    reloj()
    canvas.update()

def timer2(): #reloj sistemas y dibijar
    lblT = Label(canvas, text="Tiempo de juego").place(x=10, y=200)
    t = time.localtime()
    hora = t[3]
    minutos =t[4]
    segundos = t[5]
    lblHour = Label(canvas, text = str(hora)).place(x = 10, y = 120)
    lblC = Label(canvas, text = ":").place(x = 30, y = 120)
    lblMin = Label(canvas, text = str(minutos)).place(x = 40, y = 120)
    lclC2 = Label(canvas, text = ":").place(x = 60, y = 120)
    lblSec = Label(canvas, text = str(segundos)).place(x = 70, y = 120)
    otroTime = reloj-timer()
    lblT = Label(canvas, text="ti").place(x=10, y=300)
