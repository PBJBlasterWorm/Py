import tkinter

win = tkinter.Tk()
win.geometry("650x400")
win.resizable(False, False)
win.title("Button 연습")

btn1 = tkinter.Button(win, text="aaaaa", width=7, activebackground="red")
btn2 = tkinter.Button(win, text="bbbbb", width=7, activeforeground="blue")
btn3 = tkinter.Button(win, text="ccccc", width=7, state="disabled")

btn1.pack()
btn2.pack()
btn3.pack()
win.mainloop()
"""
state = 버튼 상태 / overrelief = 마우스를 올렸을때 테두리 모양
repeatdelay = 버튼을 눌렀을때부터 실행까지의 대기 시간
repeatinteval = 버튼을 눌렀을때부터 실행까지의 반복 시간
activebackground = 실행시 배경색
activeforeground = 실행시 문자열색
disableforeground = 비활성화 일때 문자열색
highlightcolor = 버튼 선택시 색
highlightthickness = 버튼 선택시 두께
command = 명령(함수)
"""