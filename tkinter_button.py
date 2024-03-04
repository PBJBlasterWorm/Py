import tkinter

win = tkinter.Tk()
win.geometry("650x400")
win.resizable(False, False)
win.title("Button 연습")

label = tkinter.Label(win, text="0", font=("맑은고딕", 30), relief="sunken", width=4, height=1)
label.pack()

count = 0

def cntup():
    global count # global = 전역변수 -> 지역변수
    count += 1
    if (count > 100):
        count = 100
    label.config(text=count)
    
def cntdown():
    global count
    count -= 1
    if (count < 0):
        count = 0
    label.config(text=count)
    
def init():
    global count
    count = 0
    label.config(text=count)


up = tkinter.Button(win, text="1 증가", font=("맑은고딕", 20), width=5, height=1, command=cntup,repeatdelay=100 , repeatinterval=100)
up.pack()

down = tkinter.Button(win, text="1 감소", font=("맑은고딕", 20), width=5, height=1, command=cntdown,repeatdelay=100 , repeatinterval=100)
down.pack()

clear = tkinter.Button(win, text="초기화", font=("맑은고딕", 20), width=5, height=1, command=init) 
clear.pack()

win.mainloop()