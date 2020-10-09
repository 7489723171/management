from Tkinter import *
import os
root = Tk()
import sqlite3
con=sqlite3.Connection('details')
cur=con.cursor()
def clear():
    li = root.place_slaves()
    for i in li:
        i.destroy()

def get():
    clear()
    Label(root, text = 'vehicle type: 1-Two Wheeler 2-Four Wheeler', font = 'times 15 bold').place(relx = .6, rely = .2, anchor = NW)
    Label(root, text = 'Vehicle Number:', font = 'times 15 bold').place(relx = .2, rely = .4, anchor = NW)
    Label(root, text = 'Vehicle Type:', font = 'times 15 bold').place(relx = .2, rely = .48, anchor = NW)
    Label(root, text = 'Customer Name:', font = 'times 15 bold').place(relx = .2, rely = .56, anchor = NW)
    Label(root, text = 'Mobile Number:', font = 'times 15 bold').place(relx = .2, rely = .64, anchor = NW)
    Label(root, text = 'Vehicle Model:', font = 'times 15 bold').place(relx = .2, rely = .72, anchor = NW)
  
    dt = cur.execute("select vn,vt,cn,mn,vmo from details where slot = ?",[sn.get()]).fetchone()
    s = 0.4
    for i in dt:
        Label(root, text = i, font = 'times 15 bold').place(relx = .5, rely = s, anchor = NW)
        s = s+0.08
    
'''Label(root,text = "Enter slot Number", font = 'times 20').place(relx = .2, rely = .2, anchor = CENTER)
sn = Entry(root, font = 'times 20')
sn.place(relx = .5, rely = .18, anchor = NW)
Button(root, text = "GET", height = 1, width = 5, command = get).place(relx = .5, rely =.3)'''

Label(root, text = 'ENQUIRE', font = 'times 28 bold').grid(row = 0, columnspan = 4)
Label(root, text = '').grid(row = 1, columnspan = 4)
Label(root,text = "Enter slot Number", font = 'times 20').grid(row = 2, column = 1)
sn = Entry(root, font = 'times 20')
sn.grid(row = 2, column = 3)
Label(root, text = '').grid(row = 3, columnspan = 4)
Button(root, text = "GET", height = 1, width = 5, command = get).grid(row = 4, column = 3)


root.minsize(500,500)
root.mainloop()
