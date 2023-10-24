import datetime
from tkinter import *
from tkinter import ttk

#Define the window
my_window = Tk()

#Configure the window
my_window.title("Week Day Finder")
my_window.geometry("305x100")
my_window.resizable(False,False)

#Get values Function
def get_values():
    res_day = Day_Entry.get()
    res_month = Month_Entry.get()
    res_year = Year_Entry.get()   

    if not type(res_day) == int or not type(res_month) == int or not type(res_year) == int:
        Result_Text.config(text = "Invalid Format", justify="center")
        Day_Entry.delete(0, END)
        Month_Entry.delete(0 ,END)
        Year_Entry.delete(0, END)

    if res_day == "" or res_month == "" or res_month == "":
        Result_Text.config(text = "Fill all values", justify="center")

    day = int(str(res_day)[:2])
    month = int(str(res_month)[:2])
    year = int(str(res_year)[:4])

    if day > 31 or day <= 0:
        Day_Entry.insert(0, 1)
        day = 1
    elif month > 12 or month <= 0:
        Month_Entry.insert(0, 1)
        month = 1
    elif year > 2300 or year < 1700:
        Month_Entry.insert(0, 1700)
        year = 1700

    if not year % 4 == 0 and not year % 400 == 0:
        if month == 2 and day >= 29:
            day = 28
    else:
        if month == 2 and day > 29:
            day = 28

    Day_Entry.delete(0, END)
    Day_Entry.insert(0, day)

    Month_Entry.delete(0 ,END)
    Month_Entry.insert(0, month)

    Year_Entry.delete(0, END)
    Year_Entry.insert(0, year)

    dt = datetime.datetime(year, month, day).weekday()

    match dt:
        case 0:
            dt = "Monday"
        case 1:
            dt = "Tuesday"
        case 2:
            dt = "Wednesday"
        case 3:
            dt = "Thursday"
        case 4:
            dt = "Friday"
        case 5:
            dt = "Saturday"
        case 6:
            dt = "Sunday"

    Result_Text.config(text = dt, justify="center")
 
#Function that deletes everything
def Clear_Values():
    Day_Entry.delete(0, END)

    Month_Entry.delete(0 ,END)

    Year_Entry.delete(0, END)

    Result_Text.config(text = "")

#Design the GUI

#spaces
Frame_Space = Label(my_window,
                    text=" ")

#Text Labels
Day_Label = Label(my_window, text="Day")
Day_Label.grid(row=1, column=1,sticky = W)

Month_Label = Label(my_window, text="Month")
Month_Label.grid(row=2, column=1,sticky = W)

Year_Label = Label(my_window, text="Year")
Year_Label.grid(row=3, column=1,sticky = W)

#Enties
Day_Entry = Entry(my_window)
Day_Entry.grid(row=1,column=2)

Month_Entry = Entry(my_window)
Month_Entry.grid(row=2,column=2)

Year_Entry = Entry(my_window)
Year_Entry.grid(row=3,column=2)

#Buttons

#Enter
Enter_Button = Button(my_window,
text="Enter",
width="17",
command=get_values)

Enter_Button.grid(column=2,row=5)

#Clear
Clear_Button = Button(my_window,
text="Clear",
width="15",
command=Clear_Values)
Clear_Button.grid(row=5,column=4)

Frame_Space.grid(column=3,row=1)

#Result
Result_Text = Label(my_window, text="Result:",width=15)
Result_Text.grid(row=1,column=4)
Result_Text = Label(my_window, bg="Gray",width=15)
Result_Text.grid(row=2,column=4)

my_window.mainloop()