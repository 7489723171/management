from Tkinter import *
from tkMessageBox import *

import sqlite3
con=sqlite3.Connection('details')
cur=con.cursor()

#def full():

master = Tk()
master.title('map')
w = Canvas(master, width=400, height=400)
l1=w.create_line(0,20,320,20,fill='red',width=4)
for i in range(1,16):
    a=w.create_line(20*i,20,20*i,80,width=4)
    z=w.create_line(20*i,140,20*i,200,width=4)
    y=w.create_line(20*i,260,20*i,320,width=4)


ran = cur.execute("select slot from details where vn !='None'").fetchall()


def full():
    j=0
    for l in ran:
        i=ran[j][0]
        #print j
        j=j+1
        print i
        
        
        #for i in l:
        if(i<16):
                #i=(i)*20
                Label(w,text="O",bg="red",fg="red").place(x=5+(20*i),y=50,width=10,height=10)
                #j=j+1
                #print i
        if i>15 and i<32:
                #i=(i-16)*20
                Label(w,text="O",bg="red",fg="red").place(x=5+((i-16)*20),y=170,width=10,height=10)
                #j=j+1
                #print i
        if i>31 and i<48:
                #i=(i-32)*20
                Label(w,text="O",bg="red",fg="red").place(x=5+((i-32)*20),y=290,width=10,height=10)
                #j=j+1
        '''else:
                showinfo("FULL","NO VACANCY")'''
            
            
            

l2=w.create_line(0,140,320,140,fill='red',width=4)
l3=w.create_line(0,260,320,260,fill='red',width=4)
#for i in range(2,20):
    
   # a=w.create_line(20*i,320,20*i,380,width=4)
b=Button(master,text='GET CURRENT STATUS',command=full).pack()

w.pack()
Label(w,text="G.F.",font="times 15 bold",bd=10).place(x=360,y=45,anchor=CENTER)
Label(w,text="1.F.",font="times 15 bold",bd=10).place(x=360,y=175,anchor=CENTER)
Label(w,text="2.F.",font="times 15 bold",bd=10).place(x=360,y=295,anchor=CENTER)

master.minsize(250,350)
master.maxsize(600,600)
mainloop()
