from tkinter import *
import tkinter as tk
import numpy as np
import os

size = 15 # 바둑판 크기
board = np.zeros([size, size])

black = 1 # 흑돌
white = 2 # 백돌
run = True # 게임시작
first = 1 # 흑돌 선턴



def play(turn):
    while run:
        os.system("clear")
    print(board)
    
    if turn % 2 == 1:
        turn_player = "black"
    else:
        turn_player = "white"
        
    print("")
    print("turn_player")

root = Tk()
root.title("gomoku")
root.geometry("800x800")

root.mainloop()