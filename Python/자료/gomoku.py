import tkinter as tk
from tkinter import messagebox
import random
import tkinter as tk
from pygame import mixer  # 배경음 or 효과음 넣기위한 모듈
import tkinter as tk
import threading
import sys

def play_background_music(): # 메인 배경음악
    mixer.init() # 맨 처음 초기화
    mixer.music.load("자료/aa.mp3")  # 음악 파일 경로 설정
    mixer.music.play(-1)  # -1로 설정하여 반복 재생
    # 음악 재생을 백그라운드 스레드에서 수행
music_thread = threading.Thread(target=play_background_music)

def play_effect_stone(): # 착석할때 효과음
    mixer.init()
    mixer.music.load("자료/티모.mp3")
    mixer.music.play(0) # 1번만 재생
music1 = threading.Thread(target=play_effect_stone)

def play_win_sound(): # 승리시 효과음
    mixer.init()
    mixer.music.load("자료/승리.wav")
    mixer.music.play(0)
music2 = threading.Thread(target=play_win_sound)

def play_lose_sound(): # 패배시 효과음
    mixer.init()
    mixer.music.load("자료/패배.wav")
    mixer.music.play(0)
music3 = threading.Thread(target=play_lose_sound)
    
class OmokGame: # 오목게임을 구현하는 메인 클래스
    def __init__(self, master): # 오목게임의 메인 or 초기화하는 메서드
        self.master = master # master 매개변수로 전달된 tkinterface 윈도우 객체를 저장하는 공간
        self.master.title("Omok Game") # 게임 제목
        
        objectlabel = tk.Label(self.master, text="오목게임\n게임 설명 : 5개의 돌이 이어지면 승리!!",bg="black",fg="white", font=("Helvetica", 18)) # 게임 목표를 위에 라벨로 적어줌
        objectlabel.pack(pady=20) # 라벨을 위에 배치
        
        self.canvas = tk.Canvas(master, width=600, height=700, bg="tan") # 600x700 크기의 게임판 생성
        self.canvas.pack() # tkinter에 배치

        self.board_size = 19 # 보드 크기
        self.cell_size = 25 # 돌을 놓는 셀의 크기
        self.margin = 80 # 보드 왼쪽상단 기준 가장자리와의 여백

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)] # 위의 보드크기 변수값을 담는 2차원 리스트 
        self.turn = 1 # 플레이어의 차례(턴)을 나타내는 변수
        self.game_over = False # 게임오버 여부(즉 True일떄 게임오버 상태이며 평상시엔 False상태)

        self.stone_positions = [] # 플레이어아 놓은 돌의 위치를 저장하는 리스트
        
        self.mode = tk.IntVar() # 게임모드를 나타내는 변수(1은 pvp모드, 2는 pve모드)
        self.mode.set(1) # 초기 게임모드를 pvp로 나타냄
        
        self.time_limit = 15 # 메인시간 제한
        self.time_remaining = self.time_limit # 아래쪽 라벨에 띄울 시간
        self.time_label = tk.Label(master, text=f"시간 제한 : {self.time_remaining}", font=("맑은고딕", 15), relief="sunken", border=3) # 시간제한 구현
        self.time_label.pack() # 구현한 라벨을 tkinter에 넣음
                
        self.create_mode_selection() # 게임모드 선택을 위한 라디오버튼을 생성하는 메서드를 호출

        self.draw_board() # 초기 보드를 그리는 메서드
        self.canvas.bind("<Button-1>", self.click_handler) # 캔버스에 마우스 왼쪽버튼 클릭이벤트를 구현하는 핸들러를 등록

        self.create_menu() # 게임 메뉴를 구현하는 메서드를 호출
        self.start_timer() # 게임 타이머를 시작하는 메서드를 호출
        
    def create_mode_selection(self): # 모드 선택을 위한 라디오 버튼을 담은 메서드
        mode_frame = tk.Frame(self.master) #모드 라디오 버튼을 담을 프레임을 생성
        mode_frame.pack() # 프레임을 tkinter에 배치

        pvp_radio = tk.Radiobutton(mode_frame, text="Player vs Player", variable=self.mode, value=1, command=self.restart_game) # pvp 모드를 선택하는 라디오 버튼을 생성하며 self.mode 변수에 연계, 값으로 1을 가지며 클릭시 게임이 초기화되면서 모드가 바뀜)
        pvp_radio.pack(side="left") # pvp 라디오버튼을 배치

        pve_radio = tk.Radiobutton(mode_frame, text="Player vs AI", variable=self.mode, value=2, command=self.restart_game) # pvp 모드를 선택하는 라디오 버튼을 생성하며 self.mode 변수에 연계, 값으로 1을 가지며 클릭시 게임이 초기화되면서 모드가 바뀜)
        pve_radio.pack(side="right") # pve 라디오버튼을 배치


    def create_menu(self): # 게임 메뉴를 생성하는 메서드
        menu_bar = tk.Menu(self.master) # 메뉴를 집어넣을 변수

        game_menu = tk.Menu(menu_bar, tearoff=0) # 메인 메뉴를 생성
        game_menu.add_command(label="New Game", command=self.restart_game) # 게임 재시작 기능을 하는 세부메뉴
        game_menu.add_command(label="Select mode : PVP", command=self.select_pvp) # pvp 모드로 설정하는 세부메뉴
        game_menu.add_command(label="Select mode : PVE", command=self.select_pve) # pve 모드로 설정하는 세부메뉴
        game_menu.add_separator() # 메뉴 사이 선으로 구분
        game_menu.add_command(label="Exit", command=sys.exit) # 게임을 종료하는 세부메뉴
        menu_bar.add_cascade(label="Game", menu=game_menu) # 위 세부메뉴들을 포함하는 앞에서 생성한 메인메뉴를 배치

        self.master.config(menu=menu_bar) # self.master 의 메뉴를 위에서 tk메뉴로 지정한 menu_bar로 설정
        
    def select_pvp(self): # pvp 모드를 선택하는 기능을 구현하는 메서드
        self.restart_game() # 게임을 초기화하고
        self.mode.set(1) # 라디오 버튼에 지정한 변수값 1을 호출하여 pvp모드 라디오버튼을 선택하고 pvp모드로 바뀜
        
    def select_pve(self): # pve 모드를 선택하는 기능을 구현하는 메서드
        self.restart_game() # 게임을 초기화하고
        self.mode.set(2) # 라디오 버튼에 지정한 변수값 2를 호출하여 pve모드 라디오버튼을 선택하고 pve모드로 바뀜

    def draw_board(self): # 게임판을 그리는 메서드
        for i in range(self.board_size): # 보드 크기만큼 반복문을 돌림
            start = self.margin + i * self.cell_size # 보드판 구현할때 시작점을 정함
            self.canvas.create_line(self.margin, start, self.margin + (self.board_size - 1) * self.cell_size, start) # 수평선을 그림
            self.canvas.create_line(start, self.margin, start, self.margin + (self.board_size - 1) * self.cell_size) # 수직선을 그림

    def click_handler(self, event): # 마우스 클릭 이벤트를 처리하는 메서드
        if not self.game_over: # 게임이 진행중일때(게임오버가 아닐때)
            col = round((event.x - self.margin) / self.cell_size) # 클릭위치의 x좌표를 보드의 열값으로 대입
            row = round((event.y - self.margin) / self.cell_size) # 클릭위치의 y좌표를 보드의 행값으로 대입
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0: # 클릭한 위치가 보드 안쪽이고 비어있다면
                self.draw_piece(row, col) # 클릭한 위치에 돌을 배치한다
                self.stone_positions.append((row, col)) # 돌의 위치를 리스트에 저장
                self.check_winner(row, col) # 승리 체크
                self.turn = -self.turn # 턴을 변경함
                
                if self.mode.get() == 2: # 만약 pve모드이면
                    self.ai_move() # ai가 무작위로 돌을 놓는 메서드를 호출
                    
            self.stop_timer() # 타이머를 중지
            self.time_remaining = self.time_limit # 타이머를 초기화
            self.update_timer_label() # 타이머를 업데이트
            self.start_timer() # 타이머를 다시 돌림
            


    def draw_piece(self, row, col): # 주어진 행과 열에 바둑알을 그리는 메서드
        x = self.margin + col * self.cell_size # 바둑알을 그릴 x좌표를 계산
        y = self.margin + row * self.cell_size # 바둑알을 그릴 y좌표를 계산
        if self.turn == 1: # 만약 흑돌차례인 경우
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="black") # 중심좌표(x,y)11씩 주어진, 즉 반지름이 11인 흑돌을 그림
            self.board[row][col] = 1 # 해당 위치를 1(흑돌)로 표시
            self.turn == -1 # 턴을 백돌차례로 변경
            play_effect_stone() # 돌을 놓을때 효과음 출력
        else:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="white") # 중심좌표(x,y)11씩 주어진, 즉 반지름이 11인 백돌을 그림
            self.board[row][col] = -1 # 해당 위치를 -1(백돌)로 표시
            self.turn == 1 # 턴을 흑돌차례로 다시 변경
            play_effect_stone() # 역시 착석할때 효과음을 출력함

    def check_winner(self, row, col): # 바둑돌을 놓을때 승리 조건을 만족하는지 체크함
        player = self.board[row][col] # 현재 행과열에 해당하는 바둑돌의 플레이어를 정함
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # 승리조건을 체크하기위해 방향을 구현(가로, 세로, 대각선 전부다)
        for d in directions: # 모든 방향을 체크
            count = self.count_consecutive(row, col, d[0], d[1], player) + self.count_consecutive(row, col, -d[0], -d[1], player) + 1 # 해당 방향으로 연속된 돌의 갯수를 체크(돌을 놓은직후 현재위치도 포함하여 양쪽으로 연속된 돌의갯수를 체크)
            if count == 5: # 만약 연속된 돌의갯수가 5개이면
                self.game_over = True # 게임을 종료한다(False -> True)
                self.show_winner(player) # 승리한 플레이어를 출력하는 메서드를 호출
                return # 메서드 탈출(종료)

    def count_consecutive(self, row, col, d_row, d_col, player): # 위에서 승리조건을 체크할때 돌의 갯수를 세기위한 메서드
        count = 0 # 연속된 돌의 갯수를 저장할 변수값을 0으로 리셋
        r, c = row + d_row, col + d_col # 주어진 위치에서 시작하여 주어진 방향으로 이동
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player: # 보드 내부에 있고 현재 위치의 바둑돌이 주어진 플레이어의 돌과 같은 색일때 반복
            count += 1 # 연속된 돌의 값에 1을 증가
            r, c = r + d_row, c + d_col # 주어진 방향으로 한칸 이동
        return count # 연속된 돌의 값으로 반환

    def show_winner(self, player): # 게임의 승자를 표시해주는 메서드
        if player == 1: winner = "흑돌"  # 만약 1(흑돌)이 이겼다면 흑돌승리를
        else: winner = "백돌" # 아니라면 백돌승리를 출력
        
        if player == 1: # 플레이어 기준 흑돌이므로 흑돌승리지 승리사운드 출력
            play_win_sound()
        else: # 아니라면 패배사운드 출력
            play_lose_sound()
        messagebox.showinfo("Game Over", f"{winner}이 승리하였습니다.") # 메세지박스
        

    def restart_game(self): # 게임을 재시작하거나 모드를 변경할때 초기화하는 메서드
        self.canvas.delete("all") # 캔버스에 기록된 모든 내용물을 지움
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)] # 게임보드를 초기화하고 0(공백)으로 채움
        self.game_over = False # 게임오버(True)상태를 다시 진행상태(False)로 변경
        self.stone_positions = [] # 돌의 위치를 저장하는 리스트를 초기화
        self.turn = 1 # 턴을 다시 흑돌로 전환
        self.draw_board() # 보드를 다시 그림
        self.stop_timer() # 타이머를 멈춤
        self.time_remaining = self.time_limit # 남은 시간을 다시 초기 제한시간값으로 초기화
        self.update_timer_label() # 타이머 레이블을 업데이트함
        self.start_timer() # 타이머를 다시 돌림
        
    def ai_move(self): # 인공지능 구현하는 메서드
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0] # 현재 보드에서 비어있는 셀의 위치를 저장
        if empty_cells: # 빈셀에 대한 조건
            # 1. 상대방이 다음에 이길 수 있는 상황을 막을 수 있는지 확인
            for row, col in empty_cells: 
                if self.should_block(row, col): # 이 메서드가 True를 반환시
                    self.draw_piece(row, col) # 해당 위치에 돌을 놓음
                    self.stone_positions.append((row, col)) # 방금 놓은 돌의 위치를 리스트에 저장
                    self.check_winner(row, col) # 승자체크
                    self.turn = -self.turn # 차례 변경
                    return
            
            # 2. 자신이 이길 수 있는 상황이 있는지 확인
            for row, col in empty_cells: 
                if self.can_win(row, col): # 이 메서드가 True를 반환시(ai 본인이 이길수 있는 상황)
                    self.draw_piece(row, col) # 해당 위치에
                    self.stone_positions.append((row, col)) # 방금 놓은 돌의 위치를 리스트에 넣음
                    self.check_winner(row, col) # 승자 체크
                    self.turn = -self.turn # 차례 변경
                    return
            
            # 3. 내 근처에 돌을 놓도록 하기 위해, 랜덤하게 돌을 놓되, 내 근처에 가까운 곳을 우선적으로 선택
            if self.stone_positions:
                last_move_row, last_move_col = self.stone_positions[-1] # ai가 이전에 놓은 돌의 위치를 확인
                nearby_empty_cells = [(r, c) for r, c in empty_cells if abs(r - last_move_row) <= 2 and abs(c - last_move_col) <= 2] # 이전에 놓은돌의 2칸범위 이내에 비어있는 셀을확인
                if nearby_empty_cells: # 만약 놓은돌의 주변에 비어있는 셀이 있으면
                    row, col = random.choice(nearby_empty_cells) # 랜덤으로 그중에서 빈칸에 넣음
                else: # 주변에 돌이 없을땐 그냥 그주위에 무작위로 돌을 넣음
                    row, col = random.choice(empty_cells)
            else:
                row, col = random.choice(empty_cells)
            
            self.draw_piece(row, col) # 그 위치에 돌을 생성
            self.stone_positions.append((row, col)) # 그 돌의 위치도 리스트에 저장
            self.check_winner(row, col) # 승자 체크
            self.turn = -self.turn # ai 차례 종료
            
    def should_block(self, row, col): # 상대방이 이길수있는 상황을 막을수 있는지 여부를 확인
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # 모든 방향에 대하여
        for d in directions: # 반복
            count_forward = self.count_consecutive(row, col, d[0], d[1], -self.turn) # 앞쪽 방향을 검사
            count_backward = self.count_consecutive(row, col, -d[0], -d[1], -self.turn) # 뒷쪽 방향을 검사
            total_count = count_forward + count_backward # 앞뒤로 검사한 돌의 갯수를 저장
            if total_count >= 3 or total_count >= 4: # 만약 수평,수직으로 연속된돌이 3,4개 이상인경우 
                return True # True를 반환하여 돌을 막음
        return False # 아니면 굳이 막는 스탠스를 취하지 않음

    def can_win(self, row, col, player=None):
        if player is None: # 플레이어 값이 주어지지 않았으므로 현재 플레이어로 설정
            player = self.turn # 플레이어 값이 주어지지 않았으므로 현재 플레이어로 설정
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # 모든 방향
        for d in directions: # 모든 방향을 검사
            count_forward = self.count_consecutive(row, col, d[0], d[1], player) # 전방의 연속된 돌을 검사
            count_backward = self.count_consecutive(row, col, -d[0], -d[1], player) # 후방의 연속된 돌을 검사
            total_count = count_forward + count_backward + 1  # 현재 위치의 돌을 포함(+1)하여 평가 
            if total_count >= 5:  # 돌이 5개이상이면
                return True # 승리조건 만족(True)
        return False
    
    def start_timer(self): # 타이머를 돌리는 메서드
        self.timer_id = self.master.after(1000, self.update_timer) # 1000ms의 간격으로 시간을 흘러가게함(1초)
        
    def stop_timer(self): # 타이머를 멈추는 메서드
        if hasattr(self, "timer_id"): # timer_id란 변수가 존재할때 
            self.master.after_cancel(self.timer_id) # 해당 타이머를 취소함
            
    def update_timer(self): # 타이머를 지속적으로 갱신
        self.time_remaining -= 1 # 위의 제한시간을 1씩 감소
        self.update_timer_label() # 라벨에 갱신
        
        if self.time_remaining <= 0: # 남은 시간이 0이면
            self.game_over = True # you are die~~~~~~~~~~~~~~~
            messagebox.showerror("시간제한", "시간이 지났으므로 이번차례 플레이어는 자동으로 패배합니다") # 자동 패배처리
            self.stop_timer() # 타이머를 멈춘다음
            sys.exit() # 프로세스를 종료
        elif not self.game_over: # 게임오버가 아닌 상황
            self.timer_id = self.master.after(1000, self.update_timer) # 타이머를 지속적으로 1초씩 갱신
                  
    def update_timer_label(self): # 남은 시간표시를 라벨로 구현하는 메서드
        self.time_label.config(text=f"시간 제한 : {self.time_remaining}", relief="sunken",border=3) # 아래쪽 라벨을 지속적으로 갱신해줌
        
def main(): # tkinterface 자체를 구현하는 메서드
    root = tk.Tk()
    game = OmokGame(root)
    root.mainloop() # tkinter가 꺼지지않도록 계속 유지하게끔 루프를 한다

if __name__ == "__main__": # 이 파일을 직접 실행했을 때만 main코드를 구동한다(안전장치)
    main()