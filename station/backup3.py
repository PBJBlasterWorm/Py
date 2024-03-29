from tkinter import *
import tkinter.ttk as ttk
from datetime import datetime
import heapq
from tkinter import messagebox

# 역 사이의 거리 정보
station_distances = {
    "출발역": {"도착역1": 10, "도착역2": 20, "도착역3": 15},
    "도착역1": {"출발역": 10, "도착역2": 5, "도착역3": 30},
    "도착역2": {"출발역": 20, "도착역1": 5, "도착역3": 8},
    "도착역3": {"출발역": 15, "도착역1": 30, "도착역2": 8}
}

def dijkstra(start, end):
    # 출발역에서 각 역까지의 최단 거리를 저장할 딕셔너리
    shortest_distance = {station: float('inf') for station in station_distances}
    shortest_distance[start] = 0  # 출발역까지의 거리는 0으로 설정
    # 우선순위 큐를 사용하여 최단 거리를 찾음
    queue = [(0, start)]  # (거리, 역)의 튜플을 우선순위 큐에 넣음
    while queue:
        current_distance, current_station = heapq.heappop(queue)  # 가장 가까운 역 선택
        if current_distance > shortest_distance[current_station]:
            continue  # 이미 최단 거리를 찾은 경우 건너뜀
        for neighbor_station, distance in station_distances[current_station].items():
            distance += current_distance
            if distance < shortest_distance[neighbor_station]:
                shortest_distance[neighbor_station] = distance
                heapq.heappush(queue, (distance, neighbor_station))
    return shortest_distance[end]

def set_start_station(e):
    selected_station = start_combobox.get()
    start_station_entry.delete(0, END)
    start_station_entry.insert(0, selected_station)
    
def set_end_station(e):
    selected_station = end_combobox.get()
    end_station_entry.delete(0, END)
    end_station_entry.insert(0, selected_station)
    
def reset_func1():
    start_station_entry.delete(0, END)
    
def reset_func2():
    end_station_entry.delete(0, END)
    
def time():
    settime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label_3.config(text="현재시각 : " + settime)
    root.after(1000, time)
    
def find_shortest_path():
    start_station = start_combobox.get()
    end_station = end_combobox.get()
    shortest_distance = dijkstra(start_station, end_station)
    messagebox.showinfo("최단 거리", f"{start_station}에서 {end_station}까지의 최단 거리는 {shortest_distance}입니다.")

root = Tk()
root.geometry("1500x1000")
root.resizable(False, False)

# 왼쪽 프레임
frame_1 = Frame(root, relief="solid", bd=1)
frame_1.pack(side="left", fill="both", expand=True)

# 오른쪽 프레임
frame_2 = Frame(root, relief="solid", bd=1)
frame_2.pack(side="right", fill="both", expand=True)

label_1 = Label(frame_1, text="출발 : ", bd=1, relief="sunken", font=("맑은고딕", 20))
label_1.place(x=100, y=150)

label_2 = Label(frame_1, text="도착 : ", bd=1, relief="sunken", font=("맑은고딕", 20))
label_2.place(x=100, y=200)

label_3 = Label(frame_1, text="현재시각 : ", bd=1, relief="sunken", font=("맑은고딕", 20))
label_3.place(x=100, y=250)

start_name = Label(frame_2, text="출발지점", font=("맑은고딕", 20))
start_name.place(x=60, y=100)

start_list = list(station_distances.keys())
start_combobox = ttk.Combobox(frame_2, height=10, values=start_list, state="readonly")
start_combobox.place(x=60, y=140)
start_combobox.set("출발역 선택")
start_combobox.bind("<<ComboboxSelected>>", set_start_station)

end_name = Label(frame_2, text="도착지점", font=("맑은고딕", 20))
end_name.place(x=60, y=200)

end_list = list(station_distances.keys())
end_combobox = ttk.Combobox(frame_2, height=10, values=end_list, state="readonly")
end_combobox.place(x=60, y=240)
end_combobox.set("도착역 선택")
end_combobox.bind("<<ComboboxSelected>>", set_end_station)

searchbutton = Button(frame_2, text="최단거리 찾기", font=("맑은고딕", 15), command=find_shortest_path)
searchbutton.place(x=70, y=280)

resetbutton1 = Button(frame_2, text="초기화", font=("맑은고딕",15), command=reset_func1)
resetbutton1.place(x=300, y=130)

resetbutton2 = Button(frame_2, text="초기화", font=("맑은고딕", 15), command=reset_func2)
resetbutton2.place(x=300, y=230)

start_station_entry = Entry(frame_2)
start_station_entry.place(x=200, y=102, height=25)

end_station_entry = Entry(frame_2)
end_station_entry.place(x=200, y=202, height=25)

time()
root.mainloop()
