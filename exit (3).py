from Tkinter import *
root=Tk()
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('details')
cur=con.cursor()

def ex():
    vno = e1.get()
    info = cur.execute("select slot from details where vn = ?",[vno]).fetchall()
    if len(info)==0:
        showerror("not found","Wrong Vehicle Number")
    else:
        cur.execute("update details set vn = null, vt = null,cn = null,mn = null,vmo = null, time = null where vn = ?",[vno])
        con.commit()
        e2.insert(END,"$5")
        showinfo("exit","Vehicle Number: %s\n Exited from: %s"%(vno,info[0][0]))
        e2.delete(0,END)
        e1.delete(0,END)

ca =Canvas(root,width=500,height=500)
ca.pack()
l=Label(ca,text='VEHICLE EXIT',font="times 20 bold ").place(x=160,y=20)
l1=Label(ca,text=' ENTER VEHICLE NO.',font="times 15 bold ").place(x=160,y=80)
e1=Entry(ca,width=35)
e1.place(x=160,y=120)
l1=Label(ca,text='RENT.',font="times 15 bold ").place(x=220,y=160)
e2=Entry(ca,width=20,font="times 15 bold ")
e2.place(x=160,y=200)
b=Button(ca,text ="EXIT",bd=5, command = ex).place(width=50,x=230,y=240)
b1=Button(ca,text ="PRINT RENT",bd=5).place(width=80,x=210,y=280)
root.mainloop()
