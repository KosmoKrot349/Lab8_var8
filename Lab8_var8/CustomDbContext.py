import mysql.connector
from mysql.connector import Error
from Pack import *

class DbContext:
    dataBase=''
    dataBaseUser=''
    dataBasePassword=''
    dataBaseServer=''
    isSuccessConnection=0
    conn=mysql.connector

    def __init__ (self):
        self.dataBase=''
        self.dataBaseUser=''
        self.dataBasePassword=''
        self.dataBaseServer=''

    def SetFileds(self,dataBase,dataBaseUser,dataBasePassword,dataBaseServer):
        self.dataBase=dataBase
        self.dataBaseUser=dataBaseUser
        self.dataBasePassword=dataBasePassword
        self.dataBaseServer=dataBaseServer

    def CreateConnect(self):
        try:
            self.conn=mysql.connector.connect(
                host=self.dataBaseServer,
                database=self.dataBase,
                user=self.dataBaseUser,
                password=self.dataBasePassword)
            if self.conn.is_connected: 
                self.isSuccessConnection=1
        except Error as e:
            self.isSuccessConnection=0
    
    def InsertIntoTable(self,sql):
        mycursor = self.conn.cursor()
        mycursor.execute(sql)
        self.conn.commit()

    def ShowRecords(self,sql):
        mycursor = self.conn.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        pack = Pack()
        for dogData in myresult:
            pack.addNewDog(Dog(dogData[0],dogData[1],dogData[2],dogData[3],dogData[4],dogData[5],dogData[6],dogData[7]))
        pack.showPack()

                