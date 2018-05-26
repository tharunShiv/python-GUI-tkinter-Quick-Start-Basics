from tkinter import *


def onclick():
    uname=E1.get()
    pword=E2.get()
    cur.execute('insert into login values (?,?)',(uname,pword))
    con.commit()
    cur.execute('select * from login')
    print(cur.fetchall())

def dele():
    print("not saved")
    cur.execute('select * from login')
    print(cur.fetchall())

L1 = Label(top, text="User Name")
L1.grid(row=0,column=0,padx=25,pady=25)
E1 = Entry(top, bd =10,bg="red",fg="white",font="arial")
E1.grid(row=0,column=1,padx=25,pady=25)

L2 = Label(top, text="Password")
L2.grid(row=1,column=0,padx=25,pady=25)
E2 = Entry(top, bd =25,bg="green",fg="white",show="*",font="arial")
E2.grid(row=1,column=1,padx=25,pady=25)


B1=Button(top,text="login",command=onclick)
B1.grid(row=2,column=0,padx=25,pady=25)
B2=Button(top,text="cancle",command=dele)
B2.grid(row=2,column=1,padx=25,pady=25)

c1 = IntVar()
c = Checkbutton(top, text="save login", variable=c1, onvalue=1, offvalue=0, padx=25, pady=10).grid(row=3, column=0)

top.mainloop()
