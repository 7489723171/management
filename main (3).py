from Tkinter import *
import sqlite3
con=sqlite3.Connection('details')
cur=con.cursor()

from tkMessageBox import *

'''cur.execute("drop table details")
cur.execute("create table if not exists details(slot number primary key ,vn varchar(20),vt number,cn varchar(20), mn number, vmo varchar(20), time datetime)")
con.commit()
i=0
while(i<47):
    cur.execute("insert into details(slot) values(?)",[i])
    con.commit()
    i = i+1'''

import os
root=Tk()


def submit():
    vno = e1.get()
    vty = t.get()
    cnm = e2.get()
    cmb = e3.get()
    vmd = e4.get()
    i = 0
    
    while(i<48):
        ch = cur.execute("select vn from details where vn = ?",[vno]).fetchall()
        res = cur.execute("select vn from details where slot = ?",(i,)).fetchall()
        if res[0][0]==None and len(ch)==0:
            time = cur.execute("select current_timestamp").fetchall()
            cur.execute("update details set vn = ?,vt = ?,cn = ?, mn = ?, vmo = ?, time = ? where slot = ?",(vno,vty,cnm,cmb,vmd,time[0][0],i))
            con.commit()
            showinfo("Entry","Vehicle Number: %s\n Slot Number: %s\n Entry time: %s"%(vno,i,time[0][0]))
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            break
        if len(ch)!=0:
            showinfo("invalid","vehicle already in slot")
            break
        else:
            i= i+1
    
  

t=IntVar()
c = Canvas(root, width=1500, height=1500)
l=c.create_line(500,0,500,1500,fill='red',width=4)
li=c.create_line(1000,0,1000,1500,fill='red',width=4)
c.pack()
l1=Label(c,text='VEHICLE DETAILS',font="times 25 bold ").place(x=600,y=20)
l2=Label(c,text='VEHICLE TYPE',font="times 15 bold ").place(x=670,y=70)
rb1=Radiobutton(c,text='FOUR WHEELER',variable=t,value=1)
rb1.place(x=670,y=100)
rb2=Radiobutton(c,text='TWO WHEELER',variable=t,value=2).place(x=670,y=120)
l3=Label(c,text='VEHICLE NO.',font="times 15 bold ").place(x=675,y=160)
e1=Entry(c,width=35)
e1.place(x=670,y=200)
l4=Label(c,text='CUSTOMER NAME.',font="times 15 bold ").place(x=650,y=240)
e2=Entry(c,width=35)
e2.place(x=670,y=280)
l5=Label(c,text='CUSTOMER MOB.NO.',font="times 15 bold ").place(x=650,y=320)
e3=Entry(c,width=35)
e3.place(x=670,y=360)
l6=Label(c,text='VEHICLE MODEL',font='times 15 bold').place(x=650,y=400)
e4=Entry(c,width=35)
e4.place(x=670,y=440)
Button(root,bg='red',text='SUBMIT',command = submit).place(x=750,y=500,width=70)
root.minsize(1000,500)
img=PhotoImage(file="p1.gif")
Label(c,image=img).place(x=0,y=0)



root.mainloop()
