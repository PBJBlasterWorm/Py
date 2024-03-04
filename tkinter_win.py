import tkinter

window = tkinter.Tk()
window.geometry("300x500+200+50") # 넓이x높이+x좌표+y좌표
window.resizable(False, False) # 크기 조절(넓이, 높이)

lb = tkinter.Label(window, text="Hello~\nTkinter")
lb.pack()
lb = tkinter.Label(window, text="곧 쉬는시간입니다.")
lb.pack()

window.mainloop()