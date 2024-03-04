from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as msgbox

class cal:
    def __init__(self, admin):
        self.admin = admin
        admin.title("망할 계산기")
        admin.resizable(False, False)
        
        self.display_var = tk.StringVar()
        self.display_var.set("")
        self.display_label = tk.Label(admin, textvariable=self.display_var, font=("맑은고딕", 16), width=15, height=1,
                                       anchor=E, padx=10, pady=10)
        self.display_label.grid(row=0, column=0, columnspan=4)
        
        
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("*", 1, 3)
        
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)
        
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("+", 3, 3)
        
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("/", 4, 3)
        
        self.create_button("C", 5, 3)
        
        self.reset()
        
    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.admin, text=text, font=("맑은고딕", 15), width=4, height=2, 
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=3, pady=3)
        
    def button_click(self, text):
            if text == "C":
                self.reset()
            elif text == "=":
                self.calculate()
            else:
                self.display_var.set(self.display_var.get() + text)
    def calculate(self):
        try:
            result = str(eval(self.display_var.get()))
            self.display_var.set(result)
            
        except:
            ask = msgbox.askokcancel("잘못된 연산", "계산 제대로 한게 맞는가?")
            
            if ask == 1:
                msgbox.showerror("에러!!!!!!!", "프로그램 오류로 종료합니다")
                quit()
                
            else:
                self.reset()
            
    def reset(self):
        self.display_var.set("")

root = Tk()

img = Image.open("내 시험결과.png")
bg = ImageTk.PhotoImage(img)

label = Label(root, image=bg)
label.place(x = 0, y = 0)

program = cal(root)
root.mainloop()