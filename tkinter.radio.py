import tkinter
win = tkinter.Tk()
win.geometry("200x230")

radio_var_1 = tkinter.IntVar()
radio_var_2 = tkinter.IntVar()

def check():
    label.config(text=" radio_var_1 = " + str(radio_var_1.get()) + "\n" +
                      " radio_var_2 = " + str(radio_var_2.get()) + "\n\n" +
                      " Total = " + str(radio_var_1.get() + radio_var_2.get())
                      )

radio1 = tkinter.Radiobutton(win, text="1번", variable=radio_var_1, value=3, command=check)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="2번", variable=radio_var_1, value=6, command=check)
radio2.pack()
radio3 = tkinter.Radiobutton(win, text="3번", variable=radio_var_1, value=9, command=check)
radio3.pack()

label = tkinter.Label(win, text="wait", height=5)
label.pack()

radio4 = tkinter.Radiobutton(win, text="4번", variable=radio_var_2, value=13, command=check)
radio4.pack()
radio5 = tkinter.Radiobutton(win, text="5번", variable=radio_var_2, value=17, command=check)
radio5.pack()




win.mainloop()