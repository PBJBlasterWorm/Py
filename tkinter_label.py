import tkinter

win = tkinter.Tk()
win.geometry("650x400")
win.resizable(False, False)
win.title("라벨연습")

label = tkinter.Label(win, text="Python Label 제목", width=50, height=2, relief="solid", bg="green", fg="red")
label.pack()
text_str = "Python 연습\nPython 연습 Python 연습\n"
label2 = tkinter.Label(win ,text=text_str, relief="raised", justify="right")
label2.pack()
label3 = tkinter.Label(win, text="Hello~ Python", font=("궁서체", 30), highlightthickness=5, highlightbackground="#ffff00")
label3.pack()

"""
text = 문자열의 내용 / textvariable = 가져올 문자열의 변수(다른 컨트롤)
justify = 문자열 정렬 / font = (글꼴, 크기)
bitmap = 기본 이미지 / image = 임의 이미지 / compound = 문자열 + 이미지 겹치기

width = 넓이 / height = 높이 / relief = 테두리모양
bd(borderwidth) = 테두리 두께
bg(background) = 배경 색 / fg(foreground) = 문자열 색
highlightthickness = 테두리 두께 / highlightbackground = 테두리 색상
padx = 가로 안 여백 / pady = 세로 안 여백

"""

win.mainloop()