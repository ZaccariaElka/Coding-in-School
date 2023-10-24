#Modules
from tkinter import * #Gui
from tkinter import ttk #Gui

print("Logs")

#Define the window
my_window = Tk()

#Configure the window
my_window.title("Week Day Finder")
my_window.geometry("305x100")
my_window.resizable(False,False)

#Function to get week day
def get_weekday(year,month,day):

    #gets wrong values
    y = year
    m = month
    d = day

    #(Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7
    yy = y % 100 #Last 2 digits of the year

    yc = (yy + yy / 4) #Year code

    mc = 0 #Month code

    match m:
        case 1:
            mc = 0
        case 2:
            mc = 3
        case 3:
            mc = 3
        case 4:
            mc = 6
        case 5:
            mc = 1
        case 6:
            mc = 4
        case 7:
            mc = 6
        case 8:
            mc = 2
        case 9:
            mc = 5
        case 10:
            mc = 0
        case 11:
            mc = 3
        case 12:
            mc = 5
    
    cc = 0 #Century code

    if y >= 1700 and y <= 1799:
        cc = 4
    if y >= 1800 and y <= 1899:
        cc = 2
    if y >= 1900 and y <= 1999:
        cc = 0
    if y >= 2000 and y <= 2099:
        cc = 6
    if y >= 2100 and y <= 2199:
        cc = 4
    if y >= 2200 and y <= 2299:
        cc = 2
    if y >= 2300 and y <= 2399:
        cc = 0
    
    lp = 0 #Leap year?

    if y % 400 == 0 and y % 4 == 0:
        lp = 1
    else: 
        lp = 0
    
    calculate = yc + mc + cc + d - lp 

    if m == 1 or m == 2: #January, February = calc - 1
        calculate = calculate - 1 

    result = calculate % 7 #Mod calc

    weekday = "" #Name of the week

    match int(result):
        case 0:
            weekday = "Sunday"
        case 1:
            weekday = "Monday"
        case 2:
            weekday = "Tuesday"
        case 3:
            weekday = "Wednesday"
        case 4:
            weekday = "Thursday"
        case 5:
            weekday = "Friday"
        case 6:
            weekday = "Saturday"

    print(f"{y}, {m} {d}")
    print("---")
    print(f"{yy} (yy)")
    print(f"{yc} (year code)")
    print(f"{mc} (month code)")
    print(f"{cc} (century cude)")
    print(f"{d} (day)")
    print(f"{lp} (leap year)")
    print("---")
    print(f"{int(result)} ({result}), {weekday}")
    Result_Text.config(text = weekday, justify="center")
        

#Get values Function
def get_values():
    res_day = Day_Entry.get()
    res_month = Month_Entry.get()
    res_year = Year_Entry.get()   

    isdaynum = res_day.isnumeric()
    ismonthnum = res_month.isnumeric()
    isyearnum = res_year.isnumeric()

    if res_day == "" or res_month == "" or res_month == "":
        Result_Text.config(text = "Fill all values", justify="center")
    elif isdaynum == False or ismonthnum == False or isyearnum == False:

        Day_Entry.delete(0, END)
        Month_Entry.delete(0 ,END)
        Year_Entry.delete(0, END)

        Result_Text.config(text = "Invalid Format", justify="center")

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

    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day = 30

    Day_Entry.delete(0, END)
    Day_Entry.insert(0, day)

    Month_Entry.delete(0 ,END)
    Month_Entry.insert(0, month)

    Year_Entry.delete(0, END)
    Year_Entry.insert(0, year)
    print(f"get_values - {year}, {month} {day}")
    get_weekday(year, month, day)
 

def Clear_Values():
    Day_Entry.delete(0, END)

    Month_Entry.delete(0 ,END)

    Year_Entry.delete(0, END)

    Result_Text.config(text = "")

#Design the GUI

#spaces
Frame_Space = Label(my_window,text=" ")

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

#Button
Enter_Button = Button(my_window,
text="Enter",
width="17",
command=get_values)

Enter_Button.grid(column=2,row=5)

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