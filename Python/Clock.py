from datetime import *
import time
from tkinter import *

Window = Tk()
Window.title("Clock")
Window.resizable(False,False)
#Window.geometry("270x90")

def TheTime():
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second

    Hours.config(text=f"{hour} h")
    Minutes.config(text=f"{minute} m")
    Seconds.config(text=f"{second} s")

    #print(f"{hour} : {minute} : {second}")
    Window.after(500, TheTime)

mywidth = 6
myheight = mywidth / 2

mywidth = int(mywidth)
myheight = int(myheight)

Hours = Label(Window,width=mywidth,height=myheight,text="")
Hours.config(font=('Arial', 20))
Hours.grid(column=1,row=1)

Minutes = Label(Window,width=mywidth,height=myheight,text="")
Minutes.config(font=('Arial', 20))
Minutes.grid(column=2,row=1)

Seconds = Label(Window,width=mywidth,height=myheight,text="")
Seconds.config(font=('Arial', 20))
Seconds.grid(column=3,row=1)

TheTime()
Window.mainloop()




