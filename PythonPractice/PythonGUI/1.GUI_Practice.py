from tkinter import *
from datetime import datetime

win=Tk()

win.geometry("300x100")
win.title("What Time?")
win.option_add("*Font","굴림 20")

btn = Button(win)
btn.config(text= "현재시각")
btn.config(width=10)


def alert():
    now = datetime.now()
    print(now)

btn.config(command= alert)

btn.pack()

win.mainloop()