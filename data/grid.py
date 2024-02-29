from tkinter import *

root = Tk()
root.title("개망함 ㅅㄱ")
root.geometry("640x480")
root.resizable(True, True)

btn1 = Button(root, padx=15, pady=15)
btn2 = Button(root, padx=15, pady=15)
btn3 = Button(root, padx=15, pady=15)
btn4 = Button(root, padx=15, pady=15)

btn1.grid(row=0, column=0, sticky=N+E+W+S)
btn2.grid(row=0, column=1, sticky=N+E+W+S)
btn3.grid(row=0, column=2, sticky=N+E+W+S)
btn4.grid(row=0, column=3, sticky=N+E+W+S)

btn5 = Button(root, padx=15, pady=15)
btn6 = Button(root, padx=15, pady=15)
btn7 = Button(root, padx=15, pady=15)
btn8 = Button(root, padx=15, pady=15)

btn5.grid(row=1, column=0, sticky=N+E+W+S)
btn6.grid(row=1, column=1, sticky=N+E+W+S)
btn7.grid(row=1, column=2, sticky=N+E+W+S)
btn8.grid(row=1, column=3, sticky=N+E+W+S)



root.mainloop()