import tkinter

win = tkinter.Tk()
win.geometry("650x400")

a1 = tkinter.Button(win, text="a1")

img = tkinter.PhotoImage(file="boom.png")
label = tkinter.Label(win, image=img)

a1.place(x=250, y=300)
label.place(x=0, y=0)

a1.lift()

win.mainloop()