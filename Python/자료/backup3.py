import tkinter as tk
from tkinter import messagebox
import random

class OmokGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Omok Game")

        self.canvas = tk.Canvas(master, width=600, height=700, bg="tan")
        self.canvas.pack()

        self.board_size = 19
        self.cell_size = 25
        self.margin = 80

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.turn = 1
        self.game_over = False

        self.stone_positions = []

        self.draw_board()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label="New Game", command=self.restart_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="Game", menu=game_menu)

        self.master.config(menu=menu_bar)

    def draw_board(self):
        for i in range(self.board_size):
            start = self.margin + i * self.cell_size
            self.canvas.create_line(self.margin, start, self.margin + (self.board_size - 1) * self.cell_size, start)
            self.canvas.create_line(start, self.margin, start, self.margin + (self.board_size - 1) * self.cell_size)

    def click_handler(self, event):
        if not self.game_over and self.turn == 1:
            col = round((event.x - self.margin) / self.cell_size)
            row = round((event.y - self.margin) / self.cell_size)
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0:
                self.draw_piece(row, col)
                self.stone_positions.append((row, col))
                self.check_winner(row, col)
                self.turn = -self.turn
                self.ai_move()
                
    def ai_mode(self, event):
        if not self.game_over and self.turn == -1:
            empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0]
            if empty_cells:
                row, col = random.choice(empty_cells)
                self.draw_piece(row, col)
                self.stone_positions.append((row, col))
                self.check_winner(row, col)
                self.turn = -self.turn

    def draw_piece(self, row, col):
        x = self.margin + col * self.cell_size
        y = self.margin + row * self.cell_size
        if self.turn == 1:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="black")
            self.board[row][col] = 1
        else:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="white")
            self.board[row][col] = -1

    def check_winner(self, row, col):
        player = self.board[row][col]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
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
        winner = "Black" if player == 1 else "White"
        messagebox.showinfo("Game Over", f"{winner} wins!")
        
    def start_pvp_game(self):
        self.restart_game()
        self.canvas.bind("<Button-1>", self.click_handler)
        
    def start_pve_game(self):
        self.restart_game()
        self.canvas.bind("<Button-1>", self.ai_mode)

    def restart_game(self):
        self.canvas.delete("all")
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_over = False
        self.stone_positions = []
        self.turn = 1
        self.draw_board()
        
    def ai_move(self):
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0]
        if empty_cells:
            # 1. 상대방이 다음에 이길 수 있는 상황을 막을 수 있는지 확인
            for row, col in empty_cells:
                if self.should_block(row, col):
                    self.draw_piece(row, col)
                    self.stone_positions.append((row, col))
                    self.check_winner(row, col)
                    self.turn = -self.turn
                    return
            
            # 2. 자신이 이길 수 있는 상황이 있는지 확인
            for row, col in empty_cells:
                if self.can_win(row, col):
                    self.draw_piece(row, col)
                    self.stone_positions.append((row, col))
                    self.check_winner(row, col)
                    self.turn = -self.turn
                    return
            
            # 3. 내 근처에 돌을 놓도록 하기 위해, 랜덤하게 돌을 놓되, 내 근처에 가까운 곳을 우선적으로 선택
            if self.stone_positions:
                last_move_row, last_move_col = self.stone_positions[-1]
                nearby_empty_cells = [(r, c) for r, c in empty_cells if abs(r - last_move_row) <= 3 and abs(c - last_move_col) <= 3]
                if nearby_empty_cells:
                    row, col = random.choice(nearby_empty_cells)
                else:
                    row, col = random.choice(empty_cells)
            else:
                row, col = random.choice(empty_cells)
            
            self.draw_piece(row, col)
            self.stone_positions.append((row, col))
            self.check_winner(row, col)
            self.turn = -self.turn
            
    def can_win_more_than_3(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for d in directions:
            count_forward = self.count_consecutive(row, col, d[0], d[1], self.turn)
            count_backward = self.count_consecutive(row, col, -d[0], -d[1], self.turn)
            total_count = count_forward + count_backward
            if total_count >= 3:  # 3개 이상의 돌을 놓아 이길 수 있는 상황
                return True
        return False


            
    def should_block(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for d in directions:
            count_forward = self.count_consecutive(row, col, d[0], d[1], -self.turn)
            count_backward = self.count_consecutive(row, col, -d[0], -d[1], -self.turn)
            total_count = count_forward + count_backward
            if total_count >= 3 or total_count >= 4:
                return True     
        return False

    def can_win(self, row, col, player=None):
        if player is None:
            player = self.turn
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for d in directions:
            count_forward = self.count_consecutive(row, col, d[0], d[1], player)
            count_backward = self.count_consecutive(row, col, -d[0], -d[1], player)
            total_count = count_forward + count_backward + 1  # 현재 위치의 돌을 포함하여 평가
            if total_count >= 5:  # 현재 위치에서 이길 수 있는 상황
                return True
        return False    

def main():
    root = tk.Tk()
    game = OmokGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
