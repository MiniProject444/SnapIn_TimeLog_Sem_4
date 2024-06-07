import tkinter as tk
import mysql.connector
def confirm():
    id=e2.get()
    name=e1.get()
    dep=e3.get()
    ins="INSERT INTO prof VALUES(%s,%s,%s)"
    val=(id,name,dep)
    cusor.execute(ins,val)
    cusor.execute("select * from prof")
    print(cusor.fetchall())
    con.commit()

con=mysql.connector.connect(host='localhost',user='root',password='Sohampr@2004',database='Practicee')
cusor=con.cursor()
master=tk.Tk()

tk.Label(master,text='Student name').grid(row=2,column=1)
tk.Label(master,text='Roll no').grid(row=4,column=1)
tk.Label(master,text='Department').grid(row=6,column=1)

e1=tk.Entry(master)
e1.grid(row=2,column=4)
e2=tk.Entry(master)
e2.grid(row=4,column=4)
e3=tk.Entry(master)
e3.grid(row=6,column=4)

button=tk.Button(master,text='Submit',command=confirm).grid(row=8,column=2)

master.mainloop()