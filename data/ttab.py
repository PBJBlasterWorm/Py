from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from PIL import ImageTk, Image

root = Tk()
root.title("개망함 ㅅㄱ")
root.geometry("640x480")
root.resizable(True, True)

img = Canvas(root, width=500, height=500, bg="green")
img.pack()


root.mainloop()