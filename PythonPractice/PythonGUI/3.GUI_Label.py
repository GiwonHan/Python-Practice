from tkinter import *
from datetime import datetime


win = Tk()
win.title("GUIT Basic")
win.geometry("640x480")

win.option_add("*Font", "맑은고딕 20")

lab1 = Label(win)
lab1.config(text = "ID:")
lab1.pack()

ent1 = Entry(win)
ent1.insert(0,"temp@temp.com")
def clear(event):
    if ent1.get() == "temp@temp.com":
        ent1.delete(0,len(ent1.get()))

ent1.bind("<Button-1>", clear)
ent1.pack()


lab2 = Label(win)
lab2.config(text = "Password:")
lab2.pack()

ent2 = Entry(win)
ent2.config(show = "*")
ent2.pack()

btn = Button(win, text = "로그인")

def login():
    my_id = ent1.get()
    my_pw = ent2.get()
    print(my_id, my_pw)
    lab3.config(Text = "로그인 성공")

btn.config(command = login)
btn.pack()

lab3 = Label(win)
lab3.pack()


# label = Label(win, text = "현재시각입니다.")
# label.pack()

# def nowtime():
#     now = datetime.now()
#     label.config(text= str(now))
    
# btn = Button(win, text = "현재시간은?", command=nowtime)
# btn.pack()


win.mainloop()
