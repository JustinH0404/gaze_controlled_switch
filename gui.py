from screeninfo import get_monitors
import tkinter as tk
import tkinter.font as font
# from time import time
# from tkinter import Tk, mainloop, TOP

# assuming single monitor
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height

offset_x = 0
offset_y = 0
dot_r = 10

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("calibration")
        self.geometry('{}x{}+{}+{}'.format(screen_width, screen_height, offset_x, offset_y))
        print('{}x{}'.format(screen_width, screen_height))
        genFont = font.Font(family='Helvetica', size=12, weight='bold')

        self.attributes('-fullscreen', True)

        # location - pack(), grid(), place()
        self.lbl = tk.Label(root, text="Are you ready?", font=genFont)
        self.lbl.place(relx = 0.5, rely=0.8, anchor=tk.CENTER)

        self.btn = tk.Button(root, text="Start", command=start, \
                     font=genFont, width=25, height=2, bg='#000', fg='#00FF00')
        self.btn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.min_x = offset_x + 50
        self.min_y = offset_y + 50
        self.max_x = screen_width - 50
        self.max_y = screen_height - 50

    def start(self):
        self.lbl.destroy()
        self.btn.destroy()

        canvas = tk.Canvas(root, height=screen_height, width=screen_width, bg="#EEE")

        # dot initialization
        x1, y1, x2, y2 = min_x - dot_r, min_y - dot_r, min_x + dot_r, min_y + dot_r
        self.dot = canvas.create_oval(x1, y1, x2, y2, outline='#EEE', fill="black", state=tk.HIDDEN)

        canvas.pack()

        # animation steps
        canvas.after(1000, lambda: self.blink(self.dot, 1))
        canvas.after(5000, lambda: canvas.itemconfig(o1, state=tk.NORMAL))
        canvas.after(5000, lambda: self.move_dot(self.dot, 1))

    def move_dot(self, dot, stage):
        MOVE_TIMESTEP = 30
        ox, oy = canvas.coords(dot)[0] + 10, canvas.coords(dot)[1] + 10
        if stage == 1:
            bound = oy >= self.max_y
            step_x = 0
            step_y = 10
        elif stage == 2:
            bound = ox >= self.max_x
            step_x = 10
            step_y = 0
        elif stage == 3:
            bound = oy <= self.min_y
            step_x = 0
            step_y = -10
        elif stage == 4:
            bound = ox <= self.min_x
            step_x = -10
            step_y = 0
        elif stage == 5:
            bound = ox >= self.max_x
            step_x = (self.max_x) - (self.min_x)) / 100
            step_y = (self.max_y) - (self.min_y)) / 100
        elif stage == 6:
            bound = ox <= self.min_x
            step_x = -10
            step_y = 0
        elif stage == 7:
            bound = ox >= self.max_x
            step_x = (self.max_x) - (self.min_x)) / 100
            step_y = -(self.max_y) - (self.min_y)) / 100
        elif stage == 8:
            bound = ox <= self.min_x
            step_x = -10
            step_y = 0
        elif stage == 9:
            root.destroy()
            return

        if bound:
            self.move_dot(dot, stage + 1)
        else:
            canvas.move(dot, step_x, step_y)
            canvas.after(MOVE_TIMESTEP, lambda: self.move_dot(dot, stage))

    def blink(self, dot, stage):
        if stage == 1:
            canvas.move(dot, min_x, min_y)

        canvas.itemconfig(dot, state=tk.NORMAL)
        canvas.after(1000, lambda: canvas.itemconfig(dot, state=tk.HIDDEN))

# execute tkinter if run
if __name__ == "__main__":
    app = App()
    app.mainloop()
