from tkinter import*
#import tkinter.messagebox as tkMessageBox
import sqlite3
top=Tk()
top.geometry('300x300')
Name=StringVar()
Gender=StringVar()
Age=StringVar()
def database():
   name1=Name.get()
   gen=Gender.get()
   age=Age.get()
   conn = sqlite3.connect('User.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS userdata1 (Name TEXT, Gender TEXT, Age Text)')
   cursor.execute('INSERT INTO userdata1 (Name, Gender, Age) \
                  VALUES(?,?,?)', (name1, gen, age))
   conn.commit()
lab1=Label(top, text="Save details")
lab1.place(x=120, y=10)

lab2=Label(top, text="Name")
lab2.place(x=40, y=40)
ent1=Entry(top, textvariable=Name)
ent1.place(x=120, y=40)

lab3=Label(top, text="Gender")
lab3.place(x=40, y=70)
ent2=Entry(top, textvariable=Gender)
ent2.place(x=120, y=70)

lab4=Label(top, text="Age")
lab4.place(x=40, y=100)
ent3=Entry(top, textvariable=Age)
ent3.place(x=120, y=100)


sav=Button(top, text="Save", command=database)
sav.place(x=140, y=130)
top.mainloop()