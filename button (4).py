from Tkinter import *
import os
def map():
    os.startfile("map.py")
def entry():
    os.startfile("main.py")
def exi():
    os.startfile("exit.py")
def enquire():
    os.startfile("enquire.py")
root=Tk()
img1=PhotoImage(file="p2.gif")
Button(root,image=img1,command=map).place(x=50,y=50)
Label(root,text="MAP",font= "times 25 bold").place(x=110,y=260)
img2=PhotoImage(file="ent.gif")
Button(root,image=img2,command=entry).place(x=350,y=50)
Label(root,text="ENTRY",font= "times 25 bold").place(x=410,y=260)
img3=PhotoImage(file="exit.gif")
Button(root,image=img3,command=exi).place(x=650,y=50)
Label(root,text="EXIT",font= "times 25 bold").place(x=710,y=260)
img4=PhotoImage(file="enquire.gif")
Button(root,image=img4,command = enquire).place(x=950,y=50)
Label(root,text="ENQUIRE",font= "times 25 bold").place(x=970,y=260)

#root.minsize(500,500)

root.minsize(500,500)
root.mainloop()
