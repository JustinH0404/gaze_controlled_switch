from screeninfo import get_monitors
# from tkinter import Tk, mainloop, TOP
from tkinter import *
import tkinter.font as font


# assuming single monitor
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
offset_x = -10
offset_y = 0

dot_r = 10


# creates tkinter window
root = Tk()
root.title("calibration")
root.geometry('{}x{}+{}+{}'.format(screen_width, screen_height, offset_x, offset_y))
print('{}x{}'.format(screen_width, screen_height))

genFont = font.Font(family='Helvetica', size=12, weight='bold')

# start page
def start():
    lbl.destroy()
    btn.destroy()
    # root.destroy()

    root.attributes('-fullscreen', True)

    canv = Canvas(root, height=screen_height, width=screen_width, bg="#EEE")

    offset_x = 0
    dot_x = offset_x + 50
    dot_y = offset_y + 50
    x1, y1, x2, y2 = dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r
    o1 = canv.create_oval(x1, y1, x2, y2, fill="black")

    dot_y = screen_height - 50
    x1, y1, x2, y2 = dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r
    o2 = canv.create_oval(x1, y1, x2, y2, fill="black")

    dot_x = screen_width - 50
    x1, y1, x2, y2 = dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r
    o3 = canv.create_oval(x1, y1, x2, y2, fill="black")

    dot_y = offset_y + 50
    x1, y1, x2, y2 = dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r
    o4 = canv.create_oval(x1, y1, x2, y2, fill="black")
    canv.pack()



# location
# pack(), grid(), place()

lbl = Label(root, text = "Are you ready?", font=genFont)
lbl.place(relx = 0.5, rely=0.8, anchor=CENTER)

btn = Button(root, text = "Start", command=start, \
             font=genFont, width=25, height=2, bg='#000', fg='#00FF00')
btn.place(relx=0.5, rely=0.85, anchor=CENTER)




# execute tkinter
root.mainloop()
# if __name__ == "main":
