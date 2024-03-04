import tkinter

area = tkinter.Tk()
area.geometry("640x480")
area.title("listbox 연습")

frame = tkinter.Frame(area)
frame.pack()

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tkinter.Listbox(frame,yscrollcommand=scrollbar.set)
for x in range(20):
    listbox.insert(x, str(x)+"번")
listbox.pack(side="left")
scrollbar["command"]=listbox.yview

area.mainloop()