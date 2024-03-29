import tkinter as tk
from tkinter import messagebox

class OmokGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Omok Game")

        self.canvas = tk.Canvas(master, width=600, height=600, bg="tan")
        self.canvas.pack()

        self.board_size = 20 # 오목판 크기
        self.cell_size = 25 #
        self.margin = 0

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]  # 15x15 보드 생성
        self.turn = 1  # 1: 흑돌, -1: 백돌
        self.game_over = False

        self.draw_board()

        self.canvas.bind("<Button-1>", self.click_handler)

    def draw_board(self):
        for i in range(self.board_size):
            start = self.margin + i * self.cell_size
            self.canvas.create_line(self.margin, start, self.margin + (self.board_size - 1) * self.cell_size, start)  # 수평선
            self.canvas.create_line(start, self.margin, start, self.margin + (self.board_size - 1) * self.cell_size)  # 수직선

    def click_handler(self, event):
        if not self.game_over:
            col = round((event.x - self.margin) / self.cell_size)
            row = round((event.y - self.margin) / self.cell_size)
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0:
                self.draw_piece(row, col)
                self.check_winner(row, col)

    def draw_piece(self, row, col):
        x = self.margin + col * self.cell_size
        y = self.margin + row * self.cell_size
        if self.turn == 1:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="black")
            self.board[row][col] = 1
            self.turn = -1
        else:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="white")
            self.board[row][col] = -1
            self.turn = 1

    def check_winner(self, row, col):
        player = self.board[row][col]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 가로, 세로, 대각선(↘), 대각선(↗)
        for d in directions:
            count = self.count_consecutive(row, col, d[0], d[1], player) + self.count_consecutive(row, col, -d[0], -d[1], player) + 1
            if count == 5:
                self.game_over = True
                self.show_winner(player)
                return

    def count_consecutive(self, row, col, d_row, d_col, player):
        count = 0
        r, c = row + d_row, col + d_col
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
            count += 1
            r, c = r + d_row, c + d_col
        return count

    def show_winner(self, player):
        winner = "흑돌" if player == 1 else "백돌"
        messagebox.showinfo("게임 종료", f"{winner}이(가) 승리했습니다!")

def main():
    root = tk.Tk()
    game = OmokGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()