from tkinter import *
from tkinter.colorchooser import askcolor


window = Tk()
window.maxsize(150,150)
window.minsize(150,150)

color = askcolor()



myframe = Frame(window,
                width=100,
                height=100,
                background=color[1]).pack()
                
spaceframe = Frame(window,
                height=25).pack()

resultcolor = Label(window,
                    text=color[1]).pack()


window.mainloop()