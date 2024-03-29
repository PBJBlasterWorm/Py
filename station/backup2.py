import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import copy


win = tk.Tk()
win.geometry('1900x1100+0+0')
win.title("부산 노선도")

def time():
    settime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timelabel.config(text="현재시각 : " + settime)
    win.after(1000, time)
    
def set_start_station(e):
    selected_station = start_combobox.get()
    input_entry.delete(0, END)
    input_entry.insert(0, selected_station)
    
def set_end_station(e):
    selected_station = end_combobox.get()
    destination_entry.delete(0, END)
    destination_entry.insert(0, selected_station)
    
def start_info():
    label_1.config(text="출발 : " + input_entry.get())
    
def end_info():
    label_2.config(text="도착 : " + destination_entry.get())
    
def reset_func():
    input_entry.delete(0, END)
    destination_entry.delete(0, END)
    searchlist1.delete(0, END)
    searchlist2.delete(0, END)
    
def doubleclick1(e):
    double1 = searchlist1.get(ACTIVE)
    input_entry.delete(0, END)
    input_entry.insert(0, double1)
    label_1.config(text="출발 : " + input_entry.get())
    
def doubleclick2(e):
    double2 = searchlist2.get(ACTIVE)
    destination_entry.delete(0, END)
    destination_entry.insert(0, double2)
    label_2.config(text="도착 : " + destination_entry.get())
    
def word1():
    keyword_list = keyword.get(input_entry.get()[0], [])
    searchlist1.delete(0, END)
    for item in keyword_list:
        searchlist1.insert(END, item)
    
    label_1.config(text="출발 : " + input_entry.get())

def word2():
    keyword_list = keyword.get(destination_entry.get()[0], [])
    searchlist2.delete(0, END)
    for item in keyword_list:
        searchlist2.insert(END, item)
        
    label_2.config(text="도착 : " + destination_entry.get())
    
def word3():
    keyword_list = keyword.get(start_combobox.get()[0], [])
    searchlist1.delete(0, END)
    for item in keyword_list:
        searchlist1.insert(END, item)
        
    label_1.config(text="출발 : " + start_combobox.get())
    
def word4():
    keyword_list = keyword.get(end_combobox.get()[0], [])
    searchlist2.delete(0, END)
    for item in keyword_list:
        searchlist2.insert(END, item)
        
    label_2.config(text="도착 : " + end_combobox.get())
    
    
def Enterfunc1(e):
    word1()
    word2()
    
    
def Enterfunc2(e):
    word2()
    word1()
    
    
def Enterfunc3(e):
    word3()
    
def Enterfunc4(e):
    word4()
    
def btnfunc1(station_name):
    # 역 이름에 해당하는 좌표를 찾음
    station_x, station_y = None, None
    if station_name in subway_stations_1:
        station_x, station_y = subway_stations_1[station_name]
    elif station_name in subway_stations_2:
        station_x, station_y = subway_stations_2[station_name]
    elif station_name in subway_stations_3:
        station_x, station_y = subway_stations_3[station_name]
    elif station_name in subway_stations_4:
        station_x, station_y = subway_stations_4[station_name]
    elif station_name in subway_stations_Donhae:
        station_x, station_y = subway_stations_Donhae[station_name]
    elif station_name in subway_stations_BusanGimhae:
        station_x, station_y = subway_stations_BusanGimhae[station_name]
        
    # 빨간 점 생성 및 역 이름 입력
    if station_x is not None and station_y is not None:
        traincanvas.delete("red_dot")  # 기존의 빨간 점 삭제
        traincanvas.create_oval(station_x - 5, station_y - 5, station_x + 5, station_y + 5, fill='red', tags="red_dot")

        # if input_entry.get() == "":  # 출발역이 입력되지 않은 경우
        #     input_entry.delete(0, tk.END)
        #     input_entry.insert(0, station_name)  # 출발역 입력
        # else:
        #     destination_entry.delete(0, tk.END)
        #     destination_entry.insert(0, station_name)  # 도착역 입력

    
def changeentry():
    input_entry_val = input_entry.get()
    destination_entry_val = destination_entry.get()
    
    temp = input_entry_val
    input_entry_val = destination_entry_val
    destination_entry_val = temp
    
    input_entry.delete(0, END)
    input_entry.insert(0, input_entry_val)
    destination_entry.delete(0, END)    
    destination_entry.insert(0, destination_entry_val)
    
    label_1.config(text="출발 : " + input_entry.get())
    label_2.config(text="도착 : " + destination_entry.get())
    
def first(event):
    firstshow = tk.Toplevel(sub1)
    firstshow.geometry("1500x450+300+300")
    firstimage = Image.open("station/1호노선.png")
    refirst = firstimage.resize((1500,450))
    firstimg = ImageTk.PhotoImage(refirst)
    firstlabel = Label(firstshow, image=firstimg)
    firstlabel.image = firstimg
    firstlabel.pack()
    firstlabel.focus_set()
    
def second(event):
    secondshow = tk.Toplevel(sub2)
    secondshow.geometry("1500x450+300+300")
    secondimage = Image.open("station/2호노선.png")
    resecond = secondimage.resize((1500,450))
    secondimg = ImageTk.PhotoImage(resecond)
    secondlabel = Label(secondshow, image=secondimg)
    secondlabel.image = secondimg
    secondlabel.pack()
    secondlabel.focus_set()
    
def third(event):
    thirdshow = tk.Toplevel(sub3)
    thirdshow.geometry("1500x450+300+300")
    thirdimage = Image.open("station/3호노선.png")
    rethird = thirdimage.resize((1500,450))
    thirdimg = ImageTk.PhotoImage(rethird)
    thirdlabel = Label(thirdshow, image=thirdimg)
    thirdlabel.image = thirdimg
    thirdlabel.pack()
    thirdlabel.focus_set()

def four(event):
    fourshow = tk.Toplevel(sub4)
    fourshow.geometry("1500x450+300+300")
    fourimage = Image.open("station/4호노선.png")
    refour = fourimage.resize((1500,450))
    fourimg = ImageTk.PhotoImage(refour)
    fourlabel = Label(fourshow, image=fourimg)
    fourlabel.image = fourimg
    fourlabel.pack()
    fourlabel.focus_set()
    
def donghae(event):
    donghaeshow = tk.Toplevel(sub5)
    donghaeshow.geometry("1500x450+300+300")
    donghaeimage = Image.open("station/동해노선.png")
    redonghae = donghaeimage.resize((1500,450))
    donghaeimg = ImageTk.PhotoImage(redonghae)
    donglabel = Label(donghaeshow, image=donghaeimg)
    donglabel.image = donghaeimg
    donglabel.pack()
    donglabel.focus_set()
    
def kimhae(event):
    kimhaeshow = tk.Toplevel(sub6)
    kimhaeshow.geometry("1500x450+300+300")
    kimhaeimage = Image.open("station/부산김해노선.png")
    rekimhae = kimhaeimage.resize((1500,450))
    kimhaeimg = ImageTk.PhotoImage(rekimhae)
    kimlabel = Label(kimhaeshow, image=kimhaeimg)
    kimlabel.image = kimhaeimg
    kimlabel.pack()
    kimlabel.focus_set()

def newwindow1():
    window = tk.Toplevel(btn1)
    window.geometry("150x50+1705+78")
    winlabel = Label(window, text="출발 : 노포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("노포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("노포"))
    endbtn.pack(side=RIGHT)
    
def newwindow2():
    window = tk.Toplevel(btn2)
    window.geometry("150x50+1743+78")
    winlabel = Label(window, text="출발 : 범어사")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("범어사"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("범어사"))
    endbtn.pack(side=RIGHT)
    
def newwindow3():
    window = tk.Toplevel(btn3)
    window.geometry("150x50+1672+78")
    winlabel = Label(window, text="출발 : 남산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("남산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("남산"))
    endbtn.pack(side=RIGHT)
    
def newwindow4():
    window = tk.Toplevel(btn4)
    window.geometry("150x50+1600+78")
    winlabel = Label(window, text="출발 : 두실")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("두실"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("두실"))
    endbtn.pack(side=RIGHT)
    
def newwindow5():
    window = tk.Toplevel(btn5)
    window.geometry("150x50+1529+78")
    winlabel = Label(window, text="출발 : 선릉")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("선릉"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("선릉"))
    endbtn.pack(side=RIGHT)
    
def newwindow6():
    window = tk.Toplevel(btn6)
    window.geometry("150x50+1457+78")
    winlabel = Label(window, text="출발 : 장전")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("장전"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("장전"))
    endbtn.pack(side=RIGHT)
    
def newwindow7():
    window = tk.Toplevel(btn7)
    window.geometry("150x50+1386+78")
    winlabel = Label(window, text="출발 : 부산대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부산대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부산대"))
    endbtn.pack(side=RIGHT)
    
def newwindow8():
    window = tk.Toplevel(btn8)
    window.geometry("150x50+1315+78")
    winlabel = Label(window, text="출발 : 온천장")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("온천장"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("온천장"))
    endbtn.pack(side=RIGHT)
    
def newwindow9():
    window = tk.Toplevel(btn9)
    window.geometry("150x50+1243+78")
    winlabel = Label(window, text="출발 : 명륜")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("명륜"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("명륜"))
    endbtn.pack(side=RIGHT)
    
def newwindow10():
    window = tk.Toplevel(btn10)
    window.geometry("150x50+1207+231")
    winlabel = Label(window, text="출발 : 동래")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동래"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동래"))
    endbtn.pack(side=RIGHT)
    
def newwindow11():
    window = tk.Toplevel(btn11)
    window.geometry("150x50+1207+365")
    winlabel = Label(window, text="출발 : 교대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("교대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("교대"))
    endbtn.pack(side=RIGHT)
    
def newwindow12():
    window = tk.Toplevel(btn12)
    window.geometry("150x50+1207+490")
    winlabel = Label(window, text="출발 : 연산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("연산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("연산"))
    endbtn.pack(side=RIGHT)
    
def newwindow13():
    window = tk.Toplevel(btn13)
    window.geometry("150x50+1207+562")
    winlabel = Label(window, text="출발 : 시청")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("시청"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("시청"))
    endbtn.pack(side=RIGHT)
    
def newwindow14():
    window = tk.Toplevel(btn14)
    window.geometry("150x50+1207+646")
    winlabel = Label(window, text="출발 : 양정")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("양정"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("양정"))
    endbtn.pack(side=RIGHT)
    
def newwindow15():
    window = tk.Toplevel(btn15)
    window.geometry("150x50+1207+730")
    winlabel = Label(window, text="출발 : 부전")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부전"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부전"))
    endbtn.pack(side=RIGHT)

def newwindow16():
    window = tk.Toplevel(btn16)
    window.geometry("150x50+1207+817")
    winlabel = Label(window, text="출발 : 서면")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("서면"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("서면"))
    endbtn.pack(side=RIGHT)
    
def newwindow17():
    window = tk.Toplevel(btn17)
    window.geometry("150x50+1207+889")
    winlabel = Label(window, text="출발 : 범내골")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("범내골"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("범내골"))
    endbtn.pack(side=RIGHT)
    
def newwindow18():
    window = tk.Toplevel(btn18)
    window.geometry("150x50+1207+960")
    winlabel = Label(window, text="출발 : 범일")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("범일"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("범일"))
    endbtn.pack(side=RIGHT)
    
def newwindow19():
    window = tk.Toplevel(btn19)
    window.geometry("150x50+1178+1000")
    winlabel = Label(window, text="출발 : 좌천(1호선)")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("좌천(1호선)"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("좌천(1호선)"))
    endbtn.pack(side=RIGHT)
    
def newwindow20():
    window = tk.Toplevel(btn20)
    window.geometry("150x50+1144+1000")
    winlabel = Label(window, text="출발 : 부산진")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부산진"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부산진"))
    endbtn.pack(side=RIGHT)
    
def newwindow21():
    window = tk.Toplevel(btn21)
    window.geometry("150x50+1111+1000")
    winlabel = Label(window, text="출발 : 초량")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("초량"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("초량"))
    endbtn.pack(side=RIGHT)
    
def newwindow22():
    window = tk.Toplevel(btn22)
    window.geometry("150x50+1077+1000")
    winlabel = Label(window, text="출발 : 부산역")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부산역"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부산역"))
    endbtn.pack(side=RIGHT)
    
def newwindow23():
    window = tk.Toplevel(btn23)
    window.geometry("150x50+1043+1000")
    winlabel = Label(window, text="출발 : 중앙")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("중앙"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("중앙"))
    endbtn.pack(side=RIGHT)
    
def newwindow24():
    window = tk.Toplevel(btn24)
    window.geometry("150x50+1010+1000")
    winlabel = Label(window, text="출발 : 남포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("남포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("남포"))
    endbtn.pack(side=RIGHT)
    
def newwindow25():
    window = tk.Toplevel(btn25)
    window.geometry("150x50+977+1000")
    winlabel = Label(window, text="출발 : 자갈치")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("자갈치"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("자갈치"))
    endbtn.pack(side=RIGHT)

def newwindow26():
    window = tk.Toplevel(btn26)
    window.geometry("150x50+943+1000")
    winlabel = Label(window, text="출발 : 토성")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("토성"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("토성"))
    endbtn.pack(side=RIGHT)
    
def newwindow27():
    window = tk.Toplevel(btn27)
    window.geometry("150x50+910+1000")
    winlabel = Label(window, text="출발 : 동대신")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동대신"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동대신"))
    endbtn.pack(side=RIGHT)
    
def newwindow28():
    window = tk.Toplevel(btn28)
    window.geometry("150x50+876+1000")
    winlabel = Label(window, text="출발 : 서대신")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("서대신"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("서대신"))
    endbtn.pack(side=RIGHT)
    
def newwindow29():
    window = tk.Toplevel(btn29)
    window.geometry("150x50+843+1000")
    winlabel = Label(window, text="출발 : 대티")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("대티"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("대티"))
    endbtn.pack(side=RIGHT)
    
def newwindow30():
    window = tk.Toplevel(btn30)
    window.geometry("150x50+810+1000")
    winlabel = Label(window, text="출발 : 과정")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("과정"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("과정"))
    endbtn.pack(side=RIGHT)
    
def newwindow31():
    window = tk.Toplevel(btn31)
    window.geometry("150x50+776+1000")
    winlabel = Label(window, text="출발 : 사하")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("사하"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("사하"))
    endbtn.pack(side=RIGHT)
    
def newwindow32():
    window = tk.Toplevel(btn32)
    window.geometry("150x50+743+1000")
    winlabel = Label(window, text="출발 : 당리")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("당리"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("당리"))
    endbtn.pack(side=RIGHT)
    
def newwindow33():
    window = tk.Toplevel(btn33)
    window.geometry("150x50+709+1000")
    winlabel = Label(window, text="출발 : 하단")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("하단"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("하단"))
    endbtn.pack(side=RIGHT)
    
def newwindow34():
    window = tk.Toplevel(btn34)
    window.geometry("150x50+675+1000")
    winlabel = Label(window, text="출발 : 신평")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("신평"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("신평"))
    endbtn.pack(side=RIGHT)
    
def newwindow35():
    window = tk.Toplevel(btn35)
    window.geometry("150x50+641+1000")
    winlabel = Label(window, text="출발 : 동매")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동매"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동매"))
    endbtn.pack(side=RIGHT)
    
def newwindow36():
    window = tk.Toplevel(btn36)
    window.geometry("150x50+608+1000")
    winlabel = Label(window, text="출발 : 장림")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("장림"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("장림"))
    endbtn.pack(side=RIGHT)
    
def newwindow37():
    window = tk.Toplevel(btn37)
    window.geometry("150x50+575+1000")
    winlabel = Label(window, text="출발 : 신장림")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("신장림"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("신장림"))
    endbtn.pack(side=RIGHT)
    
def newwindow38():
    window = tk.Toplevel(btn38)
    window.geometry("150x50+542+1000")
    winlabel = Label(window, text="출발 : 낫개")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("낫개"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("낫개"))
    endbtn.pack(side=RIGHT)
    
def newwindow39():
    window = tk.Toplevel(btn39)
    window.geometry("150x50+508+1000")
    winlabel = Label(window, text="출발 : 다대포항")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("다대포항"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("다대포항"))
    endbtn.pack(side=RIGHT)
    
def newwindow40():
    window = tk.Toplevel(btn40)
    window.geometry("150x50+474+1000")
    winlabel = Label(window, text="출발 : 다대포해수욕장")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("다대포해수욕장"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("다대포해수욕장"))
    endbtn.pack(side=RIGHT)
    
def newwindow41():
    window = tk.Toplevel(btn41)
    window.geometry("150x50+1128+78")
    winlabel = Label(window, text="출발 : 양산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("양산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("양산"))
    endbtn.pack(side=RIGHT)
    
def newwindow42():
    window = tk.Toplevel(btn42)
    window.geometry("150x50+1082+78")
    winlabel = Label(window, text="출발 : 남양산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("남양산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("남양산"))
    endbtn.pack(side=RIGHT)
    
def newwindow43():
    window = tk.Toplevel(btn43)
    window.geometry("150x50+1035+78")
    winlabel = Label(window, text="출발 : 부산대중앙캠퍼스")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부산대중앙캠퍼스"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부산대중앙캠퍼스"))
    endbtn.pack(side=RIGHT)
    
def newwindow44():
    window = tk.Toplevel(btn44)
    window.geometry("150x50+986+78")
    winlabel = Label(window, text="출발 : 중산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("중산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("중산"))
    endbtn.pack(side=RIGHT)
    
def newwindow45():
    window = tk.Toplevel(btn45)
    window.geometry("150x50+939+78")
    winlabel = Label(window, text="출발 : 호포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("호포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("호포"))
    endbtn.pack(side=RIGHT)

def newwindow46():
    window = tk.Toplevel(btn46)
    window.geometry("150x50+892+78")
    winlabel = Label(window, text="출발 : 금곡")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("금곡"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("금곡"))
    endbtn.pack(side=RIGHT)
    
def newwindow47():
    window = tk.Toplevel(btn47)
    window.geometry("150x50+845+84")
    winlabel = Label(window, text="출발 : 동원")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동원"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동원"))
    endbtn.pack(side=RIGHT)
    
def newwindow48():
    window = tk.Toplevel(btn48)
    window.geometry("150x50+829+128")
    winlabel = Label(window, text="출발 : 율리")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("율리"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("율리"))
    endbtn.pack(side=RIGHT)
    
def newwindow49():
    window = tk.Toplevel(btn49)
    window.geometry("150x50+829+268")
    winlabel = Label(window, text="출발 : 화명")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("화명"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("화명"))
    endbtn.pack(side=RIGHT)
    
def newwindow50():
    window = tk.Toplevel(btn50)
    window.geometry("150x50+829+371")
    winlabel = Label(window, text="출발 : 수정")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("수정"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("수정"))
    endbtn.pack(side=RIGHT)
    
def newwindow51():
    window = tk.Toplevel(btn51)
    window.geometry("150x50+829+71")
    winlabel = Label(window, text="출발 : 덕천")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("덕천"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("덕천"))
    endbtn.pack(side=RIGHT)
    
def newwindow52():
    window = tk.Toplevel(btn52)
    window.geometry("150x50+829+541")
    winlabel = Label(window, text="출발 : 구명")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("구명"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("구명"))
    endbtn.pack(side=RIGHT)
    
def newwindow53():
    window = tk.Toplevel(btn53)
    window.geometry("150x50+829+599")
    winlabel = Label(window, text="출발 : 구남")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("구남"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("구남"))
    endbtn.pack(side=RIGHT)
    
def newwindow54():
    window = tk.Toplevel(btn54)
    window.geometry("150x50+829+655")
    winlabel = Label(window, text="출발 : 모라")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("모라"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("모라"))
    endbtn.pack(side=RIGHT)
    
def newwindow55():
    window = tk.Toplevel(btn55)
    window.geometry("150x50+829+712")
    winlabel = Label(window, text="출발 : 모덕")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("모덕"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("모덕"))
    endbtn.pack(side=RIGHT)
    
def newwindow56():
    window = tk.Toplevel(btn56)
    window.geometry("150x50+829+767")
    winlabel = Label(window, text="출발 : 덕포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("덕포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("덕포"))
    endbtn.pack(side=RIGHT)
    
def newwindow57():
    window = tk.Toplevel(btn57)
    window.geometry("150x50+853+817")
    winlabel = Label(window, text="출발 : 사상")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("사상"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("사상"))
    endbtn.pack(side=RIGHT)
    
def newwindow58():
    window = tk.Toplevel(btn58)
    window.geometry("150x50+904+817")
    winlabel = Label(window, text="출발 : 감전")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("감전"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("감전"))
    endbtn.pack(side=RIGHT)
    
def newwindow59():
    window = tk.Toplevel(btn59)
    window.geometry("150x50+947+817")
    winlabel = Label(window, text="출발 : 주례")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("주례"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("주례"))
    endbtn.pack(side=RIGHT)
    
def newwindow60():
    window = tk.Toplevel(btn60)
    window.geometry("150x50+989+817")
    winlabel = Label(window, text="출발 : 냉정")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("냉정"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("냉정"))
    endbtn.pack(side=RIGHT)
    
def newwindow61():
    window = tk.Toplevel(btn61)
    window.geometry("150x50+1032+817")
    winlabel = Label(window, text="출발 : 개금")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("개금"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("개금"))
    endbtn.pack(side=RIGHT)
    
def newwindow62():
    window = tk.Toplevel(btn62)
    window.geometry("150x50+1075+817")
    winlabel = Label(window, text="출발 : 동의대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동의대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동의대"))
    endbtn.pack(side=RIGHT)
    
def newwindow63():
    window = tk.Toplevel(btn63)
    window.geometry("150x50+1119+817")
    winlabel = Label(window, text="출발 : 가야")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("가야"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("가야"))
    endbtn.pack(side=RIGHT)
    
def newwindow64():
    window = tk.Toplevel(btn64)
    window.geometry("150x50+947+817")
    winlabel = Label(window, text="출발 : 부암")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부암"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부암"))
    endbtn.pack(side=RIGHT)
    
def newwindow65():
    window = tk.Toplevel(btn65)
    window.geometry("150x50+1253+817")
    winlabel = Label(window, text="출발 : 전포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("전포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("전포"))
    endbtn.pack(side=RIGHT)
    
def newwindow66():
    window = tk.Toplevel(btn66)
    window.geometry("150x50+829+767")
    winlabel = Label(window, text="출발 : 국제금융센터·부산은행")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("국제금융센터·부산은행"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("국제금융센터·부산은행"))
    endbtn.pack(side=RIGHT)
    
def newwindow67():
    window = tk.Toplevel(btn67)
    window.geometry("150x50+1315+817")
    winlabel = Label(window, text="출발 : 문현")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("문현"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("문현"))
    endbtn.pack(side=RIGHT)
    
def newwindow68():
    window = tk.Toplevel(btn68)
    window.geometry("150x50+1347+817")
    winlabel = Label(window, text="출발 : 지게골")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("지게골"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("지게골"))
    endbtn.pack(side=RIGHT)
    
def newwindow69():
    window = tk.Toplevel(btn69)
    window.geometry("150x50+1376+817")
    winlabel = Label(window, text="출발 : 못골")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("못골"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("못골"))
    endbtn.pack(side=RIGHT)
    
def newwindow70():
    window = tk.Toplevel(btn70)
    window.geometry("150x50+1406+817")
    winlabel = Label(window, text="출발 : 대연")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("대연"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("대연"))
    endbtn.pack(side=RIGHT)
 

def newwindow71():
    window = tk.Toplevel(btn71)
    window.geometry("150x50+1439+817")
    winlabel = Label(window, text="출발 : 경성대·부경대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("경성대·부경대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("경성대·부경대"))
    endbtn.pack(side=RIGHT)
    
def newwindow72():
    window = tk.Toplevel(btn72)
    window.geometry("150x50+1441+715")
    winlabel = Label(window, text="출발 : 남천")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("남천"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("남천"))
    endbtn.pack(side=RIGHT)
    
def newwindow73():
    window = tk.Toplevel(btn73)
    window.geometry("150x50+1441+645")
    winlabel = Label(window, text="출발 : 금련산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("금련산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("금련산"))
    endbtn.pack(side=RIGHT)
    
def newwindow74():
    window = tk.Toplevel(btn74)
    window.geometry("150x50+1441+574")
    winlabel = Label(window, text="출발 : 광안")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("광안"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("광안"))
    endbtn.pack(side=RIGHT)
    
def newwindow75():
    window = tk.Toplevel(btn75)
    window.geometry("150x50+1455+490")
    winlabel = Label(window, text="출발 : 수영")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("수영"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("수영"))
    endbtn.pack(side=RIGHT)
    
def newwindow76():
    window = tk.Toplevel(btn76)
    window.geometry("150x50+1513+490")
    winlabel = Label(window, text="출발 : 민락")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("민락"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("민락"))
    endbtn.pack(side=RIGHT)
    
def newwindow77():
    window = tk.Toplevel(btn77)
    window.geometry("150x50+1572+490")
    winlabel = Label(window, text="출발 : 센텀시티")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("센텀시티"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("센텀시티"))
    endbtn.pack(side=RIGHT)
    
def newwindow78():
    window = tk.Toplevel(btn78)
    window.geometry("150x50+1626+490")
    winlabel = Label(window, text="출발 : 벡스코(시립미술관)")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("벡스코(시립미술관)"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("벡스코(시립미술관)"))
    endbtn.pack(side=RIGHT)
    
def newwindow79():
    window = tk.Toplevel(btn79)
    window.geometry("150x50+1677+490")
    winlabel = Label(window, text="출발 : 동백")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동백"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동백"))
    endbtn.pack(side=RIGHT)
    
def newwindow80():
    window = tk.Toplevel(btn80)
    window.geometry("150x50+1722+490")
    winlabel = Label(window, text="출발 : 해운대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("해운대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("해운대"))
    endbtn.pack(side=RIGHT)
    
def newwindow81():
    window = tk.Toplevel(btn81)
    window.geometry("150x50+1768+490")
    winlabel = Label(window, text="출발 : 중동")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("중동"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("중동"))
    endbtn.pack(side=RIGHT)
    
def newwindow82():
    window = tk.Toplevel(btn82)
    window.geometry("150x50+1815+490")
    winlabel = Label(window, text="출발 : 장산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("장산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("장산"))
    endbtn.pack(side=RIGHT)
    
def newwindow83():
    window = tk.Toplevel(btn83)
    window.geometry("150x50+474+490")
    winlabel = Label(window, text="출발 : 대저")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("대저"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("대저"))
    endbtn.pack(side=RIGHT)
    
def newwindow84():
    window = tk.Toplevel(btn84)
    window.geometry("150x50+565+490")
    winlabel = Label(window, text="출발 : 체육공원")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("체육공원"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("체육공원"))
    endbtn.pack(side=RIGHT)
    
def newwindow85():
    window = tk.Toplevel(btn85)
    window.geometry("150x50+653+490")
    winlabel = Label(window, text="출발 : 강서구청")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("강서구청"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("강서구청"))
    endbtn.pack(side=RIGHT)
    
def newwindow86():
    window = tk.Toplevel(btn86)
    window.geometry("150x50+742+490")
    winlabel = Label(window, text="출발 : 구포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("구포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("구포"))
    endbtn.pack(side=RIGHT)
    
def newwindow87():
    window = tk.Toplevel(btn87)
    window.geometry("150x50+888+490")
    winlabel = Label(window, text="출발 : 숙동")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("숙동"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("숙동"))
    endbtn.pack(side=RIGHT)
    
def newwindow88():
    window = tk.Toplevel(btn88)
    window.geometry("150x50+932+490")
    winlabel = Label(window, text="출발 : 남산정")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("남산정"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("남산정"))
    endbtn.pack(side=RIGHT)
    
def newwindow89():
    window = tk.Toplevel(btn89)
    window.geometry("150x50+565978+490")
    winlabel = Label(window, text="출발 : 만덕")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("만덕"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("만덕"))
    endbtn.pack(side=RIGHT)
    
def newwindow90():
    window = tk.Toplevel(btn90)
    window.geometry("150x50+1011+490")
    winlabel = Label(window, text="출발 : 미남")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("미남"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("미남"))
    endbtn.pack(side=RIGHT)
    
def newwindow91():
    window = tk.Toplevel(btn91)
    window.geometry("150x50+1058+490")
    winlabel = Label(window, text="출발 : 사직")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("사직"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("사직"))
    endbtn.pack(side=RIGHT)
    
def newwindow92():
    window = tk.Toplevel(btn92)
    window.geometry("150x50+1094+490")
    winlabel = Label(window, text="출발 : 종합운동장")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("종합운동장"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("종합운동장"))
    endbtn.pack(side=RIGHT)
    
def newwindow93():
    window = tk.Toplevel(btn93)
    window.geometry("150x50+1139+490")
    winlabel = Label(window, text="출발 : 거제")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("거제"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("거제"))
    endbtn.pack(side=RIGHT)
    
def newwindow94():
    window = tk.Toplevel(btn94)
    window.geometry("150x50+1267+490")
    winlabel = Label(window, text="출발 : 물만골")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("물만골"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("물만골"))
    endbtn.pack(side=RIGHT)
    
def newwindow95():
    window = tk.Toplevel(btn95)
    window.geometry("150x50+1322+490")
    winlabel = Label(window, text="출발 : 배산")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("배산"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("배산"))
    endbtn.pack(side=RIGHT)
    
def newwindow96():
    window = tk.Toplevel(btn96)
    window.geometry("150x50+1455+490")
    winlabel = Label(window, text="출발 : 수영")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("수영"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("수영"))
    endbtn.pack(side=RIGHT)
    
def newwindow97():
    window = tk.Toplevel(btn97)
    window.geometry("150x50+1815+231")
    winlabel = Label(window, text="출발 : 안평")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("안평"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("안평"))
    endbtn.pack(side=RIGHT)
    
def newwindow98():
    window = tk.Toplevel(btn98)
    window.geometry("150x50+1764+231")
    winlabel = Label(window, text="출발 : 고촌")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("고촌"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("고촌"))
    endbtn.pack(side=RIGHT)
    
def newwindow99():
    window = tk.Toplevel(btn99)
    window.geometry("150x50+1714+231")
    winlabel = Label(window, text="출발 : 윗반송")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("윗반송"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("윗반송"))
    endbtn.pack(side=RIGHT)
    
def newwindow100():
    window = tk.Toplevel(btn100)
    window.geometry("150x50+1663+231")
    winlabel = Label(window, text="출발 : 영산대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("영산대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("영산대"))
    endbtn.pack(side=RIGHT)
    
def newwindow101():
    window = tk.Toplevel(btn101)
    window.geometry("150x50+1613+231")
    winlabel = Label(window, text="출발 : 석대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("석대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("석대"))
    endbtn.pack(side=RIGHT)
    
def newwindow102():
    window = tk.Toplevel(btn102)
    window.geometry("150x50+1563+231")
    winlabel = Label(window, text="출발 : 반여농산물시장")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("반여농산물시장"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("반여농산물시장"))
    endbtn.pack(side=RIGHT)
    
def newwindow103():
    window = tk.Toplevel(btn103)
    window.geometry("150x50+1513+231")
    winlabel = Label(window, text="출발 : 금사")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("금사"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("금사"))
    endbtn.pack(side=RIGHT)
    
def newwindow104():
    window = tk.Toplevel(btn104)
    window.geometry("150x50+1462+231")
    winlabel = Label(window, text="출발 : 서동")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("서동"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("서동"))
    endbtn.pack(side=RIGHT)
    
def newwindow105():
    window = tk.Toplevel(btn105)
    window.geometry("150x50+1412+231")
    winlabel = Label(window, text="출발 : 명장")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("명장"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("명장"))
    endbtn.pack(side=RIGHT)
    
def newwindow106():
    window = tk.Toplevel(btn106)
    window.geometry("150x50+1362+231")
    winlabel = Label(window, text="출발 : 충렬사")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("충렬사"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("충렬사"))
    endbtn.pack(side=RIGHT)
    
def newwindow107():
    window = tk.Toplevel(btn107)
    window.geometry("150x50+1308+231")
    winlabel = Label(window, text="출발 : 낙민")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("낙민"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("낙민"))
    endbtn.pack(side=RIGHT)
    
def newwindow108():
    window = tk.Toplevel(btn108)
    window.geometry("150x50+1261+231")
    winlabel = Label(window, text="출발 : 수안")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("수안"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("수안"))
    endbtn.pack(side=RIGHT)
    
def newwindow109():
    window = tk.Toplevel(btn109)
    window.geometry("150x50+1815+816")
    winlabel = Label(window, text="출발 : 태화강")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("태화강"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("태화강"))
    endbtn.pack(side=RIGHT)
    
def newwindow110():
    window = tk.Toplevel(btn110)
    window.geometry("150x50+1790+816")
    winlabel = Label(window, text="출발 : 개운포")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("개운포"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("개운포"))
    endbtn.pack(side=RIGHT)
    
def newwindow111():
    window = tk.Toplevel(btn111)
    window.geometry("150x50+2366+816")
    winlabel = Label(window, text="출발 : 덕하")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("덕하"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("덕하"))
    endbtn.pack(side=RIGHT)
    
def newwindow112():
    window = tk.Toplevel(btn112)
    window.geometry("150x50+1741+816")
    winlabel = Label(window, text="출발 : 망양")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("망양"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("망양"))
    endbtn.pack(side=RIGHT)
    
def newwindow113():
    window = tk.Toplevel(btn113)
    window.geometry("150x50+1717+816")
    winlabel = Label(window, text="출발 : 남창")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("남창"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("남창"))
    endbtn.pack(side=RIGHT)
    
def newwindow114():
    window = tk.Toplevel(btn114)
    window.geometry("150x50+1693+816")
    winlabel = Label(window, text="출발 : 서생")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("서생"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("서생"))
    endbtn.pack(side=RIGHT)
    
def newwindow115():
    window = tk.Toplevel(btn115)
    window.geometry("150x50+1669+816")
    winlabel = Label(window, text="출발 : 월내")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("월내"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("월내"))
    endbtn.pack(side=RIGHT)
    
def newwindow116():
    window = tk.Toplevel(btn116)
    window.geometry("150x50+1626+760")
    winlabel = Label(window, text="출발 : 좌천(동해선)")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("좌천(동해선)"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("좌천(동해선)"))
    endbtn.pack(side=RIGHT)
    
def newwindow117():
    window = tk.Toplevel(btn117)
    window.geometry("150x50+1626+717")
    winlabel = Label(window, text="출발 : 일광")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("일광"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("일광"))
    endbtn.pack(side=RIGHT)
    
def newwindow118():
    window = tk.Toplevel(btn118)
    window.geometry("150x50+1626+674")
    winlabel = Label(window, text="출발 : 기장")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("기장"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("기장"))
    endbtn.pack(side=RIGHT)
    
def newwindow119():
    window = tk.Toplevel(btn119)
    window.geometry("150x50+1626+631")
    winlabel = Label(window, text="출발 : 오시리아")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("오시리아"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("오시리아"))
    endbtn.pack(side=RIGHT)
    
def newwindow120():
    window = tk.Toplevel(btn120)
    window.geometry("150x50+1626+588")
    winlabel = Label(window, text="출발 : 송정")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("송정"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("송정"))
    endbtn.pack(side=RIGHT)
    
def newwindow121():
    window = tk.Toplevel(btn121)
    window.geometry("150x50+1626+545")
    winlabel = Label(window, text="출발 : 신해운대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("신해운대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("신해운대"))
    endbtn.pack(side=RIGHT)
    
def newwindow122():
    window = tk.Toplevel(btn122)
    window.geometry("150x50+1605+365")
    winlabel = Label(window, text="출발 : 센텀")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("센텀"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("센텀"))
    endbtn.pack(side=RIGHT)
    
def newwindow123():
    window = tk.Toplevel(btn123)
    window.geometry("150x50+1526+365")
    winlabel = Label(window, text="출발 : 재송")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("재송"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("재송"))
    endbtn.pack(side=RIGHT)
    
def newwindow124():
    window = tk.Toplevel(btn124)
    window.geometry("150x50+1447+365")
    winlabel = Label(window, text="출발 : 부산원동")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부산원동"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부산원동"))
    endbtn.pack(side=RIGHT)
    
def newwindow125():
    window = tk.Toplevel(btn125)
    window.geometry("150x50+1369+365")
    winlabel = Label(window, text="출발 : 안락")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("안락"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("안락"))
    endbtn.pack(side=RIGHT)
    
def newwindow126():
    window = tk.Toplevel(btn126)
    window.geometry("150x50+1291+365")
    winlabel = Label(window, text="출발 : 동래(동해선)")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("동래(동해선)"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("동래(동해선)"))
    endbtn.pack(side=RIGHT)
    
def newwindow127():
    window = tk.Toplevel(btn127)
    window.geometry("150x50+1139+594")
    winlabel = Label(window, text="출발 : 거제해맞이")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("거제해맞이"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("거제해맞이"))
    endbtn.pack(side=RIGHT)
    
def newwindow128():
    window = tk.Toplevel(btn128)
    window.geometry("150x50+1139+701")
    winlabel = Label(window, text="출발 : 부전")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부전"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부전"))
    endbtn.pack(side=RIGHT)
    
def newwindow129():
    window = tk.Toplevel(btn129)
    window.geometry("150x50+808+78")
    winlabel = Label(window, text="출발 : 가야대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("가야대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("가야대"))
    endbtn.pack(side=RIGHT)
    
def newwindow130():
    window = tk.Toplevel(btn130)
    window.geometry("150x50+775+78")
    winlabel = Label(window, text="출발 : 장신대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("장신대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("장신대"))
    endbtn.pack(side=RIGHT)
    
def newwindow131():
    window = tk.Toplevel(btn131)
    window.geometry("150x50+738+78")
    winlabel = Label(window, text="출발 : 연지공원")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("연지공원"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("연지공원"))
    endbtn.pack(side=RIGHT)
    
def newwindow132():
    window = tk.Toplevel(btn132)
    window.geometry("150x50+701+78")
    winlabel = Label(window, text="출발 : 박물관")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("박물관"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("박물관"))
    endbtn.pack(side=RIGHT)
    
def newwindow133():
    window = tk.Toplevel(btn133)
    window.geometry("150x50+665+78")
    winlabel = Label(window, text="출발 : 수로왕릉")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("수로왕릉"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("수로왕릉"))
    endbtn.pack(side=RIGHT)
    
def newwindow134():
    window = tk.Toplevel(btn134)
    window.geometry("150x50+628+78")
    winlabel = Label(window, text="출발 : 봉황")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("봉황"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("봉황"))
    endbtn.pack(side=RIGHT)
    
def newwindow135():
    window = tk.Toplevel(btn135)
    window.geometry("150x50+592+78")
    winlabel = Label(window, text="출발 : 부원")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("부원"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("부원"))
    endbtn.pack(side=RIGHT)
    
def newwindow136():
    window = tk.Toplevel(btn136)
    window.geometry("150x50+555+78")
    winlabel = Label(window, text="출발 : 김해시청")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("김해시청"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("김해시청"))
    endbtn.pack(side=RIGHT)
    
def newwindow137():
    window = tk.Toplevel(btn137)
    window.geometry("150x50+518+78")
    winlabel = Label(window, text="출발 : 인제대")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("인제대"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("인제대"))
    endbtn.pack(side=RIGHT)
    
def newwindow138():
    window = tk.Toplevel(btn138)
    window.geometry("150x50+485+509")
    winlabel = Label(window, text="출발 : 김해대학")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("김해대학"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("김해대학"))
    endbtn.pack(side=RIGHT)
    
def newwindow139():
    window = tk.Toplevel(btn139)
    window.geometry("150x50+474+153")
    winlabel = Label(window, text="출발 : 지내")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("지내"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("지내"))
    endbtn.pack(side=RIGHT)
    
def newwindow140():
    window = tk.Toplevel(btn140)
    window.geometry("150x50+474+231")
    winlabel = Label(window, text="출발 : 불암")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("불암"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("불암"))
    endbtn.pack(side=RIGHT)
    
def newwindow141():
    window = tk.Toplevel(btn141)
    window.geometry("150x50+474+308")
    winlabel = Label(window, text="출발 : 대사")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("대사"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("대사"))
    endbtn.pack(side=RIGHT)
    
def newwindow142():
    window = tk.Toplevel(btn142)
    window.geometry("150x50+474+386")
    winlabel = Label(window, text="출발 : 평강")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("평강"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("평강"))
    endbtn.pack(side=RIGHT)
    
def newwindow143():
    window = tk.Toplevel(btn143)
    window.geometry("150x50+474+490")
    winlabel = Label(window, text="출발 : 등구")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("등구"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("등구"))
    endbtn.pack(side=RIGHT)
    
def newwindow144():
    window = tk.Toplevel(btn144)
    window.geometry("150x50+474+735")
    winlabel = Label(window, text="출발 : 덕두")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("덕두"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("덕두"))
    endbtn.pack(side=RIGHT)
    
def newwindow145():
    window = tk.Toplevel(btn145)
    window.geometry("150x50+549+817")
    winlabel = Label(window, text="출발 : 공항")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("공항"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("공항"))
    endbtn.pack(side=RIGHT)
    
def newwindow146():
    window = tk.Toplevel(btn146)
    window.geometry("150x50+635+817")
    winlabel = Label(window, text="출발 : 서부산유통지구")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("서부산유통지구"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("서부산유통지구"))
    endbtn.pack(side=RIGHT)
    
def newwindow147():
    window = tk.Toplevel(btn147)
    window.geometry("150x50+720+817")
    winlabel = Label(window, text="출발 : 괘법르네시떼")
    winlabel.pack()
    window.focus_set()
    
    def close1(text):
        input_entry.delete(0, END)
        input_entry.insert(0, text)
        window.destroy()
        
    def close2(text):
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)
        window.destroy()
    
    stbtn = Button(window, text="출발", command=lambda: close1("괘법르네시떼"))
    stbtn.pack(side=LEFT)
    endbtn = Button(window, text="도착", command=lambda: close2("괘법르네시떼"))
    endbtn.pack(side=RIGHT)

def result():
    start = input_entry.get()
    end = destination_entry.get()
    routing = {}
    for place in 부산지하철.keys():
        routing[place]={'shortestDist':0, 'route':[], 'visited':0}

    def visitPlace(visit):
        routing[visit]['visited'] = 1
        for toGo, betweenDist in 부산지하철[visit].items():
            toDist = routing[visit]['shortestDist'] + betweenDist
            if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:
                routing[toGo]['shortestDist'] = toDist
                routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
                routing[toGo]['route'].append(visit)
                

                
    visitPlace(start)

    while 1 :
        minDist = max(routing.values(), key=lambda x:x['shortestDist'])['shortestDist']
        toVisit = ''
        for name, search in routing.items():
            if 0 < search['shortestDist'] <= minDist and not search['visited']:
                minDist = search['shortestDist']
                toVisit = name
        
        if toVisit == '':
            break
        
        visitPlace(toVisit)
        
    routing[end]['route'].append(end)
    #a = '['+start+"->"+ end+"]\nRoute : "+routing[end]['route']+"\n소요 시간 : "+str(routing[end]['shortestDist'])
    a = f"[{start}->{end}]\nRoute: {routing[end]['route']}\n소요 시간: {routing[end]['shortestDist']}"
    resultlabel.config(text=a, font=("Arial", 12), background="lightgray", justify="center", wraplength=300) # wraplength = 자동으로 줄바꾸는 기능

def MoveTrain():
    global train_x
    train_label.place(x=train_x, y=train_y)
    train_x += train_speed  
    
#이미지가 1290을 넘어갔을 시 20의로 x축의 값을 초기화
    if train_x > 1180:
        train_x = 20
        
    frame2came1.after(100, MoveTrain)
    
frame1came1 = tk.Frame(win, height=1100 , width=400 ,background='lightgray')
frame1came1.grid(row=0, column=0,sticky="nwse")   
frame2came1 = tk.Frame(win, height=1100, width=1500, background='lightgray')
frame2came1.grid(row=0, column=1)

Lframe_top = tk.Frame(frame1came1, width=400, height=150, background='lightgray')
Lframe_top.pack(anchor='nw',expand=True,fill='both')

Lframe_bottom = tk.Frame(frame1came1, width=400, height=275, background='lightgray')
Lframe_bottom.pack(anchor='se',expand=True,fill='both')


traincanvas = tk.Canvas(frame2came1,width=1485,height=1080,relief='solid',bd=0,background='white')
traincanvas.place(x=5,y=10)   #노선도 그리는 칸

# 초기 지하철 열차 위치 및 이동 속도 설정
train_x = 0
train_y = 30
train_speed = 20

# 지하철 열차 이미지를 화면에 표시
img_train = Image.open("station/train.png")
img_sttrain = img_train.resize((300,30))
train_photo = ImageTk.PhotoImage(img_sttrain)
train_label = tk.Label(frame2came1, image=train_photo,bg='white')
train_label.place(x=train_x, y=train_y)
# 재귀함수로 열차를 움직임 

MoveTrain()

부산지하철 = { 
        '노포': {'범어사': 1},
        '범어사': {'노포': 1, '남산': 2},
        '남산': {'범어사': 2, '두실': 1},
        '두실': {'남산': 1, '구서': 2},
        '구서': {'두실': 2, '장전': 2},
        '장전': {'구서': 2, '부산대': 2},
        '부산대': {'장전': 2, '온천장': 2},
        '온천장': {'부산대': 2, '명륜': 2},
        '명륜': {'온천장': 2, '동래': 2},
        '동래': {'명륜': 2, '교대': 2, '미남': 3, '수안': 2},
        '교대': {'동래': 2, '연산': 2, '거제': 2, '동래(동해선)': 3},
        '연산': {'교대': 2, '시청': 1, '거제': 2, '물만골': 2},
        '시청': {'연산': 1, '양정': 2},
        '양정': {'시청': 2, '부전': 2},
        '부전': {'양정': 2, '서면': 2, '거제해맞이': 3},
        '서면': {'부전': 2, '범내골': 2, '부암': 12, '전포': 13},
        '범내골': {'서면': 2, '범일': 2},
        '범일': {'범내골': 2, '좌천(1호선)': 2},
        '좌천(1호선)': {'범일': 2, '부산진': 2},
        '부산진': {'좌천(1호선)': 2, '초량': 2},
        '초량': {'부산진': 2, '부산역': 1},
        '부산역': {'초량': 1, '중앙': 2},
        '중앙': {'부산역': 2, '남포': 2},
        '남포': {'중앙': 2, '자갈치': 1},
        '자갈치': {'남포': 1, '토성': 3},
        '토성': {'자갈치': 3, '동대신': 3},
        '동대신': {'토성': 3, '서대신': 3},
        '서대신': {'동대신': 3, '대티': 2},
        '대티': {'서대신': 2, '괴정': 1},
        '괴정': {'대티': 1, '사하': 2},
        '사하': {'괴정': 2, '당리': 1},
        '당리': {'사하': 1, '하단': 2},
        '하단': {'당리': 2, '신평': 3},
        '신평': {'하단': 3, '동매': 3},
        '동매': {'신평': 3, '장림': 2},
        '장림': {'동매': 2, '신장림': 2},
        '신장림': {'장림': 2, '낫개': 2},
        '낫개': {'신장림': 2, '다대포항': 2},
        '다대포항': {'낫개': 2, '다대포해수욕장': 3},
        '다대포해수욕장': {'다대포항': 3},
        '양산': {'남양산': 2},
        '남양산': {'양산': 2, '부산대중앙캠퍼스': 2},
        '부산대중앙캠퍼스': {'남양산':2, '증산': 2},
        '증산': {'부산대중앙캠퍼스': 2, '호포': 4},
        '호포': {'증산': 4, '금곡': 3},
        '금곡': {'호포': 3, '동원': 2},
        '동원': {'금곡': 2, '율리': 2},
        '율리': {'동원': 2, '화명': 2},
        '화명': {'율리': 2, '수정': 2},
        '수정': {'화명': 2, '덕천': 3},
        '덕천': {'수정': 3, '구명': 2, '구포': 3, '숙동': 2},
        '구명': {'덕천': 2, '구남': 2},
        '구남': {'구명': 2, '모라': 2},
        '모라': {'구남': 2, '모덕': 1},
        '모덕': {'모라': 1, '덕포': 1},
        '덕포': {'모덕': 1, '사상': 3},
        '사상': {'덕포': 3, '감전': 2, '괘법르네시떼': 1},
        '감전': {'사상': 2, '주례': 2},
        '주례': {'감전': 2, '냉정': 2},
        '냉정': {'주례': 2, '개금': 2},
        '개금': {'냉정': 2, '동의대': 1},
        '동의대': {'개금': 1, '가야': 2},
        '가야': {'동의대': 2, '부암': 2},
        '부암': {'가야': 2, '서면': 2},
        '서면': {'부전': 2, '범내골': 2, '부암': 2, '전포': 3},
        '전포': {'서면': 3, '국제금융센터·부산은행': 2},
        '국제금융센터·부산은행': {'전포': 2, '문헌': 2},
        '문헌': {'국제금융센터·부산은행': 2, '지게골': 1},
        '지게골': {'문헌': 1, '못골': 2},
        '못골': {'지게골': 2, '대연': 2},
        '대연': {'못골': 2, '경성대·부경대': 2},
        '경성대·부경대': {'대연': 2, '남천': 2},
        '남천': {'경성대·부경대': 2, '금련산': 2},
        '금련산': {'남천': 2, '광안': 2},
        '광안': {'금련산': 2, '수영': 2},
        '수영': {'광안': 2, '민락': 2, '망미': 2},
        '민락': {'수영': 2, '센텀시티': 2},
        '센텀시티': {'민락': 2, '벡스코(시립미술관)': 2},
        '벡스코(시립미술관)': {'센텀시티': 2, '동백': 2, '센텀': 12, '신해운대': 5},
        '동백': {'벡스코(시립미술관)': 2, '해운대': 2},
        '해운대': {'동백': 2, '중동': 2},
        '중동': {'해운대': 2, '장산': 2},
        '장산': {'중동': 2},
        '대저': {'체육공원': 1, '평강': 1, '등구': 13},
        '체육공원': {'대저': 1, '강서구청': 2},
        '강서구청': {'체육공원': 2, '구포': 3},
        '구포': {'강서구청': 3, '덕천': 3},
        '덕천': {'수정': 3, '구명': 2, '구포': 3, '숙동': 2},
        '숙동': {'덕천': 2, '남산정': 2},
        '남산정': {'숙동': 2, '만덕': 2},
        '만덕': {'남산정': 2, '미남': 4},
        '미남': {'만덕': 4, '사직': 2, '동래': 3},
        '사직': {'미남': 2, '종합운동장': 2},
        '종합운동장': {'사직': 2, '거제': 1},
        '거제': {'종합운동장': 1, '연산': 2, '교대': 2, '거제해맞이': 2},
        '연산': {'교대': 2, '시청': 1, '거제': 2, '물만골': 2},
        '물만골': {'연산': 2, '배산': 3},
        '배산': {'물만골': 3, '망미': 2},
        '망미': {'배산': 2, '수영': 2},
        '수영': {'광안': 2, '민락': 2, '망미': 2},
        '미남': {'만덕': 4, '사직': 2, '동래': 3},
        '동래': {'명륜': 2, '교대': 2, '미남': 3, '수안': 2},
        '수안': {'동래': 2, '낙민': 2},
        '낙민': {'수안': 2, '충렬사': 1},
        '충렬사': {'낙민': 1, '명장': 2},
        '명장': {'충렬사': 2, '서동': 2},
        '서동': {'명장': 2, '금사': 2},
        '금사': {'서동': 2, '반여농산물시장': 2},
        '반여농산물시장': {'금사': 2, '석대': 2},
        '석대': {'반여농산물시장': 2, '영산대': 2},
        '영산대': {'석대': 2, '윗반송': 3},
        '윗반송': {'영산대': 3, '고촌': 1},
        '고촌': {'윗반송': 1, '안평': 3},
        '안평': {'고촌': 3},
        '부전': {'양정': 2, '서면': 2, '거제해맞이': 3},
        '거제해맞이': {'부전': 3, '거제': 2},
        '거제': {'종합운동장': 1, '연산': 12, '교대': 2, '거제해맞이': 2},
        '교대': {'동래': 2, '연산': 12, '거제': 2, '동래(동해선)': 3},
        '동래(동해선)': {'교대': 3, '안락': 2},
        '안락': {'동래(동해선)': 2, '부산원동': 2},
        '부산원동': {'안락': 2, '재송': 1},
        '재송': {'부산원동': 1, '센텀': 2},
        '센텀': {'재송': 2, '벡스코(시립미술관)': 2},
        '벡스코(시립미술관)': {'센텀시티': 2, '동백': 2, '센텀': 2, '신해운대': 5},
        '신해운대': {'벡스코(시립미술관)': 5, '송정': 3},
        '송정': {'신해운대': 3, '오시리아': 3},
        '오시리아': {'송정': 3, '기장': 4},
        '기장': {'오시리아': 4, '일광': 3},
        '일광': {'기장': 3, '좌천(동해선)': 4},
        '좌천(동해선)': {'일광': 4, '월내': 3},
        '월내': {'좌천(동해선)': 3, '서생': 3},
        '서생': {'월내': 3, '남창': 7},
        '남창': {'서생': 7, '망양': 4},
        '망양': {'남창': 4, '덕하': 4},
        '덕하': {'망양': 4, '개운포': 2},
        '개운포': {'덕하': 2, '태화강': 4},
        '태화강': {'개운포': 4},
        '가야대': {'장신대': 2},
        '장신대': {'가야대': 2, '연지공원': 3},
        '연지공원': {'장신대': 3, '박물관': 2},
        '박물관': {'연지공원': 2, '수로왕릉': 2},
        '수로왕릉': {'박물관': 2, '봉황': 1},
        '봉황': {'수로왕릉': 1, '부원': 2},
        '부원': {'봉황': 2, '김해시청': 2},
        '김해시청': {'부원': 2, '인제대': 2},
        '인제대': {'김해시청': 2, '김해대학': 2},
        '김해대학': {'인제대': 2, '지내': 1},
        '지내': {'김해대학': 1, '불암': 2},
        '불암': {'지내': 2, '대사': 2},
        '대사': {'불암': 2, '평강': 2},
        '평강': {'대사': 2, '대저': 2},
        '대저': {'체육공원': 1, '평강': 1, '등구': 3},
        '등구': {'대저': 3, '덕두': 3},
        '덕두': {'등구': 3, '김해공항': 2},
        '김해공항': {'덕두': 2, '서부산유통지구': 2},
        '서부산유통지구': {'김해공항': 2, '괘법르네시떼': 2},
        '괘법르네시떼': {'서부산유통지구': 2, '사상': 1},
        '사상': {'덕포': 3, '감전': 2, '괘법르네시떼': 1},
}

start_list = ["노포","범어사","남산","두실","구서","장전","부산대","온천장","명륜","동래","교대","연산",
            "시청","양정","부전","서면","범내골","범일","좌천(1호선)","부산진","초량","부산역","중앙",
            "남포","자갈치","토성","동대신","서대신","대티","괴정","사하","당리","하단","신평","동매",
            "장림","신장림","낫개","다대포항","다대포해수욕장","양산","남양산","부산대중앙캠퍼스","증산",
            "호포","금곡","동원","율리","화명","수정","덕천","구명","구남","모라","모덕","덕포","사상",
            "감전","주례","냉정","개금","동의대","가야","부암","전포","국제금융센터·부산은행","지게골",
            "못골","대연","경성대·부경대","남천","금련산","광안","수영","민락","센텀시티","벡스코(시립미술관)",
            "동백","대저","체육공원","강서구청","구포","숙동","남산정","만덕","미남","사직","종합운동장",
            "거제","물만골","배산","망미","수안","낙민","충렬사","명장","서동","금사","반여농산물시장",
            "석대","영산대","윗반송","고촌","안평","거제해맞이","동래(동해선)","안락","부산원동","재송",
            "센텀","신해운대","송정","오시리아","기장","일광","좌천(동해선)","월내","서생","남창","망양",
            "덕하","개운포","태화강","가야대","장신대","연지공원","박물관","수로왕릉","봉황","부원","김해시청",
            "인제대","김해대학","지내","불암","대사","평강","대저","등구","덕두","김해공항","서부산유통지구",
            "괘법르네시떼","사상"]

end_list = ["노포","범어사","남산","두실","구서","장전","부산대","온천장","명륜","동래","교대","연산",
            "시청","양정","부전","서면","범내골","범일","좌천(1호선)","부산진","초량","부산역","중앙",
            "남포","자갈치","토성","동대신","서대신","대티","괴정","사하","당리","하단","신평","동매",
            "장림","신장림","낫개","다대포항","다대포해수욕장","양산","남양산","부산대중앙캠퍼스","증산",
            "호포","금곡","동원","율리","화명","수정","덕천","구명","구남","모라","모덕","덕포","사상",
            "감전","주례","냉정","개금","동의대","가야","부암","전포","국제금융센터·부산은행","지게골",
            "못골","대연","경성대·부경대","남천","금련산","광안","수영","민락","센텀시티","벡스코(시립미술관)",
            "동백","대저","체육공원","강서구청","구포","숙동","남산정","만덕","미남","사직","종합운동장",
            "거제","물만골","배산","망미","수안","낙민","충렬사","명장","서동","금사","반여농산물시장",
            "석대","영산대","윗반송","고촌","안평","거제해맞이","동래(동해선)","안락","부산원동","재송",
            "센텀","신해운대","송정","오시리아","기장","일광","좌천(동해선)","월내","서생","남창","망양",
            "덕하","개운포","태화강","가야대","장신대","연지공원","박물관","수로왕릉","봉황","부원","김해시청",
            "인제대","김해대학","지내","불암","대사","평강","대저","등구","덕두","김해공항","서부산유통지구",
            "괘법르네시떼","사상"]

keyword = {
    "ㄱ" : ['가야', '가야대', '감전', '강서구청', '개금', '개운포', '거제', '거제해맞이', '경성대·부경대', '고촌',
           '광안', '괘법르네시떼', '괴정', '교대', '구남', '구명', '구서', '구포', '국제금융센터·부산은행', 
           '금곡', '금련산', '금사', '기장', '김해공항', '김해대학', '김해시청'],
    
    "ㄴ" : ['낙민', '남산', '남산정', '남양산', '남창', '남천', '남포', '낫개', '냉정', '노포'],
    "ㄷ" : ['다대포항', '다대포해수욕장', '당리', '대사', '대연', '대저', '대저',
           '대티', '덕두', '덕천', '덕포', '덕하', '동대신', '동래', '동래(동해선)', '동매', '동백', '동원', '동의대', '두실', '등구'],
    "ㅁ" : ['만덕', '망미', '망양', '명륜', '명장', '모덕', '모라', '못골', '물만골', '미남','민락'],
    "ㅂ" : ['박물관', '반여농산물시장', '배산', '벡스코(시립미술관)', '범내골', '범어사', '범일', '봉황', '부산대', '부산대중앙캠퍼스', '부산역', '부산원동', '부산진', '부암', '부원', '부전'],
    "ㅅ" : ['사상', '사상','사직', '사하', '서대신', '서동', '서면', '서부산유통지구', '서생', '석대', '센텀', '센텀시티', '송정', '수로왕릉', '수안', '수영', '수정', '숙동', '시청', '신장림', '신평', '신해운대'],
    "ㅇ" : ['안락', '안평', '양산','양정', '연산', '연지공원', '영산대', '오시리아', '온천장', '월내', '윗반송', '율리', '인제대', '일광'],
    "ㅈ" : ['자갈치', '장림', '장신대', '장전', '재송', '전포', '종합운동장', '좌천(1호선)', '좌천(동해선)', '주례','중앙', '증산', '지게골', '지내'],
    "ㅌ" : ['태화강', '토성'],
    "ㅎ" : ['하단', '호포', '화명'],
    '가': ['가야', '가야대'],
    '갈': ['자갈치'],
    '감': ['감전'],
    '강': ['강서구청', '태화강', '평강'],
    '개': ['개금', '개운포', '낫개'],
    '거': ['거제', '거제해맞이'],
    '게': ['지게골'],
    '경': ['경성대·부경대'],
    '곡': ['금곡'],
    '골': ['못골', '물만골', '범내골', '지게골'],
    '공': ['공항', '연지공원', '체육공원'],
    '관': ['박물관', '벡스코(시립미술관)'],
    '광': ['광안', '일광'],
    '괘': ['괘법르네시떼'],
    '괴': ['괴정'],
    '교': ['교대'],
    '구': ['강서구청', '구남', '구명', '구서', '구포', '등구', '서부산유통지구'],
    '국': ['국제금융센터·부산은행'],
    '금': ['개금', '국제금융센터·부산은행', '금곡', '금련산', '금사'],
    '김': ['김해대학', '김해시청'],
    '낙': ['낙민'],
    '남': ['구남', '남산', '남산정', '남양산', '남창', '남천', '남포', '미남'],
    '낫': ['낫개'],
    '내': ['범내골', '월내', '지내'],
    '냉': ['냉정'],
    '네': ['괘법르네시떼'],
    '노': ['노포'],
    '농': ['반여농산물시장'],
    '다': ['다대포항', '다대포해수욕장'],
    '단': ['하단'],
    '당': ['당리'],
    '대': ['가야대', '경성대·부경대', '교대', '김해대학', '다대포항', '다대포항해수욕장', '대사', '대연', '대저', '대티',
          '동대신', '동의대', '부산대', '부산대양산캠퍼스', '서대신', '석대', '신해운대', '영산대', '인제대', '장신대', '해운대'],
    '덕': ['덕두', '덕천', '덕포', '덕하', '만덕', '모덕'],
    '동': ['동대신', '동래', '동래(동해선)', '동매', '동백', '동원', '동의대', '부산원동', '서동', '종합운동장', '좌천(동해선)', '중동'],
    '두': ['덕두', '두실'],
    '등': ['등구', '숙등'],
    '떼': ['괘법르네시떼'],
    '라': ['모라'],
    '락': ['민락'],
    '량': ['초량'],
    '래': ['동래', '동래(동해선)'],
    '례': ['주례'],
    '련': ['금련산'],
    '렬': ['충렬사'],
    '로': ['수로왕릉'],
    '륜': ['명륜'],
    '르': ['괘법르네시떼'],
    '릉': ['수로왕릉'],
    '리': ['당리', '오시리아', '율리'],
    '림': ['신장림', '장림'],
    '립': ['벡스코(시립미술관)'],
    '만': ['만덕', '물만골'],
    '망': ['망미', '망양'],
    '맞': ['거제해맞이'],
    '매': ['동매'],
    '면': ['서면'],
    '명': ['구명', '명륜', '명장', '화명'],
    '모': ['모덕', '모라'],
    '못': ['못골'],
    '문': ['문현'],
    '물': ['물만골', '박물관', '반여농산물시장'],
    '미': ['망미', '미남', '벡스코(시립미술관)'],
    '민': ['낙민', '민락'],
    '박': ['박물관'],
    '반': ['반여농산물시장', '윗반송'],
    '배': ['배산'],
    '백': ['동백'],
    '범': ['범내골', '범어사', '범일'],
    '법': ['괘법르네시떼'],
    '벡': ['벡스코(시립미술관)'],
    '봉': ['봉황'],
    '부': ['경성대·부경대', '국제금융센터·부산은행', '부산역', '부산대', '부산대양산캠퍼스', '부산원동', '부산진', '부암', '부원'
          '부전', '서부산유통진구'],
    '불': ['불암'],
    '사': ['금사', '대사', '범어사', '사상', '사직', '사하', '충렬사'],
    '산': ['국제금융센터·부산은행', '금련산', '남산', '남산정', '남양산', '반여농산물시장', '배산', '부산역', '부산대', '부산대양산캠퍼스',
          '부산원동', '부산진', '서부산유통지구', '양산', '연산', '영산대', '장산', '증산'],
    '상': ['사상'],
    '서': ['강서구청', '구서', '서대신', '서동', '서면', '서부산유통지구', '서생'],
    '석': ['석대'],
    '성': ['경성대·부경대', '토성'],
    '생': ['서생'],
    '센': ['국제금융센터·부산은행', '센텀', '센텀시티'],
    '송': ['윗반송','송정','재송'],
    '수': ['다대포해수욕장', '수로왕릉', '수안', '수영', '수정'],
    '숙': ['숙등'],
    '술': ['벡스코(시립미술관)'],
    '스': ['벡스코(시립미술관)', '부산대양산캠퍼스'],
    '시': ['괘법르네시떼', '김해시청', '반여농산물시장', '벡스코(시립미술관)', '센텀시티', '시청', '오시리아'],
    '신': ['동대신', '서대신', '신장림', '신평', '신해운대', '장신대'],
    '실': ['두실'],
    '아': ['오시리아'],
    '안': ['광안', '수안', '안락', '안평'],
    '암': ['부암', '불암'],
    '앙': ['중앙'],
    '야': ['가야', '가야대'],
    '양': ['남양산', '망양', '부산대양산캠퍼스', '양산', '양정'],
    '어': ['범어사'],
    '여': ['반여농산물시장'],
    '역': ['부산역'],
    '연': ['대연', '연산', '연지공원'],
    '영': ['수영', '영산대'],
    '오': ['오시리아'],
    '온': ['온천장'],
    '욕': ['다대포해수욕장'],
    '운': ['개운포', '신해운대', '종합운동장', '해운대'],
    '왕': ['수로왕릉'],
    '원': ['동원', '부산원동', '부원', '연지공원', '체육공원'],
    '유': ['서부산유통지구'],
    '육': ['체육공원'],
    '율': ['율리'],
    '융': ['국제금융센터·부산은행'],
    '은': ['국제금융센터·부산은행'],
    '의': ['동의대'],
    '이': ['거제해맞이'],
    '일': ['범일', '일광'],
    '인': ['인제대'],
    '윗': ['윗반송'],
    '자': ['자갈치'],
    '장': ['기장', '다대포해수욕장', '명장', '반여농산물시장', '신장림', '온천장', '장림', '장산', '장신대', '장전', '종합운동장'],
    '저': ['대저'],
    '전': ['감전', '대저', '부전', '장전', '전포'],
    '정': ['괴정', '남산정', '냉정', '송정', '수정', '양정'],
    '재': ['재송'],
    '제': ['거제', '거제해맞이', '국제금융센터·부산은행', '인제대'],
    '종': ['종합운동장'],
    '좌': ['좌천(1호선)', '좌천(동해선)'],
    '주': ['주례'],
    '중': ['중동', '중앙'],
    '증': ['증산'],
    '지': ['서부산유통지구', '연지공원', '지게골', '지내'],
    '직': ['사직'],
    '진': ['부산진'],
    '창': ['남창'],
    '천': ['남천', '덕천', '온천장', '좌천(1호선)', '좌천(동해선)'],
    '청': ['강서구청', '김해시청', '시청'],
    '체': ['체육공원'],
    '초': ['초량'],
    '촌': ['고촌'],
    '충': ['충렬사'],
    '치': ['자갈치'],
    '캠': ['부산대양산캠퍼스'],
    '코': ['벡스코(시립미술관)'],
    '태': ['태화강'],
    '터': ['국제금융센터·부산은행'],
    '텀': ['센텀', '센텀시티'],
    '토': ['토성'],
    '통': ['서부산유통지구'],
    '티': ['대티', '센텀시티'],
    '퍼': ['부산대양산캠퍼스'],
    '평': ['신평', '안평', '평강'],
    '포': ['개운포', '구포', '남포', '노포', '다대포항', '다대포해수욕장', '덕포', '전포', '호포'],
    '하': ['덕하', '사하', '하단'],
    '학': ['김해대학'],
    '합': ['종합운동장'],
    '항': ['공항', '다대포항'],
    '해': ['거제해맞이', '김해대학', '김해시청', '동래(동해선)', '신해운대', '해운대'],
    '행': ['국제금융센터·부산은행'],
    '현': ['문현'],
    '호': ['호포'],
    '화': ['태화강', '화명'],
    '황': ['봉황'],
    
    '가야': ['가야', '가야대'],
    '강서': ['강서구청'],
    '갈치': ['자갈치'],
    '감전': ['감전'],
    '개운': ['개운포'],
    '거제': ['거제', '거제해맞이'],
    '개금': ['개금'],
    '게골': ['지게골'],
    '경대': ['경성대·부경대'],
    '경성': ['경성대·부경대'],
    '고촌': ['고촌'],
    '공원': ['연지공원', '체육공원'],
    '공항': ['공항'],
    '관)': ['벡스코(시립미술관)'],
    '광안': ['광안'],
    '괘법': ['괘법르네시떼'],
    '괴정': ['괴정'],
    '구남': ['구남'],
    '구명': ['구명'],
    '구서': ['구서'],
    '구청': ['강서구청'],
    '구포': ['구포'],
    '국제': ['국제금융센터·부산은행'],
    '교대': ['교대'],
    '금곡': ['금곡'],
    '금련': ['금련산'],
    '금사': ['금사'],
    '금융': ['국제금융센터·부산은행'],
    '기장': ['기장'],
    '김해': ['김해대학', '김해시청'],
    '낙민': ['낙민'],
    '남산': ['남산', '남산정'],
    '남양': ['남양산'],
    '남천': ['남천'],
    '남창': ['남창'],
    '남포': ['남포'],
    '낫개': ['낫개'],
    '내골': ['범내골'],
    '냉정': ['냉정'],
    '네시': ['괘법르네시떼'],
    '노포': ['노포'],
    '농산': ['반여농산물시장'],
    '다대': ['다대포항', '다대포해수욕장'],
    '당리': ['당리'],
    '대부': ['경성대·부경대'],
    '대사': ['대사'],
    '대신': ['동대신', '서대신'],
    '대양': ['부산대양산캠퍼스'],
    '대연': ['대연'],
    '대저': ['대저'],
    '대티': ['대티'],
    '대포': ['다대포항', '다대포해수욕장'],
    '대학': ['김해대학'],
    '덕두': ['덕두'],
    '덕천': ['덕천'],
    '덕포': ['덕포'],
    '덕하': ['덕하'],
    '동대': ['동대신'],
    '동래': ['동래', '동래(동해선)'],
    '동매': ['동매'],
    '동백': ['동백'],
    '동원': ['동원'],
    '동의': ['동의대'],
    '동장': ['종합운동장'],
    '두실': ['두실'],
    '등구': ['등구'],
    '련산': ['금련산'],
    '렬사': ['충렬사'],
    '로왕': ['로왕'],
    '르네': ['괘법르네시떼'],
    '리아': ['오시리아'],
    '립미': ['벡스코(시립미술관)'],
    '만골': ['물만골'],
    '만덕': ['만덕'],
    '망미': ['망미'],
    '망양': ['망양'],
    '맞이': ['거제해맞이'],
    '명륜': ['명륜'],
    '명장': ['명장'],
    '모덕': ['모덕'],
    '모라': ['모라'],
    '문헌': ['문헌'],
    '물관': ['박물관'],
    '물만': ['물만골'],
    '물시': ['반여농산물시장'],
    '못골': ['못골'],
    '미남': ['미남'],
    '미술': ['벡스코(시립미술관)'],
    '박물': ['박물관'],
    '반송': ['윗반송'],
    '반여': ['반여농산물시장'],
    '배산': ['배산'],
    '범내': ['범내골'],
    '범어': ['범어사'],
    '범일': ['범일'],
    '법르': ['괘법르네시떼'],
    '벡스': ['벡스코(시립미술관)'],
    '봉황': ['봉황'],
    '부경': ['경성대·부경대'],
    '부산': ['국제금융센터·부산은행', '부산역', '부산대', '부산대양산캠퍼스', '부산원동', '부산진', '서부산유통지구'],
    '부암': ['부암'],
    '부원': ['부원'],
    '부전': ['부전'],
    '불암': ['불암'],
    '사상': ['사상'],
    '사직': ['사직'],
    '사하': ['사하'],
    '산대': ['부산대', '부산대양산캠퍼스', '영산대'],
    '산물': ['반여농산물시장'],
    '산역': ['부산역'],
    '산원': ['부산원동'],
    '산유': ['서부산유통지구'],
    '산은': ['국제금융센터·부산은행'],
    '산정': ['남산정'],
    '산진': ['부산진'],
    '산캠': ['부산대양산캠퍼스'],
    '서구': ['강서구청'],
    '서대': ['서대신'],
    '서동': ['서동'],
    '서면': ['서면'],
    '서부': ['서부산유통지구'],
    '서생': ['서생'],
    '석대': ['석대'],
    '성대': ['경성대·부경대'],
    '센터': ['국제금융센터·부산은행'],
    '센텀': ['센텀', '센텀시티'],
    '송정': ['송정'],
    '수로': ['수로왕릉'],
    '수안': ['수안'],
    '수영': ['수영'],
    '수욕': ['다대포해수욕장'],
    '수정': ['수정'],
    '숙등': ['숙등'],
    '술관': ['벡스코(시립미술관)'],
    '스코': ['벡스코(시립미술관)'],
    '시떼': ['괘법르네시떼'],
    '시리': ['오시리아'],
    '시립': ['벡스코(시립미술관)'],
    '시장': ['반여농산물시장'],
    '시청': ['김해시청', '시청'],
    '시티': ['센텀시티'],
    '신대': ['신대'],
    '신평': ['신평'],
    '신해': ['신해운대'],
    '안락': ['안락'],
    '안평': ['안평'],
    '야대': ['가야대'],
    '양산': ['남양산', '부산대양산캠퍼스', '양산'],
    '양정': ['양정'],
    '어사': ['범어사'],
    '여농': ['반여농산물시장'],
    '연산': ['연산'],
    '연지': ['연지공원'],
    '영산': ['영산대'],
    '오시': ['오시리아'],
    '온천': ['온천장'],
    '왕릉': ['수로왕릉'],
    '욕장': ['다대포해수욕장'],
    '운대': ['신해운대', '해운대'],
    '운동': ['종합운동장'],
    '운포': ['개운포'],
    '원동': ['부산원동'],
    '월내': ['월내'],
    '윗반': ['윗반송'],
    '유통': ['서부산유통지구'],
    '육공': ['체육공원'],
    '율리': ['율리'],
    '융센': ['국제금융센터·부산은행'],
    '은행': ['국제금융센터·부산은행'],
    '의대': ['의대'],
    '인제': ['인제대'],
    '일광': ['일광'],
    '자갈': ['자갈치'],
    '장림': ['신장림', '장림'],
    '장산': ['장산'],
    '장신': ['장신대'],
    '장전': ['장전'],
    '재송': ['재송'],
    '전포': ['전포'],
    '제금': ['국제금융센터·부산은행'],
    '제대': ['인제대'],
    '제해': ['거제해맞이'],
    '종합': ['종합운동장'],
    '좌천': ['좌천(1호선)', '좌천(동해선)'],
    '주례': ['주례'],
    '중동': ['중동'],
    '중앙': ['중앙'],
    '증산': ['증산'],
    '지게': ['지게골'],
    '지공': ['연지공원'],
    '지구': ['서부산유통지구'],
    '지내': ['지내'],
    '천장': ['온천장'],
    '체육': ['체육공원'],
    '초량': ['초량'],
    '충렬': ['충렬사'],
    '캠퍼': ['부산대양산캠퍼스'],
    '코시': ['벡스코(시립미술관)'],
    '코(': ['벡스코(시립미술관)'],
    '태화강': ['태화강'],
    '터부': ['국제금융센터·부산은행'],
    '텀시': ['센텀시티'],
    '토성': ['토성'],
    '통지': ['서부산유통지구'],
    '퍼스': ['부산대양산캠퍼스'],
    '평강': ['평강'],
    '포항': ['다대포항'],
    '포해': ['다대포해수욕장'],
    '하단': ['하단'],
    '합운': ['종합운동장'],
    '해대': ['김해대학'],
    '해맞': ['거제해맞이'],
    '해수': ['다대포해수욕장'],
    '해시': ['김해시청'],
    '해운': ['신해운대', '해운대'],
    '호포': ['호포'],
    '화강': ['태화강'],
    '화명': ['화명'],
    '(시': ['벡스코(시립미술관)'],
    
    '가야대': ['가야대'],
    '강서구': ['강서구청'],
    '개운포': ['개운포'],
    '거제해': ['거제해맞이'],
    '경성대': ['경성대·부경대'],
    '괘법르': ['괘법르네시떼'],
    '국제금': ['국제금융센터·부산은행'],
    '금련산': ['금련산'],
    '금융센': ['국제금융센터·부산은행'],
    '김해대': ['김해대학'],
    '김해시': ['김해시청'],
    '남양산': ['남양산'],
    '네시떼': ['괘법르네시떼'],
    '농산물': ['반여농산물시장'],
    '다대포': ['다대포항', '다대포해수욕장'],
    '대부경': ['경성대·부경대'],
    '대양산': ['부산대양산캠퍼스'],
    '대포항': ['다대포항'],
    '대포해': ['다대포해수욕장'],
    '동대신': ['동대신'],
    '동의대': ['동의대'],
    '로왕릉': ['수로왕릉'],
    '르네시': ['괘법르네시떼'],
    '립미술': ['벡스코(시립미술관)'],
    '물만골': ['물만골'],
    '물시장': ['반여농산물시장'],
    '미술관': ['벡스코(시립미술관)'],
    '박물관': ['박물관'],
    '반여농': ['반여농산물시장'],
    '범내골': ['범내골'],
    '범어사': ['범어사'],
    '법르네': ['괘법르네시떼'],
    '벡스코': ['벡스코(시립미술관)'],
    '부경대': ['경성대·부경대'],
    '부산대': ['부산대', '부산대양산캠퍼스'],
    '부산역': ['부산역'],
    '부산원': ['부산원동'],
    '부산유': ['서부산유통지구'],
    '부산은': ['국제금융센터·부산은행'],
    '부산진': ['부산진'],
    '산대양': ['부산대양산캠퍼스'],
    '산물시': ['반여농산물시장'],
    '산원동': ['부산원동'],
    '산유통': ['서부산유통지구'],
    '산은행': ['국제금융센터·부산은행'],
    '산캠퍼': ['부산대양산캠퍼스'],
    '서구청': ['강서구청'],
    '서대신': ['서대신'],
    '서부산': ['서부산유통지구'],
    '성대부': ['경성대·부경대'],
    '센터부': ['국제금융센터·부산은행'],
    '센텀시': ['센텀시티'],
    '수로왕': ['수로왕릉'],
    '수욕장': ['다대포해수욕장'],
    '술관)': ['벡스코(시립미술관)'],
    '스코시': ['벡스코(시립미술관)'],
    '스코(': ['벡스코(시립미술관)'],
    '시리아': ['오시리아'],
    '시립미': ['벡스코(시립미술관)'],
    '신장림': ['신장림'],
    '신해운': ['신해운대'],
    '양산캠': ['부산대양산캠퍼스'],
    '여농산': ['반여농산물시장'],
    '연지공': ['연지공원'],
    '영산대': ['영산대'],
    '오시리': ['오시리아'],
    '온천장': ['온천장'],
    '운동장': ['종합운동장'],
    '윗반송': ['윗반송'],
    '유통지': ['서부산유통지구'],
    '육공원': ['체육공원'],
    '융센터': ['국제금융센터·부산은행'],
    '인제대': ['인제대'],
    '자갈치': ['자갈치'],
    '장신대': ['장신대'],
    '제금융': ['국제금융센터·부산은행'],
    '제해맞': ['거제해맞이'],
    '종합운': ['종합운동장'],
    '지게골': ['지게골'],
    '지공원': ['연지공원'],
    '체육공': ['체육공원'],
    '충렬사': ['충렬사'],
    '캠퍼스': ['부산대양산캠퍼스'],
    '코시립': ['벡스코(시립미술관)'],
    '코(시': ['벡스코(시립미술관)'],
    '태화강': ['태화강'],
    '터부산': ['국제금융센터·부산은행'],
    '텀시티': ['센텀시티'],
    '통지구': ['서부산유통지구'],
    '포해수': ['다대포해수욕장'],
    '합운동': ['종합운동장'],
    '해대학': ['김해대학'],
    '해맞이': ['거제해맞이'],
    '해수욕': ['다대포해수욕장'],
    '해시청': ['김해시청'],
    '해운대': ['신해운대', '해운대'],
    '(시립': ['벡스코(시립미술관)'],
    
    '강서구청': ['강서구청'],
    '거제해맞': ['거제해맞이'],
    '경성대부': ['경성대·부경대'],
    '괘법르네': ['괘법르네시떼'],
    '국제금융': ['국제금융센터·부산은행'],
    '금융센터': ['국제금융센터·부산은행'],
    '김해대학': ['김해대학'],
    '김해시청': ['김해시청'],
    '농산물시': ['반여농산물시장'],
    '다대포해': ['다대포해수욕장'],
    '대부경대': ['경성대·부경대'],
    '대양산캠': ['부산대양산캠퍼스'],
    '대포해수': ['다대포해수욕장'],
    '르네시떼': ['괘법르네시떼'],
    '립미술관': ['벡스코(시립미술관)'],
    '미술관)': ['벡스코(시립미술관)'],
    '반여농산': ['반여농산물시장'],
    '법르네시': ['괘법르네시떼'],
    '벡스코시': ['벡스코(시립미술관)'],
    '벡스코(': ['벡스코(시립미술관)'],
    '부산대양': ['부산대양산캠퍼스'],
    '부산원동': ['부산원동'],
    '부산유통': ['서부산유통지구'],
    '부산은행': ['국제금융센터·부산은행'],
    '산대양산': ['부산대양산캠퍼스'],
    '산물시장': ['반여농산물시장'],
    '산유통지': ['서부산유통지구'],
    '산캠퍼스': ['부산대양산캠퍼스'],
    '서부산유': ['서부산유통지구'],
    '성대부경': ['경성대·부경대'],
    '센터부산': ['국제금융센터·부산은행'],
    '수로왕릉': ['수로왕릉'],
    '스코시립': ['벡스코(시립미술관)'],
    '스코(시': ['벡스코(시립미술관)'],
    '시립미술': ['벡스코(시립미술관)'],
    '신해운대': ['신해운대'],
    '양산캠퍼': ['부산대양산캠퍼스'],
    '여농산': ['반여농산물시장'],
    '연지공원': ['연지공원'],
    '오시리아': ['오시리아'],
    '유통지구': ['서부산유통지구'],
    '융센터부': ['국제금융센터·부산은행'],
    '제금융센': ['국제금융센터·부산은행'],
    '제해맞이': ['거제해맞이'],
    '종합운동': ['종합운동장'],
    '체육공원': ['체육공원'],
    '코시립미': ['벡스코(시립미술관)'],
    '코(시립': ['벡스코(시립미술관)'],
    '터부산은': ['국제금융센터·부산은행'],
    '포해수욕': ['다대포해수욕장'],
    '합운동장': ['종합운동장'],
    '해수욕장': ['다대포해수욕장'],
    '(시립미': ['벡스코(시립미술관)'],
    
    '거제해맞이': ['거제해맞이'],
    '경성대부경': ['경성대·부경대'],
    '괘법르네시': ['괘법르네시떼'],
    '국제금융센': ['국제금융센터·부산은행'],
    '금융센터부': ['국제금융센터·부산은행'],
    '농산물시장': ['반여농산물시장'],
    '다대포해수': ['다대포해수욕장'],
    '대양산캠퍼': ['부산대양산캠퍼스'],
    '대포해수욕': ['다대포해수욕장'],
    '립미술관)': ['벡스코(시립미술관)'],
    '반여농산물': ['반여농산물시장'],
    '법르네시떼': ['괘법르네시떼'],
    '벡스코시립': ['벡스코(시립미술관)'],
    '벡스코(시': ['벡스코(시립미술관)'],
    '부산대양산': ['부산대양산캠퍼스'],
    '부산유통지': ['서부산유통지구'],
    '산대양산캠': ['부산대양산캠퍼스'],
    '산유통지구': ['서부산유통지구'],
    '성대부경대': ['경성대·부경대'],
    '서부산유통': ['서부산유통지구'],
    '센터부산은': ['국제금융센터·부산은행'],
    '스코시립미': ['벡스코(시립미술관)'],
    '스코(시립': ['벡스코(시립미술관)'],
    '시립미술관': ['벡스코(시립미술관)'],
    '양산캠퍼스': ['부산대양산캠퍼스'],
    '여농산물시': ['반여농산물시장'],
    '융센터부산': ['국제금융센터·부산은행'],
    '제금융센터': ['국제금융센터·부산은행'],
    '종합운동장': ['종합운동장'],
    '코시립미술': ['벡스코(시립미술관)'],
    '코(시립미': ['벡스코(시립미술관)'],
    '터브산은행': ['국제금융센터·부산은행'],
    '포해수욕장': ['다대포해수욕장'],
    '(시립미술':['벡스코(시립미술관)'],
    
    '경성대부경대': ['경성대·부경대'],
    '괘법르네시떼': ['괘법르네시떼'],
    '국제금융센터': ['국제금융센터·부산은행'],
    '금융센터부산': ['국제금융센터·부산은행'],
    '다대포해수욕': ['다대포해수욕장'],
    '대양산캠퍼스': ['부산대양산캠퍼스'],
    '대포해수욕장': ['다대포해수욕장'],
    '반여농산물시': ['반여농산물시장'],
    '벡스코시립미': ['벡스코(시립미술관)'],
    '벡스코(시립': ['벡스코(시립미술관)'],
    '부산대양산캠': ['부산대양산캠퍼스'],
    '부산유통지구': ['서부산유통지구'],
    '산대양산캠퍼': ['부산대양산캠퍼스'],
    '서부산유통지': ['서부산유통지구'],
    '센터부산은행': ['국제금융센터·부산은행'],
    '스코시립미술': ['벡스코(시립미술관)'],
    '스코(시립미': ['벡스코(시립미술관)'],
    '시립미술관)': ['벡스코(시립미술관)'],
    '여농산물시장': ['반여농산물시장'],
    '융센터부산은': ['국제금융센터·부산은행'],
    '제금융센터부': ['국제금융센터·부산은행'],
    '코시립미술관': ['벡스코(시립미술관)'],
    '코(시립미술': ['벡스코(시립미술관)'],
    '(시립미술관': ['벡스코(시립미술관)'],
    
    '국제금융센터부': ['국제금융센터·부산은행'],
    '금융센터부산은': ['국제금융센터·부산은행'],
    '다대포해수욕장': ['다대포해수욕장'],
    '반여농산물시장': ['반여농산물시장'],
    '벡스코시립미술': ['벡스코(시립미술관)'],
    '벡스코(시립미': ['벡스코(시립미술관)'],
    '부산대양산캠퍼': ['부산대양산캠퍼스'],
    '산대양산캠퍼스': ['부산대양산캠퍼스'],
    '서부산유통지구': ['서부산유통지구'],
    '스코시립미술관': ['벡스코(시립미술관)'],
    '스코(시립미술': ['벡스코(시립미술관)'],
    '융센터부산은행': ['국제금융센터·부산은행'],
    '제금융센터부산': ['국제금융센터·부산은행'],
    '코(시립미술관': ['벡스코(시립미술관)'],
    '(시립미술관)': ['벡스코(시립미술관)'],
    
    '국제금융센터부산': ['국제금융센터·부산은행'],
    '금융센터부산은행': ['국제금융센터·부산은행'],
    '벡스코시립미술관': ['벡스코(시립미술관)'],
    '벡스코(시립미술': ['벡스코(시립미술관)'],
    '부산대양산캠퍼스': ['부산대양산캠퍼스'],
    '스코(시립미술관': ['벡스코(시립미술관)'],
    '제금융센터부산은': ['국제금융센터·부산은행'],
    '코(시립미술관)': ['벡스코(시립미술관)'],
    
    '국제금융센터부산은': ['국제금융센터·부산은행'],
    '벡스코(시립미술관': ['벡스코(시립미술관)'],
    '스코(시립미술관)': ['벡스코(시립미술관)'],
    '제금융센터부산은행': ['국제금융센터·부산은행'],
    
    '국제금융센터부산은행': ['국제금융센터·부산은행'],
    '벡스코(시립미술관)': ['벡스코(시립미술관)'],
}

# 지하철 역과 노선 정보
subway_stations_1 = {
    '노포': (1415, 98),
    '범어사': (1343, 98),
    '남산': (1272, 98),
    '두실': (1200, 98),
    '선릉': (1129, 98),
    '장전': (1057,98),
    '부산대': (986,98),
    '온천장': (915,98),
    '명륜': (843,98),
    '동래': (807,251),
    '교대': (807,385),
    '연산': (807,510),
    '시청': (807,582),
    '양정': (807,666),
    '부전': (807,750),
    '서면': (807,837),
    '범내골': (807,909),
    '범일': (807,980),
    '좌천(1호선)': (778,1020),
    '부산진': (744,1020),
    '초량': (711,1020),
    '부산역': (677,1020),
    '중앙': (643,1020),
    '남포': (610,1020),
    '자갈치': (577,1020),
    '토성': (543,1020),
    '동대신': (510,1020),
    '서대신': (476,1020),
    '대티': (443,1020),
    '과정': (410,1020),
    '사하': (376,1020),
    '당리': (343,1020),
    '하단': (309,1020),
    '신평': (275,1020),
    '동매': (241,1020),
    '장림': (208,1020),
    '신장림': (175,1020),
    '낫개': (142,1020),
    '다대포항': (108,1020),
    '다대포해수욕장': (74,1020),
}

subway_lines_1 = [
    ['노포', '범어사', '남산', '두실', '선릉', '장전', '부산대', '온천장', '명륜', '동래', '교대', '연산', '시청', '양정', '부전', '서면', '범내골', '범일', '좌천(1호선)', '부산진', '초량', '부산역', '중앙',
     '남포', '자갈치', '토성', '동대신', '서대신', '대티', '과정', '사하', '당리', '하단', '신평', '동매', '장림', '신장림', '낫개', '다대포항', '다대포해수욕장'],

] 

subway_stations_2 = {
    '양산': (728,98),
    '남양산': (682,98),
    '부산대중앙캠퍼스': (635,98),
    '중산': (586,98),
    '호포': (539,98),
    '금곡': (492,98),
    '동원': (445,104),
    '율리': (429,148),
    '화명': (429,288),
    '수정': (429,391),
    '덕천': (429,510),
    '구명': (429,561),
    '구남': (429,619),
    '모라': (429,675),
    '모덕': (429,732),
    '덕포': (429,787),
    '사상': (453,837),
    '감전': (504,837),
    '주례': (547,837),
    '냉정': (589,837),
    '개금': (632,837),
    '동의대': (675,837),
    '가야': (719,837),
    '부암': (761,837),
    '서면': (807,837),
    '전포': (853,837),
    '국제금융센터 - 부산은행': (883,837),
    '문현': (915,837),
    '지게골': (947,837),
    '못골': (976,837),
    '대연': (1006,837),
    '경성대*부경대': (1039,805),
    '남천': (1039,735),
    '금련산': (1039,665),
    '광안': (1039,594),
    '수영': (1055,510),
    '민락': (1113,510),
    '센텀시티': (1172,510),
    '벡스코(시립미술관)': (1226,510),
    '동백': (1277,510),
    '해운대': (1322,510),
    '중동': (1368,510),
    '장산': (1415,510),   
}

subway_lines_2 = ['양산', '남양산','부산대중앙캠퍼스','중산','호포','금곡','동원','율리','화명','수정','덕천','구명',
                  '구남','모라','모덕','덕포','사상','감전','주례','냉정','개금','동의대','가야','부암','서면','전포',
                  '국제금융센터·부산은행','문헌','지게골','못골','대연','경성대*부경대','남천','금련산','광안','수영',
                  '민락','센텀시티','벡스코(시립미술관)','동백','해운대','중동','장산']

subway_stations_3 = {
    '대저': (74,510),
    '체육공원': (165,510),
    '강서구청': (253,510),
    '구포': (342,510),
    '덕천': (429,510),
    '숙동': (488,510),
    '남산정': (532,510),
    '만덕': (578,510),
    '미남': (611,510),
    '사직': (658,510),
    '종합운동장': (694,510),
    '거제': (739,510),
    '연산': (807,510),
    '물만골': (867,510),
    '배산': (922,510),
    '망미': (976,510),
    '수영': (1055,510),
}

subway_lines_3 = ['대저','체육공원','강서구청','구포','덕천','숙동','남산정','만덕','미남','사직','종합운동장','거제','연산',
                  '물만골','배산','망미','수영']

subway_stations_4 = {
    '안평': (1415,251),
    '고촌': (1364,251),
    '윗반송': (1314,251),
    '영산대': (1263,251),
    '석대': (1213,251),
    '반여농산물시장': (1163,251),
    '금사': (1113,251),
    '서동': (1062,251),
    '명장': (1012,251),
    '충렬사': (962,251),
    '낙민': (908,251),
    '수안': (861,251),
    '동래': (807,251),
    '미남': (611,510),
}

subway_lines_4 = ['안평','고촌','윗반송','영산대','석대','반여농산물시장','금사','서동','명장','충렬사','낙민',
    '수안','동래', '미남']

subway_stations_Donhae = {
    '태화강': (1415,836),
    '개운포': (1390,836),
    '덕하': (1366,836),
    '망양': (1341,836),
    '남창': (1317,836),
    '서생': (1293,836),
    '월내': (1269,836),
    '좌천(동해선)': (1226,780),
    '일광': (1226,737),
    '기장': (1226,694),
    '오시리아': (1226,651),
    '송정': (1226,608),
    '신해운대': (1226,565),
    '벡스코(시립미술관)': (1226,510),
    '센텀': (1205,385),
    '재송': (1126,385),
    '부산원동': (1047,385),
    '안락': (969,385),
    '동래(동해선)': (891,385),
    '교대': (807,385),
    '거제': (739,510),
    '거제해맞이': (739,614),
    '부전': (739,721)
}

subway_lines_Donhae = [
    ['태화강', '개운포', '덕하', '망양', '남창', '서생', '월내', '좌천(동해선)', '일광', '기장', '오시리아', '송정', '신해운대', '벡스코(시립미술관)',
     '센텀', '재송', '부산원동', '안락', '동래', '교대', '거제', '거제해맞이', '부전']

]

subway_stations_BusanGimhae = {
    '가야대': (408,98),
    '장신대': (375,98),
    '연지공원': (338,98),
    '박물관': (301,98),
    '수로왕릉': (265,98),
    '봉황': (228,98),
    '부원': (192,98),
    '김해시청': (155,98),
    '인제대': (118,98),
    '김해대학': (85,109),
    '지내': (74,173),
    '불암': (74,251),
    '대사': (74,328),
    '평강': (74,406),
    '대저': (74,510),
    '등구': (74,627),
    '덕두': (74,755),
    '공항': (149,837),
    '서부산유통지구': (235,837),
    '괘법르네시떼': (320,837),
    '사상': (453,837)  
}

subway_lines_BusanGimhae = [
    ['가야대', '장신대', '연지공원', '박물관', '수로왕릉', '봉황', '부원', '김해시청', '인제대', '김해대학', '지내', '불암',
     '대사', '평강', '대저', '등구', '덕두', '공항', '서부산유통지구', '괘법르네시떼', '사상']
    
]

부산지하철_시간 = {
    # 1호선
    '노포': {'범어사': 1},
    '범어사': {'노포': 1, '남산': 2},
    '남산': {'범어사': 2, '두실': 1},
    '두실': {'남산': 1, '구서': 2},
    '구서': {'두실': 2, '장전': 2},
    '장전': {'구서': 2, '부산대': 2},
    '부산대': {'장전': 2, '온천장': 2},
    '온천장': {'부산대': 2, '명륜': 2},
    '명륜': {'온천장': 2, '동래': 2},
    '동래': {'명륜': 2, '교대': 2, '미남': 3, '수안': 2},
    '교대': {'동래': 2, '연산': 2, '거제': 2, '동래(동해선)': 3},
    '연산': {'교대': 2, '시청': 1, '거제': 2, '물만골': 2},
    '시청': {'연산': 1, '양정': 2},
    '양정': {'시청': 2, '부전': 2},
    '부전': {'양정': 2, '서면': 2, '거제해맞이': 3},
    '서면': {'부전': 2, '범내골': 2, '부암': 2, '전포': 3},
    '범내골': {'서면': 2, '범일': 2},
    '범일': {'범내골': 2, '좌천(1호선)': 2},
    '좌천(1호선)': {'범일': 2, '부산진': 2},
    '부산진': {'좌천(1호선)': 2, '초량': 2},
    '초량': {'부산진': 2, '부산역': 1},
    '부산역': {'초량': 1, '중앙': 2},
    '중앙': {'부산역': 2, '남포': 2},
    '남포': {'중앙': 2, '자갈치': 1},
    '자갈치': {'남포': 1, '토성': 3},
    '토성': {'자갈치': 3, '동대신': 3},
    '동대신': {'토성': 3, '서대신': 3},
    '서대신': {'동대신': 3, '대티': 2},
    '대티': {'서대신': 2, '괴정': 1},
    '괴정': {'대티': 1, '사하': 2},
    '사하': {'괴정': 2, '당리': 1},
    '당리': {'사하': 1, '하단': 2},
    '하단': {'당리': 2, '신평': 3},
    '신평': {'하단': 3, '동매': 3},
    '동매': {'신평': 3, '장림': 2},
    '장림': {'동매': 2, '신장림': 2},
    '신장림': {'장림': 2, '낫개': 2},
    '낫개': {'신장림': 2, '다대포항': 2},
    '다대포항': {'낫개': 2, '다대포해수욕장': 3},
    '다대포해수욕장': {'다대포항': 3},
    # 2호선
    '양산': {'남양산': 2},
    '남양산': {'양산': 2, '부산대양산캠퍼스': 2},
    '부산대양산캠퍼스': {'남양산':2, '증산': 2},
    '증산': {'부산대양산캠퍼스': 2, '호포': 4},
    '호포': {'증산': 4, '금곡': 3},
    '금곡': {'호포': 3, '동원': 2},
    '동원': {'금곡': 2, '율리': 2},
    '율리': {'동원': 2, '화명': 2},
    '화명': {'율리': 2, '수정': 2},
    '수정': {'화명': 2, '덕천': 3},
    '덕천': {'수정': 3, '구명': 2, '구포': 3, '숙등': 2},
    '구명': {'덕천': 2, '구남': 2},
    '구남': {'구명': 2, '모라': 2},
    '모라': {'구남': 2, '모덕': 1},
    '모덕': {'모라': 1, '덕포': 1},
    '덕포': {'모덕': 1, '사상': 3},
    '사상': {'덕포': 3, '감전': 2, '괘법르네시떼': 1},
    '감전': {'사상': 2, '주례': 2},
    '주례': {'감전': 2, '냉정': 2},
    '냉정': {'주례': 2, '개금': 2},
    '개금': {'냉정': 2, '동의대': 1},
    '동의대': {'개금': 1, '가야': 2},
    '가야': {'동의대': 2, '부암': 2},
    '부암': {'가야': 2, '서면': 2},
    '서면': {'부전': 2, '범내골': 2, '부암': 2, '전포': 3},
    '전포': {'서면': 3, '국제금융센터·부산은행': 2},
    '국제금융센터·부산은행': {'전포': 2, '문현': 2},
    '문현': {'국제금융센터·부산은행': 2, '지게골': 1},
    '지게골': {'문현': 1, '못골': 2},
    '못골': {'지게골': 2, '대연': 2},
    '대연': {'못골': 2, '경성대·부경대': 2},
    '경성대·부경대': {'대연': 2, '남천': 2},
    '남천': {'경성대·부경대': 2, '금련산': 2},
    '금련산': {'남천': 2, '광안': 2},
    '광안': {'금련산': 2, '수영': 2},
    '수영': {'광안': 2, '민락': 2, '망미': 2},
    '민락': {'수영': 2, '센텀시티': 2},
    '센텀시티': {'민락': 2, '벡스코(시립미술관)': 2},
    '벡스코(시립미술관)': {'센텀시티': 2, '동백': 2, '센텀': 2, '신해운대': 5},
    '동백': {'벡스코(시립미술관)': 2, '해운대': 2},
    '해운대': {'동백': 2, '중동': 2},
    '중동': {'해운대': 2, '장산': 2},
    '장산': {'중동': 2},
    # 3호선
    '대저': {'체육공원': 1, '평강': 1, '등구': 3},
    '체육공원': {'대저': 1, '강서구청': 2},
    '강서구청': {'체육공원': 2, '구포': 3},
    '구포': {'강서구청': 3, '덕천': 3},
    '덕천': {'수정': 3, '구명': 2, '구포': 3, '숙등': 2},
    '숙등': {'덕천': 2, '남산정 ': 2},
    '남산정 ': {'숙등': 2, '만덕': 2},
    '만덕': {'남산정 ': 2, '미남': 4},
    '미남': {'만덕': 4, '사직': 2, '동래': 3},
    '사직': {'미남': 2, '종합운동장': 2},
    '종합운동장': {'사직': 2, '거제': 1},
    '거제': {'종합운동장': 1, '연산': 2, '교대': 2, '거제해맞이': 2},
    '연산': {'교대': 2, '시청': 1, '거제': 2, '물만골': 2},
    '물만골': {'연산': 2, '배산': 3},
    '배산': {'물만골': 3, '망미': 2},
    '망미': {'배산': 2, '수영': 2},
    '수영': {'광안': 2, '민락': 2, '망미': 2},
    # 4호선
    '미남': {'만덕': 4, '사직': 2, '동래': 3},
    '동래': {'명륜': 2, '교대': 2, '미남': 3, '수안': 2},
    '수안': {'동래': 2, '낙민': 2},
    '낙민': {'수안': 2, '충렬사': 1},
    '충렬사': {'낙민': 1, '명장': 2},
    '명장': {'충렬사': 2, '서동': 2},
    '서동': {'명장': 2, '금사': 2},
    '금사': {'서동': 2, '반여농산물시장': 2},
    '반여농산물시장': {'금사': 2, '석대': 2},
    '석대': {'반여농산물시장': 2, '영산대': 2},
    '영산대': {'석대': 2, '윗반송': 3},
    '윗반송': {'영산대': 3, '고촌': 1},
    '고촌': {'윗반송': 1, '안평': 3},
    '안평': {'고촌': 3},
    # 동해선
    '부전': {'양정': 2, '서면': 2, '거제해맞이': 3},
    '거제해맞이': {'부전': 3, '거제': 2},
    '거제': {'종합운동장': 1, '연산': 2, '교대': 2, '거제해맞이': 2},
    '교대': {'동래': 2, '연산': 2, '거제': 2, '동래(동해선)': 3},
    '동래(동해선)': {'교대': 3, '안락': 2},
    '안락': {'동래(동해선)': 2, '부산원동': 2},
    '부산원동': {'안락': 2, '재송': 1},
    '재송': {'부산원동': 1, '센텀': 2},
    '센텀': {'재송': 2, '벡스코(시립미술관)': 2},
    '벡스코(시립미술관)': {'센텀시티': 2, '동백': 2, '센텀': 2, '신해운대': 5},
    '신해운대': {'벡스코(시립미술관)': 5, '송정': 3},
    '송정': {'신해운대': 3, '오시리아': 3},
    '오시리아': {'송정': 3, '기장': 4},
    '기장': {'오시리아': 4, '일광': 3},
    '일광': {'기장': 3, '좌천(동해선)': 4},
    '좌천(동해선)': {'일광': 4, '월내': 3},
    '월내': {'좌천(동해선)': 3, '서생': 3},
    '서생': {'월내': 3, '남창': 7},
    '남창': {'서생': 7, '망양': 4},
    '망양': {'남창': 4, '덕하': 4},
    '덕하': {'망양': 4, '개운포': 2},
    '개운포': {'덕하': 2, '태화강': 4},
    '태화강': {'개운포': 4},
    # 부산김해
    '가야대': {'장신대': 2},
    '장신대': {'가야대': 2, '연지공원': 3},
    '연지공원': {'장신대': 3, '박물관': 2},
    '박물관': {'연지공원': 2, '수로왕릉': 2},
    '수로왕릉': {'박물관': 2, '봉황': 1},
    '봉황': {'수로왕릉': 1, '부원': 2},
    '부원': {'봉황': 2, '김해시청': 2},
    '김해시청': {'부원': 2, '인제대': 2},
    '인제대': {'김해시청': 2, '김해대학': 2},
    '김해대학': {'인제대': 2, '지내': 1},
    '지내': {'김해대학': 1, '불암': 2},
    '불암': {'지내': 2, '대사': 2},
    '대사': {'불암': 2, '평강': 2},
    '평강': {'대사': 2, '대저': 2},
    '대저': {'체육공원': 1, '평강': 1, '등구': 3},
    '등구': {'대저': 3, '덕두': 3},
    '덕두': {'등구': 3, '김해공항': 2},
    '김해공항': {'덕두': 2, '서부산유통지구': 2},
    '서부산유통지구': {'김해공항': 2, '괘법르네시떼': 2},
    '괘법르네시떼': {'서부산유통지구': 2, '사상': 1},
    '사상': {'덕포': 3, '감전': 2, '괘법르네시떼': 1},
}

부산지하철_환승 = {
    '동래': {'수안', '미남', '명륜', '교대'},
    '교대': {'동래(동해선)', '거제', '동래', '연산'},
    '연산': {'거제', '물만골', '교대', '시청'},
    '부전': {'거제해맞이', '양정', '서면'},
    '서면': {'부암', '전포', '부전', '범내골'},
    '덕천': {'구포', '숙등', '수정', '구명'},
    '사상': {'괘법르네시떼', '덕포', '감전'},
    '수영': {'망미', '민락', '광안'},
    '벡스코(시립미술관)': {'센텀', '신해운대', '센텀시티', '동백'},
    '대저': {'평강', '등구', '체육공원'},
    '미남': {'동래', '만덕', '사직'},
    '거제': {'교대', '거제해맞이', '종합운동장', '연산'},
}

부산지하철_거리 = {
    # 1호선
    '노포': {'범어사': 1.2},
    '범어사': {'노포': 1.2, '남산': 0.9},
    '남산': {'범어사': 0.9, '두실': 1},
    '두실': {'남산': 1, '구서': 1},
    '구서': {'두실': 1, '장전': 1.1},
    '장전': {'구서': 1.1, '부산대': 1},
    '부산대': {'장전': 1, '온천장': 1.1},
    '온천장': {'부산대': 1.1, '명륜': 1},
    '명륜': {'온천장': 1, '동래': 0.8},
    '동래': {'명륜': 0.8, '교대': 1.2, '미남': 1, '수안': 0.7},
    '교대': {'동래': 1.2, '연산': 1, '거제': 0.7, '동래(동해선)': 1.2},
    '연산': {'교대': 1, '시청': 0.9, '거제': 0.7, '물만골': 1.1},
    
    '시청': {'연산': 0.9, '양정': 0.8},
    
    '양정': {'시청': 0.8, '부전': 1.4},
    
    '부전': {'양정': 1.4, '서면': 0.6, '거제해맞이': 2.3},
    
    '서면': {'부전': 0.6, '범내골': 1.2, '부암': 0.8, '전포': 1.1},
    
    '범내골': {'서면': 1.2, '범일': 0.8},
    
    '범일': {'범내골': 0.8, '좌천(1호선)': 0.9},
    
    '좌천(1호선)': {'범일': 0.9, '부산진': 1},
    
    '부산진': {'좌천(1호선)': 1, '초량': 0.8},
    
    '초량': {'부산진': 0.8, '부산역': 0.8},
    
    '부산역': {'초량': 0.8, '중앙': 1.1},
    
    '중앙': {'부산역': 1.1, '남포': 0.9},
    
    '남포': {'중앙': 0.9, '자갈치': 0.7},
    
    '자갈치': {'남포': 0.7, '토성': 1},
    
    '토성': {'자갈치': 1, '동대신': 1.2},
    
    '동대신': {'토성': 1.2, '서대신': 0.7},
    
    '서대신': {'동대신': 0.7, '대티': 1.4},
    
    '대티': {'서대신': 1.4, '괴정': 0.8},
    
    '괴정': {'대티': 0.8, '사하': 0.9},
    
    '사하': {'괴정': 0.9, '당리': 0.9},
    
    '당리': {'사하': 0.9, '하단': 0.8},
    
    '하단': {'당리': 0.8, '신평': 1.6},
    
    '신평': {'하단': 1.6, '동매': 1.7},
    
    '동매': {'신평': 1.7, '장림': 1.2},
    
    '장림': {'동매': 1.2, '신장림': 0.8},
    
    '신장림': {'장림': 0.8, '낫개': 1.1},
    
    '낫개': {'신장림': 1.1, '다대포항': 1.2},
    
    '다대포항': {'낫개': 1.2, '다대포해수욕장': 1.4},
    '다대포해수욕장': {'다대포항': 1.4},
    # 2호선
    '양산': {'남양산': 1.6},
    
    '남양산': {'양산': 1.6, '부산대양산캠퍼스': 1.1},
    
    '부산대양산캠퍼스': {'남양산':1.1, '증산': 1},
    
    '증산': {'부산대양산캠퍼스': 1, '호포': 3.5},
    
    '호포': {'증산': 3.5, '금곡': 1.5},
    
    '금곡': {'호포': 1.5, '동원': 1},
    
    '동원': {'금곡': 1, '율리': 1.5},
    
    '율리': {'동원': 1.5, '화명': 1.2},
    
    '화명': {'율리': 1.2, '수정': 1.5},
    
    '수정': {'화명': 1.5, '덕천': 1.5},
    
    '덕천': {'수정': 1.5, '구명': 1.2, '구포': 1.1, '숙등': 0.7},
    
    '구명': {'덕천': 1.2, '구남': 0.7},
    
    '구남': {'구명': 0.7, '모라': 1.1},
    
    '모라': {'구남': 1.1, '모덕': 1},
    
    '모덕': {'모라': 1, '덕포': 0.8},
    
    '덕포': {'모덕': 0.8, '사상': 1.2},
    
    '사상': {'덕포': 1.2, '감전': 1.1, '괘법르네시떼': 0.8},
    
    '감전': {'사상': 1.1, '주례': 1.2},
    
    '주례': {'감전': 1.2, '냉정': 0.9},
    
    '냉정': {'주례': 0.9, '개금': 0.8},
    
    '개금': {'냉정': 0.8, '동의대': 1.1},
    
    '동의대': {'개금': 1.1, '가야': 0.9},
    
    '가야': {'동의대': 0.9, '부암': 0.7},
    
    '부암': {'가야': 0.7, '서면': 0.8},
    
    '서면': {'부전': 0.6, '범내골': 1.2, '부암': 0.8, '전포': 1.1},
    
    '전포': {'서면': 1.1, '국제금융센터·부산은행': 0.8},
    
    '국제금융센터·부산은행': {'전포': 0.8, '문현': 0.8},
    
    '문현': {'국제금융센터·부산은행': 0.8, '지게골': 0.8},
    
    '지게골': {'문현': 0.8, '못골': 0.9},
    
    '못골': {'지게골': 0.9, '대연': 0.7},
    
    '대연': {'못골': 0.7, '경성대·부경대': 0.9},
    
    '경성대·부경대': {'대연': 0.9, '남천': 0.8},
    
    '남천': {'경성대·부경대': 0.8, '금련산': 0.9},
    
    '금련산': {'남천': 0.9, '광안': 0.9},
    
    '광안': {'금련산': 0.9, '수영': 0.9},
    
    '수영': {'광안': 0.9, '민락': 0.9, '망미': 1},
    
    '민락': {'수영': 0.9, '센텀시티': 1},
    
    '센텀시티': {'민락': 1, '벡스코(시립미술관)': 0.8},
    
    '벡스코(시립미술관)': {'센텀시티': 0.8, '동백': 1.1, '센텀': 1.4, '신해운대': 4.5},
    
    '동백': {'벡스코(시립미술관)': 1.1, '해운대': 1.2},
    
    '해운대': {'동백': 1.2, '중동': 0.9},
    
    '중동': {'해운대': 0.9, '장산': 0.9},
    '장산': {'중동': 0.9},
    # 3호선
    '대저': {'체육공원': 0.8, '평강': 1, '등구': 2},
    
    '체육공원': {'대저': 0.8, '강서구청': 1.1},
    
    '강서구청': {'체육공원': 1.1, '구포': 1.6},
    
    '구포': {'강서구청': 1.6, '덕천': 1.1},
    
    '덕천': {'수정': 1.5, '구명': 1.2, '구포': 1.1, '숙등': 0.7},
    
    '숙등': {'덕천': 0.7, '남산정 ': 1},
    
    '남산정 ': {'숙등': 1, '만덕': 1.1},
    
    '만덕': {'남산정 ': 1.1, '미남': 3.3},
    
    '미남': {'만덕': 3.3, '사직': 0.8, '동래': 1},
    
    '사직': {'미남': 0.8, '종합운동장': 0.8},
    
    '종합운동장': {'사직': 0.8, '거제': 0.7},
    
    '거제': {'종합운동장': 0.7, '연산': 0.7, '교대': 0.7, '거제해맞이': 1},
    
    '연산': {'교대': 1, '시청': 0.9, '거제': 0.7, '물만골': 1.1},
    
    '물만골': {'연산': 1.1, '배산': 1.1},
    
    '배산': {'물만골': 1.1, '망미': 1.2},
    
    '망미': {'배산': 1.2, '수영': 1},
    
    '수영': {'광안': 0.9, '민락': 0.9, '망미': 1},
    # 4호선
    '미남': {'만덕': 3.3, '사직': 0.8, '동래': 1},
    
    '동래': {'명륜': 0.8, '교대': 1.2, '미남': 1, '수안': 0.7},
    
    '수안': {'동래': 0.7, '낙민': 0.7},
    
    '낙민': {'수안': 0.7, '충렬사': 0.7},
    
    '충렬사': {'낙민': 0.7, '명장': 0.7},
    
    '명장': {'충렬사': 0.7, '서동': 1},
    
    '서동': {'명장': 1, '금사': 0.8},
    
    '금사': {'서동': 0.8, '반여농산물시장': 0.8},
    
    '반여농산물시장': {'금사': 0.8, '석대': 1.2},
    
    '석대': {'반여농산물시장': 1.2, '영산대': 1.4},
    
    '영산대': {'석대': 1.4, '윗반송': 1.1},
    
    '윗반송': {'영산대': 1.1, '고촌': 0.8},
    
    '고촌': {'윗반송': 0.8, '안평': 1.1},
    '안평': {'고촌': 1.1},
    # 동해선
    '부전': {'양정': 1.4, '서면': 0.6, '거제해맞이': 2.3},
    
    '거제해맞이': {'부전': 2.3, '거제': 1},
    
    '거제': {'종합운동장': 0.7, '연산': 0.7, '교대': 0.7, '거제해맞이': 1},
    
    '교대': {'동래': 1.2, '연산': 1, '거제': 0.7, '동래(동해선)': 1.2},
    
    '동래(동해선)': {'교대': 1.2, '안락': 0.9},
    
    '안락': {'동래(동해선)': 0.9, '부산원동': 1.2},
    
    '부산원동': {'안락': 1.2, '재송': 1.1},
    
    '재송': {'부산원동': 1.1, '센텀': 1},
    
    '센텀': {'재송': 1, '벡스코(시립미술관)': 1.4},
    
    '벡스코(시립미술관)': {'센텀시티': 0.8, '동백': 1.1, '센텀': 1.4, '신해운대': 4.5},
    
    '신해운대': {'벡스코(시립미술관)': 4.5, '송정': 2.9},
    
    '송정': {'신해운대': 2.9, '오시리아': 1.1},
    
    '오시리아': {'송정': 1.1, '기장': 5.7},
    
    '기장': {'오시리아': 5.7, '일광': 3},
    
    '일광': {'기장': 3, '좌천(동해선)': 5.1},
    
    '좌천(동해선)': {'일광': 5.1, '월내': 3.5},
    
    '월내': {'좌천(동해선)': 3.5, '서생': 2.6},
    
    '서생': {'월내': 2.6, '남창': 8.4},
    
    '남창': {'서생': 8.4, '망양': 4.4},
    
    '망양': {'남창': 4.4, '덕하': 4.5},
    
    '덕하': {'망양': 4.5, '개운포': 2.4},
    
    '개운포': {'덕하': 2.4, '태화강': 4.9},
    '태화강': {'개운포': 4.9},
    # 부산김해
    '가야대': {'장신대': 0.9},
    
    '장신대': {'가야대': 0.9, '연지공원': 1.2},
    
    '연지공원': {'장신대': 1.2, '박물관': 1.1},
    
    '박물관': {'연지공원': 1.1, '수로왕릉': 0.8},
    
    '수로왕릉': {'박물관': 0.8, '봉황': 0.7},
    
    '봉황': {'수로왕릉': 0.7, '부원': 1},
    
    '부원': {'봉황': 1, '김해시청': 0.6},
    
    '김해시청': {'부원': 0.6, '인제대': 1},
    
    '인제대': {'김해시청': 1, '김해대학': 1.3},
    
    '김해대학': {'인제대': 1.3, '지내': 0.8},
    
    '지내': {'김해대학': 0.8, '불암': 0.7},
    
    '불암': {'지내': 0.7, '대사': 1.1},
    
    '대사': {'불암': 1.1, '평강': 1.2},
    
    '평강': {'대사': 1.2, '대저': 1},
    
    '대저': {'체육공원': 0.8, '평강': 1, '등구': 2},
    
    '등구': {'대저': 2, '덕두': 1.9},
    
    '덕두': {'등구': 1.9, '김해공항': 1.3},
    
    '김해공항': {'덕두': 1.3, '서부산유통지구': 0.9},
    
    '서부산유통지구': {'김해공항': 0.9, '괘법르네시떼': 2.3},
    
    '괘법르네시떼': {'서부산유통지구': 2.3, '사상': 0.8},
    
    '사상': {'덕포': 1.2, '감전': 1.1, '괘법르네시떼': 0.8},
}

부산지하철_검색 = {
    
}



#노선도 좌표 만들기
line_1= traincanvas.create_line(1415,98,1343,98,1343,98,1272,98,1200,98,1129,98,1057,98,986,98,915,98,843,98,807,251,807,385,
                                807,510,807,582,807,666,807,750,807,837,807,909,807,980,778,1020,744,1020,711,1020,677,1020,643,1020,
                                610,1020,577,1020,543,1020,510,1020,476,1020,443,1020,410,1020,376,1020,343,1020,309,1020,
                                275,1020,241,1020,208,1020,175,1020,142,1020,108,1020,74,1020,width=10, fill="orange")    #1호선

line_2= traincanvas.create_line(728,98,682,98,635,98,586,98,539,98,492,98,445,104,429,148,429,288,429,391,429,510,429,561,429,619,
                                429,675,429,732,429,787,453,837,504,837,547,837,589,837,632,837,719,837,761,837,807,837,853,837,883,837,
                                915,837,947,837,976,837,1006,837,1039,805,1039,735,1039,665,1039,594,1055,510,1113,510,1172,510,
                                1172,510,1226,510,1277,510,1322,510,1368,510,1415,510, width=10, fill="light green")  #2호선

line_3= traincanvas.create_line(74,510,165,510,253,510,342,510,428,510,488,510,532,510,611,510,658,510,694,510,739,510,807,510,
                                867,510,922,510,976,510,1055,510, width=10,fill="gold")   #3호선

line_4= traincanvas.create_line(1415,251,1364,251,1314,251,1263,251,1213,251,1163,251,1113,251,1062,251,962,251,908,251,861,251,
                                807,251,611,251,611,510, width=10, fill="skyblue")  #4호선

line_5= traincanvas.create_line(408,98,375,98,338,98,301,98,265,98,228,98,192,98,155,98,118,98,85,109,74,173,74,251,74,328,74,406,
                                74,510,74,627,74,755,149,837,235,837,320,837,453,837, width=10,fill="mediumpurple")   #부산김해경전철

line_6= traincanvas.create_line(1415,836,1390,836,1366,836,1341,836,1317,836,1293,836,1269,836,1226,780,1226,737,1226,694,1226,651,
                                1226,608,1226,565,1226,511,1205,385,1047,385,969,385,891,385,807,385,739,510,739,614,739,721, width=10, fill="blue")    #동해선


# 함수 추가: 마우스 클릭 이벤트 핸들러
def show_station(event):
    x = event.x
    y = event.y
    
    # 기존의 빨간 점 삭제
    traincanvas.delete("red_dot")
    
    # 반복문을 통해 클릭한 좌표와 가장 가까운 역을 찾음
    closest_station = None
    min_distance = float('inf')
    for station, (station_x, station_y) in subway_stations_1.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_2.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_3.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_4.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_Donhae.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_BusanGimhae.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
                                            
    # 클릭한 역을 캔버스에 표시
    if closest_station:
        if input_entry.get() == "":  # 출발역이 입력되지 않은 경우
            input_entry.delete(0, tk.END)
            input_entry.insert(0, closest_station)  # 출발역 입력
        else:
            destination_entry.delete(0, tk.END)
            destination_entry.insert(0, closest_station)  # 도착역 입력

        station_x, station_y = None, None
        if closest_station in subway_stations_1:
            station_x, station_y = subway_stations_1[closest_station]
        elif closest_station in subway_stations_2:
            station_x, station_y = subway_stations_2[closest_station]
        elif closest_station in subway_stations_3:
            station_x, station_y = subway_stations_3[closest_station]
        elif closest_station in subway_stations_4:
            station_x, station_y = subway_stations_4[closest_station]
        elif closest_station in subway_stations_Donhae:
            station_x, station_y = subway_stations_Donhae[closest_station]
        elif closest_station in subway_stations_BusanGimhae:
            station_x, station_y = subway_stations_BusanGimhae[closest_station]

        if station_x is not None and station_y is not None:
            traincanvas.create_oval(station_x - 5, station_y - 5, station_x + 5, station_y + 5, fill='red', tags="red_dot")


# 지하철 노선도 그리기
for line in subway_lines_BusanGimhae:
    for i in range(len(line) - 1):
        start_station = subway_stations_BusanGimhae[line[i]]
        end_station = subway_stations_BusanGimhae[line[i + 1]]
        traincanvas.create_line(start_station[0], start_station[1], end_station[0], end_station[1], fill='mediumpurple', width=3)

# 지하철 역 표시
for station, (x, y) in subway_stations_BusanGimhae.items():
    traincanvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="mediumpurple", width=2.5)

# def show_coordinates(event):
#     x = event.x
#     y = event.y
#     traincanvas.coords(cursor_text, x, y)
#     traincanvas.itemconfigure(cursor_text, text=f"   ({x}, {y})")
    
def draw_subway_map(canvas):
    # 지하철 노선 그리기
    for line in subway_lines_1:
        for i in range(len(line) - 1):
            start_station = subway_stations_1[line[i]]
            end_station = subway_stations_1[line[i + 1]]
            canvas.create_line(start_station[0], start_station[1], end_station[0], end_station[1], fill='orange', width=3)

    # 지하철 역 표시
    for station, (x, y) in subway_stations_1.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="orange", width=2.5)
    for station, (x, y) in subway_stations_2.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="light green", width=2.5)
    for station, (x, y) in subway_stations_3.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="gold", width=2.5)       
    for station, (x, y) in subway_stations_4.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="sky blue", width=2.5)
    for station, (x, y) in subway_stations_Donhae.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="blue", width=2.5)
    for station, (x, y) in subway_stations_BusanGimhae.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="mediumpurple", width=2.5)            

# 지하철 노선도 그리기
draw_subway_map(traincanvas)

# 마우스 이벤트 바인딩
# traincanvas.bind("<Motion>", show_coordinates)
traincanvas.bind("<Button-1>", show_station)

# 마우스 이벤트로 표시될 텍스트 객체
# cursor_text = traincanvas.create_text(10, 10, text="", anchor="nw")

# 입력 창 생성
input_frame = tk.Frame(Lframe_bottom, bg="lightgray", width=30, height=50)
input_frame.pack(pady=10, anchor=N)


start_label = tk.Label(Lframe_bottom, text="출발역 : ", bg="lightgray")
start_label.place(x=25, y=8)

input_entry = tk.Entry(input_frame, width=30)
input_entry.grid(row=0, column=1)
input_entry.bind("<Return>", Enterfunc1)

destination_label = tk.Label(Lframe_bottom, text="도착역 : ", bg="lightgray")
destination_label.place(x=25, y=28)

destination_entry = tk.Entry(input_frame, width=30)
destination_entry.grid(row=1, column=1)
destination_entry.bind("<Return>", Enterfunc2)

label_1 = Label(frame1came1, text="출발 : ", font=("Arial", 15), bg="lightgray")
label_1.place(x=55, y=80)

label_2 = Label(frame1came1, text="도착 : ", font=("Arial", 15), bg="lightgray")
label_2.place(x=55, y=110)

timelabel = Label(frame1came1, text="현재시각 : ", font=("Arial", 15), bg="lightgray")
timelabel.place(x=55, y=140)

start_label = Label(Lframe_top, text="출발지점", font=("Arial", 15), background="lightgray")
start_label.place(x=55, y=195)

end_label = Label(Lframe_top, text="도착지점", font=("Arial", 15), background="lightgray")
end_label.place(x=55, y=225)
 
start_combobox = ttk.Combobox(Lframe_top, height=10, values=start_list)
start_combobox.place(x=160, y=200)
start_combobox.bind("<<ComboboxSelected>>", set_start_station)
start_combobox.bind("<Return>", Enterfunc3)

searchlist1 = Listbox(Lframe_top, selectmode="single", height=10)
searchlist1.place(x=50, y=300, width=100, height=150)
searchlist1.bind("<Double-Button-1>", doubleclick1)

scroll1 = Scrollbar(Lframe_top, orient="vertical")
scroll1.place(x=150, y=300, height=150)
searchlist1.config(yscrollcommand=scroll1.set)
scroll1.config(command=searchlist1.yview)

searchlist2 = Listbox(Lframe_top, selectmode="single", height=10)
searchlist2.place(x=240, y=300, width=100, height=150)
searchlist2.bind("<Double-Button-1>", doubleclick2)

scroll2 = Scrollbar(Lframe_top, orient="vertical")
scroll2.place(x=340, y=300, height=150)
searchlist2.config(yscrollcommand=scroll2.set)
scroll2.config(command=searchlist2.yview)


searchbutton = Button(Lframe_bottom, text="검색", font=("Arial", 15), background="cyan", command=lambda: (start_info(), end_info(), result()))
searchbutton.place(x=112, y=60)

resetbutton = Button(Lframe_bottom, text="초기화", font=("Arial", 15), command=reset_func)
resetbutton.place(x=212, y=60)

changebutton = Button(Lframe_bottom, text="↑↓", width=5, height=2, command=changeentry)
changebutton.place(x=315, y=9)

# 검색 결과 라벨
resultlabel = Label(Lframe_bottom, border=1, width=40, height=10, justify='center', font=("Arial", 15), padx=0, pady=0, bg="lightgray")
resultlabel.place(x=0, y=120)

end_combobox = ttk.Combobox(Lframe_top, height=10, values=end_list)
end_combobox.place(x=160, y=230)
end_combobox.bind("<<ComboboxSelected>>", set_end_station)
end_combobox.bind("<Return>", Enterfunc4)

btn1 = Button(frame2came1, text="노포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("노포"), newwindow1()))
btn1.place(x=1405, y=78)

btn2 = Button(frame2came1, text="범어사", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("범어사"), newwindow2()))
btn2.place(x=1328, y=78)

btn3 = Button(frame2came1, text="남산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("남산"), newwindow3()))
btn3.place(x=1262, y=78)

btn4 = Button(frame2came1, text="두실", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("두실"), newwindow4()))
btn4.place(x=1190, y=78)

btn5 = Button(frame2came1, text="선릉", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("선릉"), newwindow5()))
btn5.place(x=1120, y=78)

btn6 = Button(frame2came1, text="장전", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("장전"), newwindow6()))
btn6.place(x=1048, y=78)

btn7 = Button(frame2came1, text="부산대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부산대"), newwindow7()))
btn7.place(x=971, y=78)

btn8 = Button(frame2came1, text="온천장", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("온천장"), newwindow13()))
btn8.place(x=900, y=78)

btn9 = Button(frame2came1, text="명륜", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("명륜"), newwindow9()))
btn9.place(x=833, y=78)

btn10 = Button(frame2came1, text="동래", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동래"), newwindow10()))
btn10.place(x=772, y=230)

btn11 = Button(frame2came1, text="교대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("교대"), newwindow11()))
btn11.place(x=772, y=370)

btn12 = Button(frame2came1, text="연산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("연산"), newwindow12()))
btn12.place(x=772, y=490)

btn13 = Button(frame2came1, text="시청", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("시청"), newwindow13()))
btn13.place(x=772, y=582)

btn14 = Button(frame2came1, text="양정", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("양정"), newwindow14()))
btn14.place(x=772, y=666)

btn15 = Button(frame2came1, text="부전", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부전"), newwindow15()))
btn15.place(x=772, y=750)

btn16 = Button(frame2came1, text="서면", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("서면"), newwindow16()))
btn16.place(x=772, y=817)

btn17 = Button(frame2came1, text="범내골", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("범내골"), newwindow17()))
btn17.place(x=757, y=909)

btn18 = Button(frame2came1, text="범일", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("범일"), newwindow18()))
btn18.place(x=772, y=965)

btn19 = Button(frame2came1, text="좌천(1호선)", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("좌천(1호선)"), newwindow19()))
btn19.place(x=772, y=1040)

btn20 = Button(frame2came1, text="부산진", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부산진"), newwindow20()))
btn20.place(x=727, y=1000)

btn21 = Button(frame2came1, text="초량", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("초량"), newwindow21()))
btn21.place(x=702, y=1040)

btn22 = Button(frame2came1, text="부산역", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부산역"), newwindow22()))
btn22.place(x=662, y=1000)

btn23 = Button(frame2came1, text="중앙", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("중앙"), newwindow23()))
btn23.place(x=635, y=1040)

btn24 = Button(frame2came1, text="남포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("남포"), newwindow24()))
btn24.place(x=600, y=1000)

btn25 = Button(frame2came1, text="자갈치", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("자갈치"), newwindow25()))
btn25.place(x=562, y=1040)

btn26 = Button(frame2came1, text="토성", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("토성"), newwindow26()))
btn26.place(x=533, y=1000)

btn27 = Button(frame2came1, text="동대신", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동대신"), newwindow27()))
btn27.place(x=495, y=1040)

btn28 = Button(frame2came1, text="서대신", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("서대신"), newwindow28()))
btn28.place(x=461, y=1000)

btn29 = Button(frame2came1, text="대티", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("대티"), newwindow29()))
btn29.place(x=433, y=1040)

btn30 = Button(frame2came1, text="과정", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("과정"), newwindow30()))
btn30.place(x=400, y=1000)

btn31 = Button(frame2came1, text="사하", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("사하"), newwindow31()))
btn31.place(x=366, y=1040)

btn32 = Button(frame2came1, text="당리", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("당리"), newwindow32()))
btn32.place(x=333, y=1000)

btn33 = Button(frame2came1, text="하단", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("하단"), newwindow33()))
btn33.place(x=299, y=1040)

btn34 = Button(frame2came1, text="신평", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("신평"), newwindow34()))
btn34.place(x=265, y=1000)

btn35 = Button(frame2came1, text="동매", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동매"), newwindow35()))
btn35.place(x=231, y=1040)

btn36 = Button(frame2came1, text="장림", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("장림"), newwindow36()))
btn36.place(x=198, y=1000)

btn37 = Button(frame2came1, text="신장림", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("신장림"), newwindow37()))
btn37.place(x=160, y=1040)

btn38 = Button(frame2came1, text="낫개", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("낫개"), newwindow38()))
btn38.place(x=132, y=1000)

btn39 = Button(frame2came1, text="다대포항", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("다대포항"), newwindow39()))
btn39.place(x=88, y=1040)

btn40 = Button(frame2came1, text="다대포해수욕장", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("다대포해수욕장"), newwindow40()))
btn40.place(x=34, y=1000)

btn41 = Button(frame2came1, text="양산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("양산"), newwindow41()))
btn41.place(x=718, y=78)

btn42 = Button(frame2came1, text="남양산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("남양산"), newwindow42()))
btn42.place(x=667, y=78)

btn43 = Button(frame2came1, text="부산대중앙캠퍼스", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부산대중앙캠퍼스"), newwindow43()))
btn43.place(x=590, y=118)

btn44 = Button(frame2came1, text="중산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("중산"), newwindow44()))
btn44.place(x=576, y=78)

btn45 = Button(frame2came1, text="호포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("호포"), newwindow45()))
btn45.place(x=529, y=78)

btn46 = Button(frame2came1, text="금곡", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("금곡"), newwindow46()))
btn46.place(x=482, y=78)

btn47 = Button(frame2came1, text="동원", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동원"), newwindow47()))
btn47.place(x=435, y=84)

btn48 = Button(frame2came1, text="율리", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("율리"), newwindow48()))
btn48.place(x=394, y=148)

btn49 = Button(frame2came1, text="화명", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("화명"), newwindow49()))
btn49.place(x=394, y=288)

btn50 = Button(frame2came1, text="수정", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("수정"), newwindow50()))
btn50.place(x=394, y=391)

btn51 = Button(frame2came1, text="덕천", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("덕천"), newwindow51()))
btn51.place(x=394, y=490)

btn52 = Button(frame2came1, text="구명", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("구명"), newwindow52()))
btn52.place(x=394, y=561)

btn53 = Button(frame2came1, text="구남", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("구남"), newwindow53()))
btn53.place(x=394, y=619)

btn54 = Button(frame2came1, text="모라", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("모라"), newwindow54()))
btn54.place(x=394, y=675)

btn55 = Button(frame2came1, text="모덕", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("모덕"), newwindow55()))
btn55.place(x=394, y=732)

btn56 = Button(frame2came1, text="덕포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("덕포"), newwindow56()))
btn56.place(x=394, y=787)

btn57 = Button(frame2came1, text="사상", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("사상"), newwindow57()))
btn57.place(x=443, y=857)

btn58 = Button(frame2came1, text="감전", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("감전"), newwindow58()))
btn58.place(x=494, y=857)

btn59 = Button(frame2came1, text="주례", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("주례"), newwindow59()))
btn59.place(x=537, y=857)

btn60 = Button(frame2came1, text="냉정", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("냉정"), newwindow60()))
btn60.place(x=579, y=857)

btn61 = Button(frame2came1, text="개금", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("개금"), newwindow61()))
btn61.place(x=622, y=857)

btn62 = Button(frame2came1, text="동의대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동의대"), newwindow62()))
btn62.place(x=660, y=857)

btn63 = Button(frame2came1, text="가야", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("가야"), newwindow63()))
btn63.place(x=709, y=857)

btn64 = Button(frame2came1, text="부암", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부암"), newwindow64()))
btn64.place(x=751, y=857)

btn65 = Button(frame2came1, text="전포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("전포"), newwindow65()))
btn65.place(x=843, y=857)

btn66 = Button(frame2came1, text="국제금융센터\n부산은행", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("국제금융센터·부산은행"), newwindow66()))
btn66.place(x=853, y=797)

btn67 = Button(frame2came1, text="문현", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("문현"), newwindow67()))
btn67.place(x=905, y=857)

btn68 = Button(frame2came1, text="지게골", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("지게골"), newwindow68()))
btn68.place(x=932, y=817)

btn69 = Button(frame2came1, text="못골", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("못골"), newwindow69()))
btn69.place(x=966, y=857)

btn70 = Button(frame2came1, text="대연", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("대연"), newwindow70()))
btn70.place(x=996, y=857)

btn71 = Button(frame2came1, text="경성대·\n부경대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("경성대·부경대"), newwindow71()))
btn71.place(x=1059, y=795)

btn72 = Button(frame2came1, text="남천", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("남천"), newwindow72()))
btn72.place(x=1059, y=735)

btn73 = Button(frame2came1, text="금련산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("금련산"), newwindow73()))
btn73.place(x=1059, y=665)

btn74 = Button(frame2came1, text="광안", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("광안"), newwindow74()))
btn74.place(x=1059, y=594)

btn75 = Button(frame2came1, text="수영", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("수영"), newwindow75()))
btn75.place(x=1070, y=530)

btn76 = Button(frame2came1, text="민락", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("민락"), newwindow76()))
btn76.place(x=1103, y=530)

btn77 = Button(frame2came1, text="센텀시티", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("센텀시티"), newwindow77()))
btn77.place(x=1152, y=530)

btn78 = Button(frame2came1, text="벡스코(시립미술관)", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("벡스코(시립미술관)"), newwindow78()))
btn78.place(x=1236, y=480)

btn79 = Button(frame2came1, text="동백", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동백"), newwindow79()))
btn79.place(x=1267, y=530)

btn80 = Button(frame2came1, text="해운대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("해운대"), newwindow80()))
btn80.place(x=1307, y=530)

btn81 = Button(frame2came1, text="중동", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("중동"), newwindow81()))
btn81.place(x=1358, y=530)

btn82 = Button(frame2came1, text="장산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("장산"), newwindow82()))
btn82.place(x=1405, y=530)

btn83 = Button(frame2came1, text="대저", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("대저"), newwindow83()))
btn83.place(x=94, y=530)

btn84 = Button(frame2came1, text="체육공원", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("체육공원"), newwindow84()))
btn84.place(x=145, y=530)

btn85 = Button(frame2came1, text="강서구청", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("강서구청"), newwindow85()))
btn85.place(x=233, y=530)

btn86 = Button(frame2came1, text="구포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("구포"), newwindow86()))
btn86.place(x=332, y=530)

btn87 = Button(frame2came1, text="숙동", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("숙동"), newwindow87()))
btn87.place(x=478, y=530)

btn88 = Button(frame2came1, text="남산정", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("남산정"), newwindow88()))
btn88.place(x=517, y=530)

btn89 = Button(frame2came1, text="만덕", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("만덕"), newwindow89()))
btn89.place(x=568, y=530)

btn90 = Button(frame2came1, text="미남", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("미남"), newwindow90()))
btn90.place(x=601, y=530)

btn91 = Button(frame2came1, text="사직", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("사직"), newwindow91()))
btn91.place(x=648, y=530)

btn92 = Button(frame2came1, text="종합운동장", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("종합운동장"), newwindow92()))
btn92.place(x=669, y=490)

btn93 = Button(frame2came1, text="거제", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("거제"), newwindow93()))
btn93.place(x=754, y=530)

btn94 = Button(frame2came1, text="물만골", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("물만골"), newwindow94()))
btn94.place(x=852, y=530)

btn95 = Button(frame2came1, text="배산", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("배산"), newwindow95()))
btn95.place(x=912, y=530)

btn96 = Button(frame2came1, text="망미", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("망미"), newwindow96()))
btn96.place(x=966, y=530)

btn97 = Button(frame2came1, text="안평", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("안평"), newwindow97()))
btn97.place(x=1405, y=231)

btn98 = Button(frame2came1, text="고촌", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("고촌"), newwindow98()))
btn98.place(x=1354, y=231)

btn99 = Button(frame2came1, text="윗반송", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("윗반송"), newwindow99()))
btn99.place(x=1299, y=231)

btn100 = Button(frame2came1, text="영산대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("영산대"), newwindow100()))
btn100.place(x=1248, y=231)

btn101 = Button(frame2came1, text="석대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("석대"), newwindow101()))
btn101.place(x=1203, y=231)

btn102 = Button(frame2came1, text="반여농산물\n시장", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("반여농산물시장"), newwindow102()))
btn102.place(x=1136, y=216)

btn103 = Button(frame2came1, text="금사", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("금사"), newwindow103()))
btn103.place(x=1103, y=231)

btn104 = Button(frame2came1, text="서동", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("서동"), newwindow104()))
btn104.place(x=1052, y=231)

btn105 = Button(frame2came1, text="명장", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("명장"), newwindow105()))
btn105.place(x=1002, y=231)

btn106 = Button(frame2came1, text="충렬사", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("충렬사"), newwindow106()))
btn106.place(x=947, y=231)

btn107 = Button(frame2came1, text="낙민", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("낙민"), newwindow107()))
btn107.place(x=898, y=231)

btn108 = Button(frame2came1, text="수안", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("수안"), newwindow108()))
btn108.place(x=851, y=231)

btn109 = Button(frame2came1, text="태화강", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("태화강"), newwindow109()))
btn109.place(x=1400, y=856)

btn110 = Button(frame2came1, text="개운포", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("개운포"), newwindow110()))
btn110.place(x=1375, y=816)

btn111 = Button(frame2came1, text="덕하", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("덕하"), newwindow111()))
btn111.place(x=1356, y=856)

btn112 = Button(frame2came1, text="망양", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("망양"), newwindow112()))
btn112.place(x=1331, y=816)

btn113 = Button(frame2came1, text="남창", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("남창"), newwindow113()))
btn113.place(x=1307, y=856)

btn114 = Button(frame2came1, text="서생", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("서생"), newwindow114()))
btn114.place(x=1283, y=816)

btn115 = Button(frame2came1, text="월내", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("월내"), newwindow115()))
btn115.place(x=1259, y=856)

btn116 = Button(frame2came1, text="좌천(동해선)", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("좌천(동해선)"), newwindow116()))
btn116.place(x=1246, y=780)

btn117 = Button(frame2came1, text="일광", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("일광"), newwindow117()))
btn117.place(x=1246, y=737)

btn118 = Button(frame2came1, text="기장", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("기장"), newwindow118()))
btn118.place(x=1246, y=694)

btn119 = Button(frame2came1, text="오시리아", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("오시리아"), newwindow119()))
btn119.place(x=1246, y=651)

btn120 = Button(frame2came1, text="송정", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("송정"), newwindow120()))
btn120.place(x=1246, y=608)

btn121 = Button(frame2came1, text="신해운대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("신해운대"), newwindow121()))
btn121.place(x=1246, y=565)

btn122 = Button(frame2came1, text="센텀", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("센텀"), newwindow122()))
btn122.place(x=1225, y=395)

btn123 = Button(frame2came1, text="재송", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("재송"), newwindow123()))
btn123.place(x=1116, y=365)

btn124 = Button(frame2came1, text="부산원동", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부산원동"), newwindow124()))
btn124.place(x=1027, y=365)

btn125 = Button(frame2came1, text="안락", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("안락"), newwindow125()))
btn125.place(x=959, y=365)

btn126 = Button(frame2came1, text="동래(동해선)", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("동래(동해선)"), newwindow126()))
btn126.place(x=861, y=365)

btn127 = Button(frame2came1, text="거제해맞이", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("거제해맞이"), newwindow127()))
btn127.place(x=664, y=614)

btn128 = Button(frame2came1, text="부전", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부전"), newwindow128()))
btn128.place(x=699, y=721)

btn129 = Button(frame2came1, text="가야대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("가야대"), newwindow129()))
btn129.place(x=393, y=78)

btn130 = Button(frame2came1, text="장신대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("장신대"), newwindow130()))
btn130.place(x=360, y=118)

btn131 = Button(frame2came1, text="연지공원", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("연지공원"), newwindow131()))
btn131.place(x=318, y=78)

btn132 = Button(frame2came1, text="박물관", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("박물관"), newwindow132()))
btn132.place(x=286, y=118)

btn133 = Button(frame2came1, text="수로왕릉", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("수로왕릉"), newwindow133()))
btn133.place(x=245, y=78)

btn134 = Button(frame2came1, text="봉황", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("봉황"), newwindow134()))
btn134.place(x=218, y=118)

btn135 = Button(frame2came1, text="부원", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("부원"), newwindow135()))
btn135.place(x=182, y=78)

btn136 = Button(frame2came1, text="김해시청", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("김해시청"), newwindow136()))
btn136.place(x=135, y=118)

btn137 = Button(frame2came1, text="인제대", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("인제대"), newwindow137()))
btn137.place(x=103, y=78)

btn138 = Button(frame2came1, text="김해대학", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("김해대학"), newwindow138()))
btn138.place(x=30, y=94)

btn139 = Button(frame2came1, text="지내", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("지내"), newwindow139()))
btn139.place(x=34, y=173)

btn140 = Button(frame2came1, text="불암", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("불암"), newwindow140()))
btn140.place(x=34, y=251)

btn141 = Button(frame2came1, text="대사", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("대사"), newwindow141()))
btn141.place(x=34, y=328)

btn142 = Button(frame2came1, text="평강", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("평강"), newwindow142()))
btn142.place(x=34, y=406)

btn143 = Button(frame2came1, text="등구", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("등구"), newwindow143()))
btn143.place(x=34, y=627)

btn144 = Button(frame2came1, text="덕두", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("덕두"), newwindow144()))
btn144.place(x=34, y=755)

btn145 = Button(frame2came1, text="공항", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("공항"), newwindow145()))
btn145.place(x=139, y=857)

btn146 = Button(frame2came1, text="서부산유통지구", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("서부산유통지구"), newwindow146()))
btn146.place(x=195, y=857)

btn147 = Button(frame2came1, text="괘법르네시떼", bd=0, highlightthickness=0, bg="white", command=lambda: (btnfunc1("괘법르네시떼"), newwindow147()))
btn147.place(x=290, y=857)

#환승역 이미지
img = Image.open("station\환승역.png")
img_re = img.resize((22,22))
img_fix = ImageTk.PhotoImage(img_re)
traincanvas.create_image(1226, 510, image=img_fix)  #벡스코(시립미술관)
traincanvas.create_image(1055, 510, image=img_fix)  #수영
traincanvas.create_image(807, 251, image=img_fix)   #동래
traincanvas.create_image(807, 385, image=img_fix)   #교대
traincanvas.create_image(807, 510, image=img_fix)   #연산
traincanvas.create_image(807, 837, image=img_fix)   #서면
traincanvas.create_image(739, 510, image=img_fix)   #거제
traincanvas.create_image(611, 510, image=img_fix)   #미남
traincanvas.create_image(453, 837, image=img_fix)   #덕천
traincanvas.create_image(429, 510, image=img_fix)   #사상
traincanvas.create_image(74, 510, image=img_fix)    #대저


subimg1 =Image.open("station/1호선.png")
sub1re = subimg1.resize((280,40))
sub1repix = ImageTk.PhotoImage(sub1re)
sub1 = Label(frame2came1, image=sub1repix)
sub1.place(x=870, y=900)
sub1.bind("<Button-1>", first)

subimg2 = Image.open("station/2호선.png")
sub2re = subimg2.resize((280,40))
sub2repix = ImageTk.PhotoImage(sub2re)
sub2 = Label(frame2came1, image=sub2repix)
sub2.place(x=870, y=950)
sub2.bind("<Button-1>", second)

subimg3 = Image.open("station/3호선.png")
sub3re = subimg3.resize((280,40))
sub3repix = ImageTk.PhotoImage(sub3re)
sub3 = Label(frame2came1, image=sub3repix)
sub3.place(x=870, y=1000)
sub3.bind("<Button-1>", third)

subimg4 = Image.open("station/4호선.png")
sub4re = subimg4.resize((280,40))
sub4repix = ImageTk.PhotoImage(sub4re)
sub4 = Label(frame2came1, image=sub4repix)
sub4.place(x=1160, y=900)
sub4.bind("<Button-1>", four)

subimg5 = Image.open("station/동해선.png")
sub5re = subimg5.resize((280,40))
sub5repix = ImageTk.PhotoImage(sub5re)
sub5 = Label(frame2came1, image=sub5repix)
sub5.place(x=1160, y=950)
sub5.bind("<Button-1>", donghae)

subimg6 = Image.open("station/부산김해.png")
sub6re = subimg6.resize((280,40))
sub6repix = ImageTk.PhotoImage(sub6re)
sub6 = Label(frame2came1, image=sub6repix)
sub6.place(x=1160, y=1000)
sub6.bind("<Button-1>", kimhae)

# img2 = Image.open("station\호선표1.png")
# img_re2 = img2.resize((280,150))
# img_fix2 = ImageTk.PhotoImage(img_re2)
# traincanvas.create_image(1030, 955, image=img_fix2)

# img3 = Image.open("station\호선표2.png")
# img_re3 = img3.resize((280,150))
# img_fix3 = ImageTk.PhotoImage(img_re3)
# traincanvas.create_image(1310, 955, image=img_fix3)

img_1 = Image.open("station/1.png")
img_st1 = img_1.resize((50,30))
img_fix_1 = ImageTk.PhotoImage(img_st1)
traincanvas.create_image(1460, 98, image=img_fix_1)
traincanvas.create_image(30, 1030, image=img_fix_1)

img_2 = Image.open("station/2.png")
img_st2 = img_2.resize((50,30))
img_fix_2 = ImageTk.PhotoImage(img_st2)
traincanvas.create_image(777, 98, image=img_fix_2)
traincanvas.create_image(1460, 510, image=img_fix_2)

img_3 = Image.open("station/3.png")
img_st3 = img_3.resize((50,30))
img_fix_3 = ImageTk.PhotoImage(img_st3)
traincanvas.create_image(995, 560, image=img_fix_3)
traincanvas.create_image(30, 510, image=img_fix_3)

img_4 = Image.open("station/4.png")
img_st4 = img_4.resize((50,30))
img_fix_4 = ImageTk.PhotoImage(img_st4)
traincanvas.create_image(1460, 251, image=img_fix_4)
traincanvas.create_image(611, 560, image=img_fix_4)

img_Donhae = Image.open("station/Donhae.png")
img_stDonhae = img_Donhae.resize((50,30))
img_fix_Donhae = ImageTk.PhotoImage(img_stDonhae)
traincanvas.create_image(1460, 836, image=img_fix_Donhae)
traincanvas.create_image(685, 695, image=img_fix_Donhae)

img_BusanGimhae = Image.open("station/BusanGimhae.png")
img_stBusanGimhae = img_BusanGimhae.resize((50,30))
img_fix_BusanGimhae = ImageTk.PhotoImage(img_stBusanGimhae)
traincanvas.create_image(360, 150, image=img_fix_BusanGimhae)
traincanvas.create_image(360, 785, image=img_fix_BusanGimhae)

time()
win.mainloop()