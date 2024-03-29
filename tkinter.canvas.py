import tkinter

window=tkinter.Tk()
window.geometry("1000x1000")

# line, arc, polygon, oval
# canvas = tkinter.Canvas(window, relief="solid", bd=2)
# line = canvas.create_line(10,10,50,50,100,30, fill="red", width=10)
# arc = canvas.create_arc(100,100,200,200, start=0, extent=150, fill="yellow")
# polygon = canvas.create_polygon(50,50,300,50,150,150,150,30, fill="blue")
# oval = canvas.create_oval(10,200,150,250, fill="pink")
# canvas.pack()

screen = tkinter.Canvas(window)
screen.pack()

# circle = screen.create_oval(30,100,150,200, fill="purple")
# rect = screen.create_rectangle(130,200,300,100, fill="blue")
# rect2 = screen.create_rectangle(200,200,300,100, fill="green")
# arm1 = screen.create_line(200,200,300,250, fill="red")
# arm2 = screen.create_line(200,200,300,250, fill="red")

a = screen.create_line(0,100,100,100, fill="red")



window.mainloop()