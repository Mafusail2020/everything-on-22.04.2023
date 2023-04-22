from tkinter import *
# from tkinter.ttk import Combobox
# from tkinter.ttk import Checkbutton

i = -1

stri = ""

def ultra_command_1():

    lbl = Label(my_wind, text="1", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "1"



def ultra_command_2():
    lbl = Label(my_wind, text="2", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "2"


def ultra_command_3():
    lbl = Label(my_wind, text="3", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "3"


def ultra_command_4():
    lbl = Label(my_wind, text="4", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "4"


def ultra_command_5():
    lbl = Label(my_wind, text="5", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "5"


def ultra_command_6():
    lbl = Label(my_wind, text="6", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "6"


def ultra_command_7():
    lbl = Label(my_wind, text="7", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "7"


def ultra_command_8():
    lbl = Label(my_wind, text="8", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "8"


def ultra_command_9():
    lbl = Label(my_wind, text="9", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "9"


def ultra_command_0():
    lbl = Label(my_wind, text="0", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "0"


def ultra_command_pl():
    lbl = Label(my_wind, text="+", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "+"


def ultra_command_mn():
    lbl = Label(my_wind, text="-", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "-"


def delit():
    lbl = Label(my_wind, text="//", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "/"


def umn():
    lbl = Label(my_wind, text="*", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "*"

def dot():
    lbl = Label(my_wind, text=".", font=("Arial", 15))
    global i
    i += 1
    lbl.grid(column=i, row=0)
    global stri
    stri += "."

def res():
    global stri
    stri = eval(stri)
    lbl = Label(my_wind, text=f"= {stri}", font=("Arial", 15))
    global i
    i+=1
    lbl.grid(column=i, row=0)


my_wind = Tk()
my_wind.geometry('500x250')
my_wind.title("Idk what to type")
my_wind.resizable(0, 0)

num_1 = Button(my_wind, text="1", font=("Arial", 15), command=ultra_command_1)
num_1.grid(column=0, row=3)
num_2 = Button(my_wind, text="2", font=("Arial", 15), command=ultra_command_2)
num_2.grid(column=1, row=3)
num_3 = Button(my_wind, text="3", font=("Arial", 15), command=ultra_command_3)
num_3.grid(column=2, row=3)
num_4 = Button(my_wind, text="4", font=("Arial", 15), command=ultra_command_4)
num_4.grid(column=0, row=2)
num_5 = Button(my_wind, text="5", font=("Arial", 15), command=ultra_command_5)
num_5.grid(column=1, row=2)
num_6 = Button(my_wind, text="6", font=("Arial", 15), command=ultra_command_6)
num_6.grid(column=2, row=2)
num_7 = Button(my_wind, text="7", font=("Arial", 15), command=ultra_command_7)
num_7.grid(column=0, row=1)
num_8 = Button(my_wind, text="8", font=("Arial", 15), command=ultra_command_8)
num_8.grid(column=1, row=1)
num_9 = Button(my_wind, text="9", font=("Arial", 15), command=ultra_command_9)
num_9.grid(column=2, row=1)
num_0 = Button(my_wind, text="0", font=("Arial", 15), command=ultra_command_0)
num_0.grid(column=1, row=4)

# Plus, minus and equality
plus = Button(my_wind, text="+", font=("Arial", 15), command=ultra_command_pl)
plus.grid(column=0, row=4)
minus = Button(my_wind, text="-", font=("Arial", 15), command=ultra_command_mn)
minus.grid(column=2, row=4)
delit = Button(my_wind, text="//", font=("Arial", 15), command=delit)
delit.grid(column=3, row=2)
dot = Button(my_wind, text=".", font=("Arial", 15), command=dot)
dot.grid(column=3, row=4)
umn = Button(my_wind, text="*", font=("Arial", 15), command=umn)
umn.grid(column=3, row=3)
equ = Button(my_wind, text="=", font=("Arial", 15), command=res)
equ.grid(column=3, row=1)

my_wind.mainloop()
