from tkinter import *
from tkinter import messagebox
from CustomDbContext import *


class LogInWindow:

    root=Tk()
    DBContext=DbContext()

    dataBaseVar=StringVar()
    dataBaseUserVar=StringVar()
    dataBasePasswordVar=StringVar()
    dataBaseServerVar=StringVar()

    def __init__(self,DBContext):
        self.DBContext=DBContext


        self.dataBaseVar.set('dogs')
        self.dataBaseUserVar.set('root')
        self.dataBasePasswordVar.set('1111')
        self.dataBaseServerVar.set('localhost')

        dataBase=Entry(textvariable=self.dataBaseVar)
        dataBaseUser=Entry(textvariable=self.dataBaseUserVar)
        dataBasePassword=Entry(textvariable=self.dataBasePasswordVar)
        dataBaseServer=Entry(textvariable=self.dataBaseServerVar)

        dataBase.grid(row=1, column=1)
        dataBaseUser.grid(row=2, column=1)
        dataBasePassword.grid(row=3, column=1)
        dataBaseServer.grid(row=4, column=1)

          #LABELS
        dataBaseLabel = Label(text='База: ')
        dataBaseUserLabel = Label(text='Пользователь: ')
        dataBasePasswordLabel = Label(text='Пароль: ')
        dataBaseServerLabel =Label(text='Сервер: ')

        dataBaseLabel.grid(row=1, column=0)
        dataBaseUserLabel.grid(row=2, column=0)
        dataBasePasswordLabel.grid(row=3, column=0)
        dataBaseServerLabel.grid(row=4, column=0)

        btn = Button(text="Подключение", command=self.ConnectToDB)
       
        btn.grid(row=5, column=0,columnspan=2)

        self.root.mainloop()

    def ConnectToDB(self):
        self.DBContext.SetFileds(self.dataBaseVar.get(),self.dataBaseUserVar.get(),self.dataBasePasswordVar.get(),self.dataBaseServerVar.get())
        self.DBContext.CreateConnect()
        if self.DBContext.isSuccessConnection==1:   
            self.root.destroy()
        else:
            messagebox.showinfo("Error", 'some errors happen')
