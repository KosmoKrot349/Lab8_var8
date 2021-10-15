from tkinter import *
from tkinter import messagebox
from Pack import Pack
from Pack import Dog
from LogInWindow import LogInWindow
import pickle
from CustomDbContext import *


def addToPackDB():
   sql = F'INSERT INTO dogs (weight,height,classification,sound,food,name,age)VALUES({wieght.get()},{height.get()},\'{calassific.get()}\',\'{sound.get()}\',\'{food.get()}\',\'{name.get()}\',{age.get()})'
   context.InsertIntoTable(sql)
   messagebox.showinfo("Message", 'new dog added')

def deleteFromPackDB():
    sql=F'delete from dogs where id={id.get()}'
    context.InsertIntoTable(sql)
    messagebox.showinfo("Message", F'record №{id.get()} deleted')

def showPackDB():
   sql = F'select * from dogs'
   context.ShowRecords(sql)




if __name__ == '__main__':
    
   
    context = DbContext()
    wind=LogInWindow(context)
    
    root = Tk()
 

    if context.isSuccessConnection!=0:

        #ENTRIES
        wieght = Entry()
        height = Entry()
        calassific = Entry()
        sound = Entry()
        food = Entry()
        name = Entry()
        age = Entry()
        id = Entry()

        wieght.grid(row=0, column=1)
        height.grid(row=1, column=1)
        calassific.grid(row=2, column=1)
        sound.grid(row=3, column=1)
        food.grid(row=4, column=1)
        name.grid(row=5, column=1)
        age.grid(row=6, column=1)
        id.grid(row=7, column=1)

        #LABELS
        wieghtLabel = Label(text='Рост: ')
        heightLabel = Label(text='Вес: ')
        calassificLabel = Label(text='Класс: ')
        soundLabel =Label(text='Звук издаёт: ')
        foodLabel = Label(text='Корм: ')
        nameLabel = Label(text='Кличка: ')
        ageLabel = Label(text='Возраст: ')
        idLabel = Label(text='Id: ')

        wieghtLabel.grid(row=0,column=0)
        heightLabel.grid(row=1, column=0)
        calassificLabel.grid(row=2, column=0)
        soundLabel.grid(row=3, column=0)
        foodLabel.grid(row=4, column=0)
        nameLabel.grid(row=5, column=0)
        ageLabel.grid(row=6, column=0)
        idLabel.grid(row=7, column=0)



        #BUTTONS
        btn = Button(text="Добавить",  command=addToPackDB)
        btn2 = Button(text="Удалить", command=deleteFromPackDB)
        btn3 = Button(text="Просмотр", command=showPackDB)

        btn.grid(row=8, column=0,columnspan=3 )
        btn2.grid(row=9, column=0,columnspan=3)
        btn3.grid(row=10, column=0,columnspan=3)

        root.mainloop()
