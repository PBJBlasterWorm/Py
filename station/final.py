import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import copy
import subprocess


win = tk.Tk()
win.geometry('1900x1100+0+0')
win.title("부산 노선도")

def hidden_window():
    game = tk.Toplevel(hiddenbtn)
    game.geometry("250x80+1000+500")
    game.title("숨겨진 게임")
    game.focus_set()
    
    easyfunc = Button(game, text="easy", command=hidden_game1, width=10)
    easyfunc.pack()
    normalfunc = Button(game, text="normal", command=hidden_game2, width=10)
    normalfunc.pack()
    hardfunc = Button(game, text="hard", command=hidden_game3, width=10)
    hardfunc.pack()

def hidden_game1():
    puzzlebubbleeasy = "station/easy.py"    
    subprocess.Popen(["python", puzzlebubbleeasy])
    
def hidden_game2():
    puzzlebubblenormal = "station/normal.py"    
    subprocess.Popen(["python", puzzlebubblenormal])
    
def hidden_game3():
    puzzlebubblehard = "station/hard.py"    
    subprocess.Popen(["python", puzzlebubblehard])

def time():
    settime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timelabel.config(text="현재시각 : " + settime)
    win.after(1000, time)
    
def reset_func():
    input_entry.delete(0, END)
    destination_entry.delete(0, END)
    resultlabel.config(text='')
    # 출발역과 도착역 입력창 초기화
    input_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)

    # 빨간 점 삭제
    traincanvas.delete("red_dot")
    
def entrydata(text):
    if input_entry.get() == "":
        input_entry.delete(0, END)
        input_entry.insert(0, text)
    else:
        destination_entry.delete(0, END)
        destination_entry.insert(0, text)

def back_func():
    station1btn1.place_forget()
    station1btn2.place_forget()
    station1btn3.place_forget()
    station1btn4.place_forget()
    station1btn5.place_forget()
    station1btn6.place_forget()
    station1btn7.place_forget()
    station1btn8.place_forget()
    station1btn9.place_forget()
    station1btn10.place_forget()
    station1btn11.place_forget()
    station1btn12.place_forget()
    station1btn13.place_forget()
    station1btn14.place_forget()
    station1btn15.place_forget()
    station1btn16.place_forget()
    station1btn17.place_forget()
    station1btn18.place_forget()
    station1btn19.place_forget()
    station1btn20.place_forget()
    station1btn21.place_forget()
    station1btn22.place_forget()
    station1btn23.place_forget()
    station1btn24.place_forget()
    station1btn25.place_forget()
    station1btn26.place_forget()
    station1btn27.place_forget()
    station1btn28.place_forget()
    station1btn29.place_forget()
    station1btn30.place_forget()
    station1btn31.place_forget()
    station1btn32.place_forget()
    station1btn33.place_forget()
    station1btn34.place_forget()
    station1btn35.place_forget()
    station1btn36.place_forget()
    station1btn37.place_forget()
    station1btn38.place_forget()
    station1btn39.place_forget()
    station1btn40.place_forget()
    station2btn1.place_forget()
    station2btn2.place_forget()
    station2btn3.place_forget()
    station2btn4.place_forget()
    station2btn5.place_forget()
    station2btn6.place_forget()
    station2btn7.place_forget()
    station2btn8.place_forget()
    station2btn9.place_forget()
    station2btn10.place_forget()
    station2btn11.place_forget()
    station2btn12.place_forget()
    station2btn13.place_forget()
    station2btn14.place_forget()
    station2btn15.place_forget()
    station2btn16.place_forget()
    station2btn17.place_forget()
    station2btn18.place_forget()
    station2btn19.place_forget()
    station2btn20.place_forget()
    station2btn21.place_forget()
    station2btn22.place_forget()
    station2btn23.place_forget()
    station2btn24.place_forget()
    station2btn25.place_forget()
    station2btn26.place_forget()
    station2btn27.place_forget()
    station2btn28.place_forget()
    station2btn29.place_forget()
    station2btn30.place_forget()
    station2btn31.place_forget()
    station2btn32.place_forget()
    station2btn33.place_forget()
    station2btn34.place_forget()
    station2btn35.place_forget()
    station2btn36.place_forget()
    station2btn37.place_forget()
    station2btn38.place_forget()
    station2btn39.place_forget()
    station2btn40.place_forget()
    station2btn41.place_forget()
    station2btn42.place_forget()
    station2btn43.place_forget()
    station3btn1.place_forget()
    station3btn2.place_forget()
    station3btn3.place_forget()
    station3btn4.place_forget()
    station3btn5.place_forget()
    station3btn6.place_forget()
    station3btn7.place_forget()
    station3btn8.place_forget()
    station3btn9.place_forget()
    station3btn10.place_forget()
    station3btn11.place_forget()
    station3btn12.place_forget()
    station3btn13.place_forget()
    station3btn14.place_forget()
    station3btn15.place_forget()
    station3btn16.place_forget()
    station3btn17.place_forget()
    station4btn1.place_forget()
    station4btn2.place_forget()
    station4btn3.place_forget()
    station4btn4.place_forget()
    station4btn5.place_forget()
    station4btn6.place_forget()
    station4btn7.place_forget()
    station4btn8.place_forget()
    station4btn9.place_forget()
    station4btn10.place_forget()
    station4btn11.place_forget()
    station4btn12.place_forget()
    station4btn13.place_forget()
    station4btn14.place_forget()
    station5btn1.place_forget()
    station5btn2.place_forget()
    station5btn3.place_forget()
    station5btn4.place_forget()
    station5btn5.place_forget()
    station5btn6.place_forget()
    station5btn7.place_forget()
    station5btn8.place_forget()
    station5btn9.place_forget()
    station5btn10.place_forget()
    station5btn11.place_forget()
    station5btn12.place_forget()
    station5btn13.place_forget()
    station5btn14.place_forget()
    station5btn15.place_forget()
    station5btn16.place_forget()
    station5btn17.place_forget()
    station5btn18.place_forget()
    station5btn19.place_forget()
    station5btn20.place_forget()
    station5btn21.place_forget()
    station5btn22.place_forget()
    station5btn23.place_forget()
    station6btn1.place_forget()
    station6btn2.place_forget()
    station6btn3.place_forget()
    station6btn4.place_forget()
    station6btn5.place_forget()
    station6btn6.place_forget()
    station6btn7.place_forget()
    station6btn8.place_forget()
    station6btn9.place_forget()
    station6btn10.place_forget()
    station6btn11.place_forget()
    station6btn12.place_forget()
    station6btn13.place_forget()
    station6btn14.place_forget()
    station6btn15.place_forget()
    station6btn16.place_forget()
    station6btn17.place_forget()
    station6btn18.place_forget()
    station6btn19.place_forget()
    station6btn20.place_forget()
    station6btn21.place_forget()
    button1station.place(x=0, y=40)
    button2station.place(x=0, y=200)
    button3station.place(x=0, y=360)
    button4station.place(x=200, y=40)
    button5station.place(x=200, y=200)
    button6station.place(x=200, y=360)
    stationback.place_forget()
    
def firststation():
    button1station.place_forget()
    button2station.place_forget()
    button3station.place_forget()
    button4station.place_forget()
    button5station.place_forget()
    button6station.place_forget()
    station1btn1.place(x=0, y=40)
    station1btn2.place(x=80, y=40)
    station1btn3.place(x=160, y=40)
    station1btn4.place(x=240, y=40)
    station1btn5.place(x=320, y=40)
    station1btn6.place(x=0, y=80)
    station1btn7.place(x=80, y=80)
    station1btn8.place(x=160, y=80)
    station1btn9.place(x=240, y=80)
    station1btn10.place(x=320, y=80)
    station1btn11.place(x=0, y=120)
    station1btn12.place(x=80, y=120)
    station1btn13.place(x=160, y=120)
    station1btn14.place(x=240, y=120)
    station1btn15.place(x=320, y=120)
    station1btn16.place(x=0, y=160)
    station1btn17.place(x=80, y=160)
    station1btn18.place(x=160, y=160)
    station1btn19.place(x=240, y=160)
    station1btn20.place(x=320, y=160)
    station1btn21.place(x=0, y=200)
    station1btn22.place(x=80, y=200)
    station1btn23.place(x=160, y=200)
    station1btn24.place(x=240, y=200)
    station1btn25.place(x=320, y=200)
    station1btn26.place(x=0, y=240)
    station1btn27.place(x=80, y=240)
    station1btn28.place(x=160, y=240)
    station1btn29.place(x=240, y=240)
    station1btn30.place(x=320, y=240)
    station1btn31.place(x=0, y=280)
    station1btn32.place(x=80, y=280)
    station1btn33.place(x=160, y=280)
    station1btn34.place(x=240, y=280)
    station1btn35.place(x=320, y=280)
    station1btn36.place(x=0, y=320)
    station1btn37.place(x=80, y=320)
    station1btn38.place(x=160, y=320)
    station1btn39.place(x=240, y=320)
    station1btn40.place(x=320, y=320)
    stationback.place(x=250, y=400)
    
def secondstation():
    button1station.place_forget()
    button2station.place_forget()
    button3station.place_forget()
    button4station.place_forget()
    button5station.place_forget()
    button6station.place_forget()
    station2btn1.place(x=0, y=40)
    station2btn2.place(x=80, y=40)
    station2btn3.place(x=160, y=40)
    station2btn4.place(x=240, y=40)
    station2btn5.place(x=320, y=40)
    station2btn6.place(x=0, y=80)
    station2btn7.place(x=80, y=80)
    station2btn8.place(x=160, y=80)
    station2btn9.place(x=240, y=80)
    station2btn10.place(x=320, y=80)
    station2btn11.place(x=0, y=120)
    station2btn12.place(x=80, y=120)
    station2btn13.place(x=160, y=120)
    station2btn14.place(x=240, y=120)
    station2btn15.place(x=320, y=120)
    station2btn16.place(x=0, y=160)
    station2btn17.place(x=80, y=160)
    station2btn18.place(x=160, y=160)
    station2btn19.place(x=240, y=160)
    station2btn20.place(x=320, y=160)
    station2btn21.place(x=0, y=200)
    station2btn22.place(x=80, y=200)
    station2btn23.place(x=160, y=200)
    station2btn24.place(x=240, y=200)
    station2btn25.place(x=320, y=200)
    station2btn26.place(x=0, y=240)
    station2btn27.place(x=80, y=240)
    station2btn28.place(x=160, y=240)
    station2btn29.place(x=240, y=240)
    station2btn30.place(x=320, y=240)
    station2btn31.place(x=0, y=280)
    station2btn32.place(x=80, y=280)
    station2btn33.place(x=160, y=280)
    station2btn34.place(x=240, y=280)
    station2btn35.place(x=320, y=280)
    station2btn36.place(x=0, y=320)
    station2btn37.place(x=80, y=320)
    station2btn38.place(x=160, y=320)
    station2btn39.place(x=240, y=320)
    station2btn40.place(x=320, y=320)
    station2btn41.place(x=0, y=360)
    station2btn42.place(x=80, y=360)
    station2btn43.place(x=160, y=360)
    stationback.place(x=250, y=400)
    
def thirdstation():
    button1station.place_forget()
    button2station.place_forget()
    button3station.place_forget()
    button4station.place_forget()
    button5station.place_forget()
    button6station.place_forget()
    station3btn1.place(x=0, y=40)
    station3btn2.place(x=80, y=40)
    station3btn3.place(x=160, y=40)
    station3btn4.place(x=240, y=40)
    station3btn5.place(x=320, y=40)
    station3btn6.place(x=0, y=80)
    station3btn7.place(x=80, y=80)
    station3btn8.place(x=160, y=80)
    station3btn9.place(x=240, y=80)
    station3btn10.place(x=320, y=80)
    station3btn11.place(x=0, y=120)
    station3btn12.place(x=80, y=120)
    station3btn13.place(x=160, y=120)
    station3btn14.place(x=240, y=120)
    station3btn15.place(x=320, y=120)
    station3btn16.place(x=0, y=160)
    station3btn17.place(x=80, y=160)
    stationback.place(x=250, y=400)
    
def fourstation():
    button1station.place_forget()
    button2station.place_forget()
    button3station.place_forget()
    button4station.place_forget()
    button5station.place_forget()
    button6station.place_forget()
    station4btn1.place(x=0, y=40)
    station4btn2.place(x=80, y=40)
    station4btn3.place(x=160, y=40)
    station4btn4.place(x=240, y=40)
    station4btn5.place(x=320, y=40)
    station4btn6.place(x=0, y=80)
    station4btn7.place(x=80, y=80)
    station4btn8.place(x=160, y=80)
    station4btn9.place(x=240, y=80)
    station4btn10.place(x=320, y=80)
    station4btn11.place(x=0, y=120)
    station4btn12.place(x=80, y=120)
    station4btn13.place(x=160, y=120)
    station4btn14.place(x=240, y=120)
    stationback.place(x=250, y=400)
    
def donghaestation():
    button1station.place_forget()
    button2station.place_forget()
    button3station.place_forget()
    button4station.place_forget()
    button5station.place_forget()
    button6station.place_forget()
    station5btn1.place(x=0, y=40)
    station5btn2.place(x=80, y=40)
    station5btn3.place(x=160, y=40)
    station5btn4.place(x=240, y=40)
    station5btn5.place(x=320, y=40)
    station5btn6.place(x=0, y=80)
    station5btn7.place(x=80, y=80)
    station5btn8.place(x=160, y=80)
    station5btn9.place(x=240, y=80)
    station5btn10.place(x=320, y=80)
    station5btn11.place(x=0, y=120)
    station5btn12.place(x=80, y=120)
    station5btn13.place(x=160, y=120)
    station5btn14.place(x=240, y=120)
    station5btn15.place(x=320, y=120)
    station5btn16.place(x=0, y=160)
    station5btn17.place(x=80, y=160)
    station5btn18.place(x=160, y=160)
    station5btn19.place(x=240, y=160)
    station5btn20.place(x=320, y=160)
    station5btn21.place(x=0, y=200)
    station5btn22.place(x=80, y=200)
    station5btn23.place(x=160, y=200)
    stationback.place(x=250, y=400)
    
def kimhaestation():
    button1station.place_forget()
    button2station.place_forget()
    button3station.place_forget()
    button4station.place_forget()
    button5station.place_forget()
    button6station.place_forget()
    station6btn1.place(x=0, y=40)
    station6btn2.place(x=80, y=40)
    station6btn3.place(x=160, y=40)
    station6btn4.place(x=240, y=40)
    station6btn5.place(x=320, y=40)
    station6btn6.place(x=0, y=80)
    station6btn7.place(x=80, y=80)
    station6btn8.place(x=160, y=80)
    station6btn9.place(x=240, y=80)
    station6btn10.place(x=320, y=80)
    station6btn11.place(x=0, y=120)
    station6btn12.place(x=80, y=120)
    station6btn13.place(x=160, y=120)
    station6btn14.place(x=240, y=120)
    station6btn15.place(x=320, y=120)
    station6btn16.place(x=0, y=160)
    station6btn17.place(x=80, y=160)
    station6btn18.place(x=160, y=160)
    station6btn19.place(x=240, y=160)
    station6btn20.place(x=320, y=160)
    station6btn21.place(x=0, y=200)
    stationback.place(x=250, y=400)
    
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
    money_card = 1450   # 카드 기본 요금 초기화
    money_cash = 1550   # 현금 기본 요금 초기화
    start = input_entry.get()       # 입력된 출발역을 가져온다
    end = destination_entry.get()   # 입력된 도착역을 가져온다
    routing = {}    # 모든 역을 넣을 리스트 초기화
    for place in 부산지하철.keys(): # 모든 역의 키값을 위 초기화한 리스트에 저장
        routing[place] = {'shortestTime': 0, 'shortestDist': 0, 'route': [], 'visited': 0}

    def visitPlace(visit):
        routing[visit]['visited'] = 1
        for toGo, info in 부산지하철[visit].items():    # 모든 역의 거리와 시간의 키값을 각각 변수에 저장
            time_toGo = routing[visit]['shortestTime'] + info['거리']
            distance_toGo = routing[visit]['shortestDist'] + info['시간']
            if (routing[toGo]['shortestDist'] >= distance_toGo) or not routing[toGo]['route']:
                routing[toGo]['shortestDist'] = distance_toGo
                routing[toGo]['shortestTime'] = time_toGo
                routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
                routing[toGo]['route'].append(visit)

    visitPlace(start)

    while 1:    # 출발역과 도착역과 사이의 모든 경우의 수를 구하는 무한 반복문
        minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
        toVisit = ''
        for name, search in routing.items():    # 출발역과 도착역 사이의 최소 시간을 구한다
            if 0 < search['shortestDist'] <= minDist and not search['visited']:
                minDist = search['shortestDist']
                toVisit = name

        if toVisit == '':   # 모든 경우의 수를 구하고 더이상 경우의 수가 없다면 반복문 탈출
            break
        
        visitPlace(toVisit)
    
    routing[end]['route'].append(end)
    
    route_list = routing[end]['route']  # 최소 시간의 출발역과 도착역 사이 역의 리스트를 변수 선언
    b = routing[end]['shortestDist']    # 최소 시간의 출발역과 도착역 사이의 시간을 변수 선언
    change_cnt = 0    # 환승 수 변수 0으로 초기화
    for x in range(76): # 환승을 검사하는 반복문
        cnt = 0
        for z in route_list:    # route_list와 change_line을 비교해 change_line이 route_lisㅅ에 속해있다면 환승
            if z in change_line[x]:
                cnt += 1
                if cnt % 3 == 0:
                    b = routing[end]['shortestDist'] + 10   # 환승할 경우 시간을 +10
                    change_cnt += 0.5                       # 환승할 경우 환승횟수를 +1

    km = routing[end]['shortestTime']
    
    if km >= 10:        # 거리의 길이가 10Km이상일 경우 요금추가
        money_card += 200
        money_cash += 200
        
    for x in range(8):  # 부산김해선을 들어오거나 빠져나갈시 요금 추가
        cnt = 0
        for z in route_list:
            if z in change_line_500[x]:
                cnt += 1
                if cnt % 3 == 0:
                    money_card += 250
                    money_cash += 700
    
    route_str = ' → '.join(route_list)  # 출박역과 도착역 사이의 역 리스트의 구분자를 →로 변경
    
    a = '[ ' + start + " → " + end + " ]\n\n" + str(route_str) + "\n\n소요 시간 : " + str(b) + "분\n\n거리 : " + str(round(km, 2)) + "km\n\n요금 : 카드 - " + str(money_card) + "원 / 현금 - " + str(money_cash) + "원\n\n환승횟수 : " + str(int(change_cnt)) + '번'
    resultlabel.config(text = a)
    # 결과 값을 resultlabel에 출력

def MoveTrain():
    global train_x
    train_label.place(x=train_x, y=train_y)
    train_x += train_speed  
    
#이미지가 1290을 넘어갔을 시 20의로 x축의 값을 초기화
    if train_x > 1180:
        train_x = 20
        
    frame2came1.after(100, MoveTrain)

my_font1 = '감탄로드바탕체 Bold'
my_font2 = '감탄로드바탕체 Regular'

frame1came1 = tk.Frame(win, height=1100 , width=390 ,background='#F8E8EE')
frame1came1.grid(row=0, column=0,sticky="nwse")   
frame2came1 = tk.Frame(win, height=1100, width=1500, background='#F8E8EE')
frame2came1.grid(row=0, column=1)

Lframe_top = tk.Frame(frame1came1, width=400, height=150, background='#F8E8EE')
Lframe_top.pack(anchor='nw', expand=True, fill='both')

button1station = Button(Lframe_top, relief="solid", text="1호선", width=10, height=5, command=firststation, font=(my_font1,20), bg='#FFA500', activebackground='#FFA500')
button1station.place(x=0, y=40)

stationback = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="뒤로 가기", width=20, height=4, command=back_func)
stationback.place_forget()
station1btn1 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="노포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("노포")))
station1btn1.place_forget()
station1btn2 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="범어사", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("범어사")))
station1btn2.place_forget()
station1btn3 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="남산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("남산")))
station1btn3.place_forget()
station1btn4 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="두실", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("두실")))
station1btn4.place_forget()
station1btn5 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="선릉", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("선릉")))
station1btn5.place_forget()
station1btn6 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="장전", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("장전")))
station1btn6.place_forget()
station1btn7 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부산대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부산대")))
station1btn7.place_forget()
station1btn8 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="온천장", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("온천장")))
station1btn8.place_forget()
station1btn9 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="명륜", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("명륜")))
station1btn9.place_forget()
station1btn10 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동래", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동래")))
station1btn10.place_forget()
station1btn11 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="교대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("교대")))
station1btn11.place_forget()
station1btn12 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="연산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("연산")))
station1btn12.place_forget()
station1btn13 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="시청", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("시청")))
station1btn13.place_forget()
station1btn14 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="양정", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("양정")))
station1btn14.place_forget()
station1btn15 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부전", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부전")))
station1btn15.place_forget()
station1btn16 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="서면", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("서면")))
station1btn16.place_forget()
station1btn17 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="범내골", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("범내골")))
station1btn17.place_forget()
station1btn18 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="범일", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("범일")))
station1btn18.place_forget()
station1btn19 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="좌천(1호선)", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("좌천(1호선)")))
station1btn19.place_forget()
station1btn20 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부산진", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부산진")))
station1btn20.place_forget()
station1btn21 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="초량", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("초량")))
station1btn21.place_forget()
station1btn22 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부산역", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부산역")))
station1btn22.place_forget()
station1btn23 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="중앙", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("중앙")))
station1btn23.place_forget()
station1btn24 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="남포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("남포")))
station1btn24.place_forget()
station1btn25 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="자갈치", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("자갈치")))
station1btn25.place_forget()
station1btn26 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="토성", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("토성")))
station1btn26.place_forget()
station1btn27 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동대신", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동대신")))
station1btn27.place_forget()
station1btn28 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="서대신", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("서대신")))
station1btn28.place_forget()
station1btn29 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="대티", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("대티")))
station1btn29.place_forget()
station1btn30 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="과정", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("과정")))
station1btn30.place_forget()
station1btn31 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="사하", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("사하")))
station1btn31.place_forget()
station1btn32 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="당리", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("당리")))
station1btn32.place_forget()
station1btn33 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="하단", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("하단")))
station1btn33.place_forget()
station1btn34 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="신평", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("신평")))
station1btn34.place_forget()
station1btn35 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동매", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동매")))
station1btn35.place_forget()
station1btn36 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="장림", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("장림")))
station1btn36.place_forget()
station1btn37 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="신장림", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("신장림")))
station1btn37.place_forget()
station1btn38 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="낫개", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("낫개")))
station1btn38.place_forget()
station1btn39 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="다대포항", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("다대포항")))
station1btn39.place_forget()
station1btn40 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="다대포\n해수욕장", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("다대포해수욕장")))
station1btn40.place_forget()

button2station = Button(Lframe_top, relief="solid", text="2호선", width=10, height=5, command=secondstation, font=(my_font1,20), bg='#90EE90', activebackground='#90EE90')
button2station.place(x=0, y=200)

station2btn1 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="양산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("양산")))
station2btn1.place_forget()
station2btn2 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="남양산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("남양산")))
station2btn2.place_forget()
station2btn3 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부산대\n중앙캠퍼스", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부산대중앙캠퍼스")))
station2btn3.place_forget()
station2btn4 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="중산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("중산")))
station2btn4.place_forget()
station2btn5 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="호포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("호포")))
station2btn5.place_forget()
station2btn6 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="금곡", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("금곡")))
station2btn6.place_forget()
station2btn7 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동원", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동원")))
station2btn7.place_forget()
station2btn8 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="율리", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("율리")))
station2btn8.place_forget()
station2btn9 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="화명", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("화명")))
station2btn9.place_forget()
station2btn10 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="수정", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("수정")))
station2btn10.place_forget()
station2btn11 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="덕천", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("덕천")))
station2btn11.place_forget()
station2btn12 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="구명", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("구명")))
station2btn12.place_forget()
station2btn13 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="구남", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("구남")))
station2btn13.place_forget()
station2btn14 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="모라", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("모라")))
station2btn14.place_forget()
station2btn15 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="모덕", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("모덕")))
station2btn15.place_forget()
station2btn16 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="덕포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("덕포")))
station2btn16.place_forget()
station2btn17 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="사상", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("사상")))
station2btn17.place_forget()
station2btn18 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="감전", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("감전")))
station2btn18.place_forget()
station2btn19 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="주례", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("주례")))
station2btn19.place_forget()
station2btn20 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="냉정", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("냉정")))
station2btn20.place_forget()
station2btn21 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="개금", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("개금")))
station2btn21.place_forget()
station2btn22 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동의대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동의대")))
station2btn22.place_forget()
station2btn23 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="가야", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("가야")))
station2btn23.place_forget()
station2btn24 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부암", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부암")))
station2btn24.place_forget()
station2btn25 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="서면", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("서면")))
station2btn25.place_forget()
station2btn26 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="전포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("전포")))
station2btn26.place_forget()
station2btn27 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="국제금융센터\n·부산은행", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("국제금융센터·부산은행")))
station2btn27.place_forget()
station2btn28 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="문현", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("문현")))
station2btn28.place_forget()
station2btn29 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="지게골", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("지게골")))
station2btn29.place_forget()
station2btn30 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="못골", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("못골")))
station2btn30.place_forget()
station2btn31 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="대연", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("대연")))
station2btn31.place_forget()
station2btn32 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="경성대·부경대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("경성대·부경대")))
station2btn32.place_forget()
station2btn33 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="남천", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("남천")))
station2btn33.place_forget()
station2btn34 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="금련산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("금련산")))
station2btn34.place_forget()
station2btn35 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="광안", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("광안")))
station2btn35.place_forget()
station2btn36 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="수영", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("수영")))
station2btn36.place_forget()
station2btn37 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="민락", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("민락")))
station2btn37.place_forget()
station2btn38 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="센텀시티", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("센텀시티")))
station2btn38.place_forget()
station2btn39 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="벡스코\n(시립박물관)", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("벡스코(시립박물관)")))
station2btn39.place_forget()
station2btn40 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동백", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동백")))
station2btn40.place_forget()
station2btn41 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="해운대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("해운대")))
station2btn41.place_forget()
station2btn42 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="중동", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("중동")))
station2btn42.place_forget()
station2btn43 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="장산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("장산")))
station2btn43.place_forget()

button3station = Button(Lframe_top, relief="solid", text="3호선", width=10, height=5, command=thirdstation, font=(my_font1,20), bg='#FFD700', activebackground='#FFD700')
button3station.place(x=0, y=360)

station3btn1 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="대저", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("대저")))
station3btn1.place_forget()
station3btn2 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="체육공원", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("체육공원")))
station3btn2.place_forget()
station3btn3 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="강서구청", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("강서구청")))
station3btn3.place_forget()
station3btn4 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="구포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("구포")))
station3btn4.place_forget()
station3btn5 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="덕천", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("덕천")))
station3btn5.place_forget()
station3btn6 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="숙동", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("숙동")))
station3btn6.place_forget()
station3btn7 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="남산정", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("남산정")))
station3btn7.place_forget()
station3btn8 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="만덕", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("만덕")))
station3btn8.place_forget()
station3btn9 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="미남", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("미남")))
station3btn9.place_forget()
station3btn10 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="사직", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("사직")))
station3btn10.place_forget()
station3btn11 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="종합운동장", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("종합운동장")))
station3btn11.place_forget()
station3btn12 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="거제", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("거제")))
station3btn12.place_forget()
station3btn13 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="연산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("연산")))
station3btn13.place_forget()
station3btn14 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="물만골", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("물만골")))
station3btn14.place_forget()
station3btn15 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="배산", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("배산")))
station3btn15.place_forget()
station3btn16 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="망미", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("망미")))
station3btn16.place_forget()
station3btn17 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="수영", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("수영")))
station3btn17.place_forget()

button4station = Button(Lframe_top, relief="solid", text="4호선", width=10, height=5, command=fourstation, font=(my_font1,20), bg='#87CEEB', activebackground='#87CEEB')
button4station.place(x=200, y=40)

station4btn1 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="안평", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("안평")))
station4btn1.place_forget()
station4btn2 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="고촌", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("고촌")))
station4btn2.place_forget()
station4btn3 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="윗반송", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("윗반송")))
station4btn3.place_forget()
station4btn4 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="영산대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("영산대")))
station4btn4.place_forget()
station4btn5 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="석대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("석대")))
station4btn5.place_forget()
station4btn6 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="반여농산물\n시장", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("반여농산물시장")))
station4btn6.place_forget()
station4btn7 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="금사", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("금사")))
station4btn7.place_forget()
station4btn8 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="서동", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("서동")))
station4btn8.place_forget()
station4btn9 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="명장", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("명장")))
station4btn9.place_forget()
station4btn10 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="충렬사", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("충렬사")))
station4btn10.place_forget()
station4btn11 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="낙민", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("낙민")))
station4btn11.place_forget()
station4btn12 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="수안", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("수안")))
station4btn12.place_forget()
station4btn13 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동래", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동래")))
station4btn13.place_forget()
station4btn14 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="미남", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("미남")))
station4btn14.place_forget()

button5station = Button(Lframe_top, relief="solid", text="동해선", width=10, height=5, command=donghaestation, font=(my_font1,20), bg='#005BAC', activebackground='#005BAC')
button5station.place(x=200, y=200)

station5btn1 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="태화강", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("태화강")))
station5btn1.place_forget()
station5btn2 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="개운포", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("개운포")))
station5btn2.place_forget()
station5btn3 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="덕하", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("덕하")))
station5btn3.place_forget()
station5btn4 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="망양", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("망양")))
station5btn4.place_forget()
station5btn5 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="남창", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("남창")))
station5btn5.place_forget()
station5btn6 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="서생", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("서생")))
station5btn6.place_forget()
station5btn7 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="월내", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("월내")))
station5btn7.place_forget()
station5btn8 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="좌천(동해선)", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("좌천(동해선)")))
station5btn8.place_forget()
station5btn9 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="일광", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("일광")))
station5btn9.place_forget()
station5btn10 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="기장", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("기장")))
station5btn10.place_forget()
station5btn11 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="오시리아", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("오시리아")))
station5btn11.place_forget()
station5btn12 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="송정", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("송정")))
station5btn12.place_forget()
station5btn13 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="신해운대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("신해운대")))
station5btn13.place_forget()
station5btn14 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="벡스코\n(시립미술관)", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("벡스코(시립미술관)")))
station5btn14.place_forget()
station5btn15 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="센텀", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("센텀")))
station5btn15.place_forget()
station5btn16 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="재송", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("재송")))
station5btn16.place_forget()
station5btn17 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부산원동", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부산원동")))
station5btn17.place_forget()
station5btn18 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="안락", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("안락")))
station5btn18.place_forget()
station5btn19 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="동래(동해선)", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("동래(동해선)")))
station5btn19.place_forget()
station5btn20 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="교대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("교대")))
station5btn20.place_forget()
station5btn21 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="거제", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("거제")))
station5btn21.place_forget()
station5btn22 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="거제해맞이", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("거제해맞이")))
station5btn22.place_forget()
station5btn23 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부전", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부전")))
station5btn23.place_forget()

button6station = Button(Lframe_top, relief="solid", text="부산김해선", width=10, height=5, command=kimhaestation, font=(my_font1,20), bg='#9370DB', activebackground='#9370DB')
button6station.place(x=200, y=360)

station6btn1 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="가야대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("가야대")))
station6btn1.place_forget()
station6btn2 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="장신대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("장신대")))
station6btn2.place_forget()
station6btn3 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="연지공원", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("연지공원")))
station6btn3.place_forget()
station6btn4 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="박물관", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("박물관")))
station6btn4.place_forget()
station6btn5 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="수로왕릉", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("수로왕릉")))
station6btn5.place_forget()
station6btn6 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="봉황", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("봉황")))
station6btn6.place_forget()
station6btn7 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="부원", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("부원")))
station6btn7.place_forget()
station6btn8 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="김해시청", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("김해시청")))
station6btn8.place_forget()
station6btn9 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="인제대", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("인제대")))
station6btn9.place_forget()
station6btn10 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="김해대학", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("김해대학")))
station6btn10.place_forget()
station6btn11 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="지내", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("지내")))
station6btn11.place_forget()
station6btn12 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="불암", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("불암")))
station6btn12.place_forget()
station6btn13 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="대사", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("대사")))
station6btn13.place_forget()
station6btn14 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="평강", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("평강")))
station6btn14.place_forget()
station6btn15 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="대저", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("대저")))
station6btn15.place_forget()
station6btn16 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="등구", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("등구")))
station6btn16.place_forget()
station6btn17 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="덕두", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("덕두")))
station6btn17.place_forget()
station6btn18 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="공항", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("공항")))
station6btn18.place_forget()
station6btn19 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="서부산\n유통지구", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("서부산유통지구")))
station6btn19.place_forget()
station6btn20 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="괘법\n르네시떼", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("괘법르네시떼")))
station6btn20.place_forget()
station6btn21 = Button(Lframe_top, relief="flat", overrelief='solid', bg='#F8E8EE', activebackground='#FDCEDF', text="사상", width=8, height=2, font=(my_font2,10), command=lambda:entrydata(("사상")))
station6btn21.place_forget()


Lframe_bottom = tk.Frame(frame1came1, width=390, height=275, background='#F8E8EE')
Lframe_bottom.pack(anchor='se',expand=True,fill='both')


traincanvas = tk.Canvas(frame2came1,width=1485,height=1080,relief='solid',bd=0,background='white')
traincanvas.place(x=5,y=10)   #노선도 그리는 칸

# 초기 지하철 열차 위치 및 이동 속도 설정
train_x = 0
train_y = 30
train_speed = 8

# 지하철 열차 이미지를 화면에 표시
img_train = Image.open("station/train.png")
img_sttrain = img_train.resize((300,30))
train_photo = ImageTk.PhotoImage(img_sttrain)
train_label = tk.Label(frame2came1, image=train_photo,bg='white')
train_label.place(x=train_x, y=train_y)
# 재귀함수로 열차를 움직임 

MoveTrain()

부산지하철 = {  # 역들의 인접역의 시간과 거리값을 저장
    # 1호선
    '노포': {
        '범어사': {'시간': 1, '거리': 1.2},
        },
    '범어사': {
        '노포': {'시간': 1, '거리': 1.2},
        '남산': {'시간': 2, '거리': 0.9},
        },
    '남산': {
        '범어사': {'시간': 2, '거리': 0.9},
        '두실': {'시간': 1, '거리': 1},
        },
    '두실': {
        '남산': {'시간': 1, '거리': 1},
        '구서': {'시간': 2, '거리': 1},
        },
    '구서': {
        '두실': {'시간': 2, '거리': 1},
        '장전': {'시간': 2, '거리': 1.1}
        },
    '장전': {
        '구서': {'시간': 2, '거리': 1.1},
        '부산대': {'시간': 2, '거리': 1}
        },
    '부산대': {
        '장전': {'시간': 2, '거리': 1},
        '온천장': {'시간': 2, '거리': 1.1}
        },
    '온천장': {
        '부산대': {'시간': 2, '거리': 1.1},
        '명륜': {'시간': 2, '거리': 1}
        },
    '명륜': {
        '온천장': {'시간': 2, '거리': 1},
        '동래': {'시간': 2, '거리': 0.8}
        },
    '동래': {
        '명륜': {'시간': 2, '거리': 0.8},
        '교대': {'시간': 2, '거리': 1.2},
        '미남': {'시간': 3, '거리': 1},
        '수안': {'시간': 2, '거리': 0.7}
        },
    '교대': {
        '동래': {'시간': 2, '거리': 1.2},
        '연산': {'시간': 2, '거리': 1},
        '거제': {'시간': 2, '거리': 0.7},
        '동래(동해선)': {'시간': 3, '거리': 1.2}
        },
    '연산': {
        '교대': {'시간': 2, '거리': 1},
        '시청': {'시간': 1, '거리': 0.9},
        '거제': {'시간': 2, '거리': 0.7},
        '물만골': {'시간': 2, '거리': 1.1}
        },
    '시청': {
        '연산': {'시간': 1, '거리': 0.9},
        '양정': {'시간': 2, '거리': 0.8}
        },
    '양정': {
        '시청': {'시간': 2, '거리': 0.8},
        '부전': {'시간': 2, '거리': 1.4}
        },
    '부전': {
        '양정': {'시간': 2, '거리': 1.4},
        '서면': {'시간': 2, '거리': 0.6},
        '거제해맞이': {'시간': 3, '거리': 2.3}
        },
    '서면': {
        '부전': {'시간': 2, '거리': 0.6},
        '범내골': {'시간': 2, '거리': 1.2},
        '부암': {'시간': 2, '거리': 0.8},
        '전포': {'시간': 3, '거리': 1.1}
        },
    '범내골': {
        '서면': {'시간': 2, '거리': 1.2},
        '범일': {'시간': 2, '거리': 0.8}
        },
    '범일': {
        '범내골': {'시간': 2, '거리': 0.8},
        '좌천(1호선)': {'시간': 2, '거리': 0.9}
        },
    '좌천(1호선)': {
        '범일': {'시간': 2, '거리': 0.9},
        '부산진': {'시간': 2, '거리': 1}
        },
    '부산진': {
        '좌천(1호선)': {'시간': 2, '거리': 1},
        '초량': {'시간': 2, '거리': 0.8}
        },
    '초량': {
        '부산진': {'시간': 2, '거리': 0.8},
        '부산역': {'시간': 1, '거리': 0.8}
        },
    '부산역': {
        '초량': {'시간': 1, '거리': 0.8},
        '중앙': {'시간': 2, '거리': 1.1}
        },
    '중앙': {
        '부산역': {'시간': 2, '거리': 1.1},
        '남포': {'시간': 2, '거리': 0.9}
        },
    '남포': {
        '중앙': {'시간': 2, '거리': 0.9},
        '자갈치': {'시간': 1, '거리': 0.7}
        },
    '자갈치': {
        '남포': {'시간': 1, '거리': 0.7},
        '토성': {'시간': 3, '거리': 1}
        },
    '토성': {
        '자갈치': {'시간': 3, '거리': 1},
        '동대신': {'시간': 3, '거리': 1.2}
        },
    '동대신': {
        '토성': {'시간': 3, '거리': 1.2},
        '서대신': {'시간': 3, '거리': 0.7}
        },
    '서대신': {
        '동대신': {'시간': 3, '거리': 0.7},
        '대티': {'시간': 2, '거리': 1.4}
        },
    '대티': {
        '서대신': {'시간': 2, '거리': 1.4},
        '괴정': {'시간': 1, '거리': 0.8}
        },
    '괴정': {
        '대티': {'시간': 1, '거리': 0.8},
        '사하': {'시간': 2, '거리': 0.9}
        },
    '사하': {
        '괴정': {'시간': 2, '거리': 0.9},
        '당리': {'시간': 1, '거리': 0.9}
        },
    '당리': {
        '사하': {'시간': 1, '거리': 0.9},
        '하단': {'시간': 2, '거리': 0.8}
        },
    '하단': {
        '당리': {'시간': 2, '거리': 0.8},
        '신평': {'시간': 3, '거리': 1.6}
        },
    '신평': {
        '하단': {'시간': 3, '거리': 1.6},
        '동매': {'시간': 3, '거리': 1.7}
        },
    '동매': {
        '신평': {'시간': 3, '거리': 1.7},
        '장림': {'시간': 2, '거리': 1.2}
        },
    '장림': {
        '동매': {'시간': 2, '거리': 1.2},
        '신장림': {'시간': 2, '거리': 0.8}
        },
    '신장림': {
        '장림': {'시간': 2, '거리': 0.8},
        '낫개': {'시간': 2, '거리': 1.1}
        },
    '낫개': {
        '신장림': {'시간': 2, '거리': 1.1},
        '다대포항': {'시간': 2, '거리': 1.2}
        },
    '다대포항': {
        '낫개': {'시간': 2, '거리': 1.2},
        '다대포해수욕장': {'시간': 3, '거리': 1.4}
        },
    '다대포해수욕장': {
        '다대포항': {'시간': 3, '거리': 1.4}
        },
    # 2호선
    '양산': {
        '남양산': {'시간': 2, '거리': 1.6}
        },
    '남양산': {
        '양산': {'시간': 2, '거리': 1.6},
        '부산대양산캠퍼스': {'시간': 2, '거리': 1.1}
        },
    '부산대양산캠퍼스': {
        '남양산':{'시간': 2, '거리': 1.1},
        '증산': {'시간': 2, '거리': 1}
        },
    '증산': {
        '부산대양산캠퍼스': {'시간': 2, '거리': 1},
        '호포': {'시간': 4, '거리': 3.5}
        },
    '호포': {
        '증산': {'시간': 4, '거리': 3.5},
        '금곡': {'시간': 3, '거리': 1.5}
        },
    '금곡': {
        '호포': {'시간': 3, '거리': 1.5},
        '동원': {'시간': 2, '거리': 1}
        },
    '동원': {
        '금곡': {'시간': 2, '거리': 1},
        '율리': {'시간': 2, '거리': 1.5}
        },
    '율리': {
        '동원': {'시간': 2, '거리': 1.5},
        '화명': {'시간': 2, '거리': 1.2}
        },
    '화명': {
        '율리': {'시간': 2, '거리': 1.2},
        '수정': {'시간': 2, '거리': 1.5}
        },
    '수정': {
        '화명': {'시간': 2, '거리': 1.5},
        '덕천': {'시간': 3, '거리': 1.5}
        },
    '덕천': {
        '수정': {'시간': 3, '거리': 1.5},
        '구명': {'시간': 2, '거리': 1.2},
        '구포': {'시간': 3, '거리': 1.1},
        '숙등': {'시간': 2, '거리': 0.7}
        },
    '구명': {
        '덕천': {'시간': 2, '거리': 1.2},
        '구남': {'시간': 2, '거리': 0.7}
        },
    '구남': {
        '구명': {'시간': 2, '거리': 0.7},
        '모라': {'시간': 2, '거리': 1.1}
        },
    '모라': {
        '구남': {'시간': 2, '거리': 1.1},
        '모덕': {'시간': 1, '거리': 1}
        },
    '모덕': {
        '모라': {'시간': 1, '거리': 1},
        '덕포': {'시간': 1, '거리': 0.8}
        },
    '덕포': {
        '모덕': {'시간': 1, '거리': 0.8},
        '사상': {'시간': 3, '거리': 1.2}
        },
    '사상': {
        '덕포': {'시간': 3, '거리': 1.2},
        '감전': {'시간': 2, '거리': 1.1},
        '괘법르네시떼': {'시간': 1, '거리': 0.8}
        },
    '감전': {
        '사상': {'시간': 2, '거리': 1.1},
        '주례': {'시간': 2, '거리': 1.2}
        },
    '주례': {
        '감전': {'시간': 2, '거리': 1.2},
        '냉정': {'시간': 2, '거리': 0.9}
        },
    '냉정': {
        '주례': {'시간': 2, '거리': 0.9},
        '개금': {'시간': 2, '거리': 0.8}
        },
    '개금': {
        '냉정': {'시간': 2, '거리': 0.8},
        '동의대': {'시간': 1, '거리': 1.1}
        },
    '동의대': {
        '개금': {'시간': 1, '거리': 1.1},
        '가야': {'시간': 2, '거리': 0.9}
        },
    '가야': {
        '동의대': {'시간': 2, '거리': 0.9},
        '부암': {'시간': 2, '거리': 0.7}
        },
    '부암': {
        '가야': {'시간': 2, '거리': 0.7},
        '서면': {'시간': 2, '거리': 0.8}
        },
    '서면': {
        '부전': {'시간': 2, '거리': 0.6},
        '범내골': {'시간': 2, '거리': 1.2},
        '부암': {'시간': 2, '거리': 0.8},
        '전포': {'시간': 3, '거리': 1.1}
        },
    '전포': {
        '서면': {'시간': 3, '거리': 1.1},
        '국제금융센터·부산은행': {'시간': 2, '거리': 0.8}
        },
    '국제금융센터·부산은행': {
        '전포': {'시간': 2, '거리': 0.8},
        '문현': {'시간': 2, '거리': 0.8}
        },
    '문현': {
        '국제금융센터·부산은행': {'시간': 2, '거리': 0.8},
        '지게골': {'시간': 1, '거리': 0.8}
        },
    '지게골': {
        '문현': {'시간': 1, '거리': 0.8},
        '못골': {'시간': 2, '거리': 0.9}
        },
    '못골': {
        '지게골': {'시간': 2, '거리': 0.9},
        '대연': {'시간': 2, '거리': 0.7}
        },
    '대연': {
        '못골': {'시간': 2, '거리': 0.7},
        '경성대·부경대': {'시간': 2, '거리': 0.9}
        },
    '경성대·부경대': {
        '대연': {'시간': 2, '거리': 0.9},
        '남천': {'시간': 2, '거리': 0.8}
        },
    '남천': {
        '경성대·부경대': {'시간': 2, '거리': 0.8},
        '금련산': {'시간': 2, '거리': 0.9}
        },
    '금련산': {
        '남천': {'시간': 2, '거리': 0.9},
        '광안': {'시간': 2, '거리': 0.9}
        },
    '광안': {
        '금련산': {'시간': 2, '거리': 0.9},
        '수영': {'시간': 2, '거리': 0.9}
        },
    '수영': {
        '광안': {'시간': 2, '거리': 0.9},
        '민락': {'시간': 2, '거리': 0.9},
        '망미': {'시간': 2, '거리': 1}
        },
    '민락': {
        '수영': {'시간': 2, '거리': 0.9},
        '센텀시티': {'시간': 2, '거리': 1}
        },
    '센텀시티': {
        '민락': {'시간': 2, '거리': 1},
        '벡스코(시립미술관)': {'시간': 2, '거리': 0.8}
        },
    '벡스코(시립미술관)': {
        '센텀시티': {'시간': 2, '거리': 0.8},
        '동백': {'시간': 2, '거리': 1.1},
        '센텀': {'시간': 2, '거리': 1.4},
        '신해운대': {'시간': 5, '거리': 4.5}
        },
    '동백': {
        '벡스코(시립미술관)': {'시간': 2, '거리': 1.1},
        '해운대': {'시간': 2, '거리': 0.9}
        },
    '해운대': {
        '동백': {'시간': 2, '거리': 1.2},
        '중동': {'시간': 2, '거리': 0.9}
        },
    '중동': {
        '해운대': {'시간': 2, '거리': 0.9},
        '장산': {'시간': 2, '거리': 0.9}
        },
    '장산': {
        '중동': {'시간': 2, '거리': 0.9}
        },
    # 3호선
    '대저': {
        '체육공원': {'시간': 1, '거리': 0.8},
        '평강': {'시간': 1, '거리': 1},
        '등구': {'시간': 3, '거리': 2}
        },
    '체육공원': {
        '대저': {'시간': 1, '거리': 0.8},
        '강서구청': {'시간': 2, '거리': 1.1}
        },
    '강서구청': {
        '체육공원': {'시간': 2, '거리': 1.1},
        '구포': {'시간': 3, '거리': 1.6}
        },
    '구포': {
        '강서구청': {'시간': 3, '거리': 1.6},
        '덕천': {'시간': 3, '거리': 1.1}
        },
    '덕천': {
        '수정': {'시간': 3, '거리': 1.5},
        '구명': {'시간': 2, '거리': 1.2},
        '구포': {'시간': 3, '거리': 1.1},
        '숙등': {'시간': 2, '거리': 0.7}
        },
    '숙등': {
        '덕천': {'시간': 2, '거리': 0.7},
        '남산정': {'시간': 2, '거리': 1}
        },
    '남산정': {
        '숙등': {'시간': 2, '거리': 1},
        '만덕': {'시간': 2, '거리': 1.1}
        },
    '만덕': {
        '남산정': {'시간': 2, '거리': 1.1},
        '미남': {'시간': 4, '거리': 3.3}
        },
    '미남': {
        '만덕': {'시간': 4, '거리': 3.3},
        '사직': {'시간': 2, '거리': 0.8},
        '동래': {'시간': 3, '거리': 1}
        },
    '사직': {
        '미남': {'시간': 2, '거리': 0.8},
        '종합운동장': {'시간': 2, '거리': 0.8}
        },
    '종합운동장': {
        '사직': {'시간': 2, '거리': 0.8},
        '거제': {'시간': 1, '거리': 0.7}
        },
    '거제': {
        '종합운동장': {'시간': 1, '거리': 0.7},
        '연산': {'시간': 2, '거리': 0.7},
        '교대': {'시간': 2, '거리': 0.7},
        '거제해맞이': {'시간': 2, '거리': 1}
        },
    '연산': {'교대': {'시간': 2, '거리': 1},
           '시청': {'시간': 1, '거리': 0.9},
           '거제': {'시간': 2, '거리': 0.7},
           '물만골': {'시간': 2, '거리': 1.1}
           },
    '물만골': {
        '연산': {'시간': 2, '거리': 1.1},
        '배산': {'시간': 3, '거리': 1.1}
        },
    '배산': {
        '물만골': {'시간': 3, '거리': 1.1},
        '망미': {'시간': 2, '거리': 1.2}
        },
    '망미': {
        '배산': {'시간': 2, '거리': 1.2},
        '수영': {'시간': 2, '거리': 1}
        },
    '수영': {
        '광안': {'시간': 2, '거리': 0.9},
        '민락': {'시간': 2, '거리': 0.9},
        '망미': {'시간': 2, '거리': 1}
        },
    # 4호선
    '미남': {
        '만덕': {'시간': 4, '거리': 3.3},
        '사직': {'시간': 2, '거리': 0.8},
        '동래': {'시간': 3, '거리': 1}
        },
    '동래': {
        '명륜': {'시간': 2, '거리': 0.8},
        '교대': {'시간': 2, '거리': 1.2},
        '미남': {'시간': 3, '거리': 1},
        '수안': {'시간': 2, '거리': 0.7}
        },
    '수안': {
        '동래': {'시간': 2, '거리': 0.7},
        '낙민': {'시간': 2, '거리': 0.7}
        },
    '낙민': {
        '수안': {'시간': 2, '거리': 0.7},
        '충렬사': {'시간': 1, '거리': 0.7}
        },
    '충렬사': {
        '낙민': {'시간': 1, '거리': 0.7},
        '명장': {'시간': 2, '거리': 0.7}
        },
    '명장': {
        '충렬사': {'시간': 2, '거리': 0.7},
        '서동': {'시간': 2, '거리': 1}
        },
    '서동': {
        '명장': {'시간': 2, '거리': 1},
        '금사': {'시간': 2, '거리': 0.8}
        },
    '금사': {
        '서동': {'시간': 2, '거리': 0.8},
        '반여농산물시장': {'시간': 2, '거리': 0.8}
        },
    '반여농산물시장': {
        '금사': {'시간': 2, '거리': 0.8},
        '석대': {'시간': 2, '거리': 1.2}
        },
    '석대': {
        '반여농산물시장': {'시간': 2, '거리': 1.2},
        '영산대': {'시간': 2, '거리': 1.4}
        },
    '영산대': {
        '석대': {'시간': 2, '거리': 1.4},
        '윗반송': {'시간': 3, '거리': 1.1}
        },
    '윗반송': {
        '영산대': {'시간': 3, '거리': 1.1},
        '고촌': {'시간': 1, '거리': 0.8}
        },
    '고촌': {
        '윗반송': {'시간': 1, '거리': 0.8},
        '안평': {'시간': 3, '거리': 1.1}
        },
    '안평': {
        '고촌': {'시간': 3, '거리': 1.1}
        },
    # 동해선
    '부전': {
        '양정': {'시간': 2, '거리': 1.4},
        '서면': {'시간': 2, '거리': 0.6},
        '거제해맞이': {'시간': 3, '거리': 2.3}
        },
    '거제해맞이': {
        '부전': {'시간': 3, '거리': 2.3},
        '거제': {'시간': 2, '거리': 1}
        },
    '거제': {
        '종합운동장': {'시간': 1, '거리': 0.7},
        '연산': {'시간': 2, '거리': 0.7},
        '교대': {'시간': 2, '거리': 0.7},
        '거제해맞이': {'시간': 2, '거리': 1}
        },
    '교대': {
        '동래': {'시간': 2, '거리': 1.2},
        '연산': {'시간': 2, '거리': 1},
        '거제': {'시간': 2, '거리': 0.7},
        '동래(동해선)': {'시간': 3, '거리': 1.2}
        },
    '동래(동해선)': {
        '교대': {'시간': 3, '거리': 1.2},
        '안락': {'시간': 2, '거리': 0.9}
        },
    '안락': {
        '동래(동해선)': {'시간': 2, '거리': 0.9},
        '부산원동': {'시간': 2, '거리': 1.2}
        },
    '부산원동': {
        '안락': {'시간': 2, '거리': 1.1},
        '재송': {'시간': 1, '거리': 1}
        },
    '재송': {
        '부산원동': {'시간': 1, '거리': 1.1},
        '센텀': {'시간': 2, '거리': 1}
        },
    '센텀': {
        '재송': {'시간': 2, '거리': 1},
        '벡스코(시립미술관)': {'시간': 2, '거리': 1.4}
        },
    '벡스코(시립미술관)': {
        '센텀시티': {'시간': 2, '거리': 0.8},
        '동백': {'시간': 2, '거리': 1.1},
        '센텀': {'시간': 2, '거리': 1.4},
        '신해운대': {'시간': 5, '거리': 4.5}
        },
    '신해운대': {
        '벡스코(시립미술관)': {'시간': 5, '거리': 4.5},
        '송정': {'시간': 3, '거리': 2.9}
        },
    '송정': {
        '신해운대': {'시간': 3, '거리': 2.9},
        '오시리아': {'시간': 3, '거리': 1.1}
        },
    '오시리아': {
        '송정': {'시간': 3, '거리': 1.1},
        '기장': {'시간': 4, '거리': 5.7}
        },
    '기장': {
        '오시리아': {'시간': 4, '거리': 5.7},
        '일광': {'시간': 3, '거리': 3}
        },
    '일광': {
        '기장': {'시간': 3, '거리': 3},
        '좌천(동해선)': {'시간': 4, '거리': 5.1}
        },
    '좌천(동해선)': {
        '일광': {'시간': 4, '거리': 5.1},
        '월내': {'시간': 3, '거리': 3.5}
        },
    '월내': {
        '좌천(동해선)': {'시간': 3, '거리': 3.5},
        '서생': {'시간': 3, '거리': 2.6}
        },
    '서생': {
        '월내': {'시간': 3, '거리': 2.6},
        '남창': {'시간': 7, '거리': 8.4}
        },
    '남창': {
        '서생': {'시간': 7, '거리': 8.4},
        '망양': {'시간': 4, '거리': 4.4}
        },
    '망양': {
        '남창': {'시간': 4, '거리': 4.4},
        '덕하': {'시간': 4, '거리': 4.5}
        },
    '덕하': {
        '망양': {'시간': 4, '거리': 4.5},
        '개운포': {'시간': 2, '거리': 2.4}
        },
    '개운포': {
        '덕하': {'시간': 2, '거리': 2.4},
        '태화강': {'시간': 4, '거리': 4.9}
        },
    '태화강': {
        '개운포': {'시간': 4, '거리': 4.9}
        },
    # 부산김해
    '가야대': {
        '장신대': {'시간': 2, '거리': 0.9}
        },
    '장신대': {
        '가야대': {'시간': 2, '거리': 0.9},
        '연지공원': {'시간': 3, '거리': 1.2}
        },
    '연지공원': {
        '장신대': {'시간': 3, '거리': 1.2},
        '박물관': {'시간': 2, '거리': 1.1}
        },
    '박물관': {
        '연지공원': {'시간': 2, '거리': 1.1},
        '수로왕릉': {'시간': 2, '거리': 0.8}
        },
    '수로왕릉': {
        '박물관': {'시간': 2, '거리': 0.8},
        '봉황': {'시간': 1, '거리': 0.7}
        },
    '봉황': {
        '수로왕릉': {'시간': 1, '거리': 0.7},
        '부원': {'시간': 2, '거리': 1}
        },
    '부원': {
        '봉황': {'시간': 2, '거리': 1},
        '김해시청': {'시간': 2, '거리': 0.6}
        },
    '김해시청': {
        '부원': {'시간': 2, '거리': 0.6},
        '인제대': {'시간': 2, '거리': 1}
        },
    '인제대': {
        '김해시청': {'시간': 2, '거리': 1},
        '김해대학': {'시간': 2, '거리': 1.3}
        },
    '김해대학': {
        '인제대': {'시간': 2, '거리': 1.3},
        '지내': {'시간': 1, '거리': 0.8}
        },
    '지내': {
        '김해대학': {'시간': 1, '거리': 0.8},
        '불암': {'시간': 2, '거리': 0.7}
        },
    '불암': {
        '지내': {'시간': 2, '거리': 0.7},
        '대사': {'시간': 2, '거리': 1.1}
        },
    '대사': {
        '불암': {'시간': 2, '거리': 1.1},
        '평강': {'시간': 2, '거리': 1.2}
        },
    '평강': {
        '대사': {'시간': 2, '거리': 1.2},
        '대저': {'시간': 2, '거리': 1}
        },
    '대저': {
        '체육공원': {'시간': 1, '거리': 0.8},
        '평강': {'시간': 1, '거리': 1},
        '등구': {'시간': 3, '거리': 2}
        },
    '등구': {
        '대저': {'시간': 3, '거리': 2},
        '덕두': {'시간': 3, '거리': 1.9}
        },
    '덕두': {
        '등구': {'시간': 3, '거리': 1.9},
        '공항': {'시간': 2, '거리': 1.3}
        },
    '공항': {
        '덕두': {'시간': 2, '거리': 1.3},
        '서부산유통지구': {'시간': 2, '거리': 0.9}
        },
    '서부산유통지구': {
        '공항': {'시간': 2, '거리': 0.9},
        '괘법르네시떼': {'시간': 2, '거리': 2.3}
        },
    '괘법르네시떼': {
        '서부산유통지구': {'시간': 2, '거리': 2.3},
        '사상': {'시간': 1, '거리': 0.8}
        },
    '사상': {
        '덕포': {'시간': 3, '거리': 1.2},
        '감전': {'시간': 2, '거리': 1.1},
        '괘법르네시떼': {'시간': 1, '거리': 0.8}
        },
}

change_line = [
    ['명륜', '동래', '수안'],
    ['명륜', '동래', '미남'],
    ['교대', '동래', '수안'],
    ['교대', '동래', '미남'],
    ['수안', '동래', '명륜'],
    ['수안', '동래', '연산'],
    ['미남', '동래', '명륜'],
    ['미남', '동래', '교대'],
    ['동래', '교대', '거제'],
    ['동래', '교대', '동래(동해선)'],
    ['연산', '교대', '거제'],
    ['연산', '교대', '동래(동해선)'],
    ['거제', '교대', '동래'],
    ['거제', '교대', '연산'],
    ['동래(동해선)', '교대', '동래'],
    ['동래(동해선)', '교대', '연산'],
    ['교대', '연산', '거제'],
    ['교대', '연산', '물만골'],
    ['거제', '연산', '교대'],
    ['거제', '연산', '시청'],
    ['시청', '연산', '거제'],
    ['시청', '연산', '물만골'],
    ['물만골', '연산', '교대'],
    ['물만골', '연산', '시청'],
    ['양정', '부전', '거제해맞이'],
    ['서면', '부전', '거제해맞이'],
    ['거제해맞이', '부전', '양정'],
    ['거제해맞이', '부전', '서면'],
    ['부전', '서면', '부암'],
    ['부전', '서면', '전포'],
    ['부암', '서면', '부전'],
    ['부암', '서면', '범내골'],
    ['범내골', '서면', '부암'],
    ['범내골', '서면', '전포'],
    ['전포', '서면', '부전'],
    ['전포', '서면', '범내골'],
    ['수정', '덕천', '구포'],
    ['수정', '덕천', '숙등'],
    ['구포', '덕천', '수정'],
    ['구포', '덕천', '구명'],
    ['구명', '덕천', '구포'],
    ['구명', '덕천', '숙등'],
    ['숙등', '덕천', '수정'],
    ['숙등', '덕천', '구명'],
    ['덕포', '사상', '괘법르네시떼'],
    ['감전', '사상', '괘법르네시떼'],
    ['괘법르네시떼', '사상', '덕포'],
    ['괘법르네시떼', '사상', '감전'],
    ['광안', '수영', '망미'],
    ['민락', '수영', '망미'],
    ['망미', '수영', '광안'],
    ['망미', '수영', '민락'],
    ['센텀시티', '벡스코(시립미술관)', '신해운대'],
    ['센텀시티', '벡스코(시립미술관)', '센텀'],
    ['센텀', '벡스코(시립미술관)', '센텀시티'],
    ['센텀', '벡스코(시립미술관)', '동백'],
    ['신해운대', '벡스코(시립미술관)', '센텀시티'],
    ['신해운대', '벡스코(시립미술관)', '동백'],
    ['동백', '벡스코(시립미술관)', '센텀'],
    ['동백', '벡스코(시립미술관)', '신해운대'],
    ['체육공원', '대저', '평강'],
    ['체육공원', '대저', '등구'],
    ['평강', '대저', '체육공원'],
    ['등구', '대저', '체육공원'],
    ['만덕', '미남', '동래'],
    ['사직', '미남', '동래'],
    ['동래', '미남', '만덕'],
    ['동래', '미남', '사직'],
    ['종합운동장', '거제', '교대'],
    ['종합운동장', '거제', '거제해맞이'],
    ['거제해맞이', '거제', '종합운동장'],
    ['거제해맞이', '거제', '연산'],
    ['연산', '거제', '거제해맞이'],
    ['연산', '거제', '교대'],
    ['교대', '거제', '연산'],
    ['교대', '거제', '종합운동장'],
]

change_line_500 = [
    ['체육공원', '대저', '평강'],
    ['체육공원', '대저', '등구'],
    ['평강', '대저', '체육공원'],
    ['등구', '대저', '체육공원'],
    ['덕포', '사상', '괘법르네시떼'],
    ['감전', '사상', '괘법르네시떼'],
    ['괘법르네시떼', '사상', '덕포'],
    ['괘법르네시떼', '사상', '감전'],
]

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
traincanvas.bind("<Button-1>", show_station)

# 입력 창 생성
input_frame = tk.Frame(Lframe_bottom, bg="#F8E8EE", width=30, height=50)
input_frame.pack(pady=10, anchor=N)


start_label = tk.Label(Lframe_bottom, text="출발역 : ", bg="#F8E8EE")
start_label.place(x=25, y=8)

input_entry = tk.Entry(input_frame, width=30)
input_entry.grid(row=0, column=1)
input_entry.bind("<Return>")

destination_label = tk.Label(Lframe_bottom, text="도착역 : ", bg="#F8E8EE")
destination_label.place(x=25, y=28)

destination_entry = tk.Entry(input_frame, width=30)
destination_entry.grid(row=1, column=1)

timelabel = Label(Lframe_top, text="현재시각 : ", font=(my_font1, 15), bg="#F8E8EE")
timelabel.place(x=55, y=5)

searchbutton = Button(Lframe_bottom, text="검색", font=(my_font1, 15), background="#ffffff", command=lambda: (result()), relief='ridge')
searchbutton.place(x=112, y=60)

resetbutton = Button(Lframe_bottom, text="초기화", font=(my_font1, 15), command=reset_func, relief='ridge', bg="#ffffff")
resetbutton.place(x=212, y=60)

changebutton = Button(Lframe_bottom, text="↑↓", width=5, height=2, command=changeentry, relief='ridge', bg="#ffffff")
changebutton.place(x=315, y=9)

# 검색 결과 라벨
resultlabel = Label(Lframe_bottom, border=1, width=38, height=20, justify='center', font=(my_font1, 12), padx=0, pady=0, bg="#F2BED1", wraplength=390, fg='#F9F5F6')
resultlabel.place(x=0, y=120)

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
img = Image.open("station/환승역.png")
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

hiddenbtn = Button(frame2came1, width=4, height=2, background="#FFFFFF", bd=0, highlightthickness=0, command=hidden_window)
hiddenbtn.place(x=1450, y=1050)

time()
win.mainloop()