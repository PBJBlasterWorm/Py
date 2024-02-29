from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import time
import os
from PIL import ImageTk, Image

root = Tk()
root.title("개망함 ㅅㄱ")
root.geometry("640x480")
root.resizable(True, True)

menu = Menu(root)
menu_test = Menu(menu, tearoff=0)
menu.add_cascade(label="하하하하하", menu=menu_test)

txt = Text(root, height=50)
txt.pack(fill="both", )

def pro():
    for i in range(1, 101):
        time.sleep(0.01)
        progressbar.set(i)
        progressbar.update()

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate",length=500, variable=pro)
progressbar.pack()
progressbar.start(100)


scrollbar = Scrollbar(txt)
scrollbar.pack(side="right", fill=Y)


def zotmang():
    msgbox.showerror("응 ㅅㄱ", "하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n하하하하하하하하하하하하하\n")
       
def zot():
    msgbox.askyesnocancel("뭘 고르든 망했다 수고링", "ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망\nㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망\nㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망\nㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망ㅈ망\n")
    
    
menu_test.add_command(label="하", command=zotmang)
menu_test.add_command(label="하하", command=zot)
menu_test.add_command(label="하하하")
menu_test.add_separator()
menu_test.add_command(label="하하하하")
menu_test.add_command(label="하하하하하")
menu_test.add_command(label="하하하하하하")

photo = ImageTk.PhotoImage(file="data/boom.png")
plabel = Label(root, image=photo)
plabel.pack(expand=1, anchor=S)

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()