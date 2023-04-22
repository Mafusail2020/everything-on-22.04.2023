from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext


#Если кнопка нажата
def command():
    res = "Hoi, {}, im TeM".format(entr.get())
    lbl_2 = Label(my_wind,text=res, font=('Arial', 20))
    lbl_2.grid(column=0, row=2)
    entr.config(state='disabled')

#Сам хослт
my_wind = Tk()
my_wind.geometry('1500x500')
my_wind.title("Who are you?")

#Списочек
comb = Combobox(my_wind)
comb['values'] = (1, 2, 3, 4, 5, "Text")
comb.current(1)
comb.grid(column=0, row=0)

#Ввод
entr = Entry(my_wind, width=10)
entr.grid(column=2, row=0)

#Текст 1
lbl_1 = Label(my_wind,text='Hoi, wats ur name??/??', font=('Comic Sans', 30))
lbl_1.grid(column=0, row=0)

#Сама кнопка
butt = Button(my_wind, text='Sus', command=command,font=('Arial', 15))
butt.grid(column=0, row=1)

#включение ввода
entr.config(state='normal')

#Незакрытие холста
my_wind.mainloop()
