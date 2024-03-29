from tkinter import *
from tkinter import font

ar = [[[]for i in range(9)]for i in range(9)]

def solve(): # solve:풀다
    for y in range(9):
        for x in range(9):
            tm = ar[y][x].get()
            if tm == "":
                tm = 0
            
            if int(tm) > 9:
                exit(1)
            game[y][x] = int(tm)
            
        for i in game:
            print(i)
        starttree(0)
        mainoutput()
            
root = Tk()
tk.title("sudoku")

font = font.Font(size=15)