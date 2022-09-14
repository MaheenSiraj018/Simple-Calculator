from tkinter import *
m=Tk()
m.title("Calculator")
m.geometry("500x800")
def click(event):
    global value
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if value.get().isdigit():
            val=int(value.get())
        else:
            val=eval(scr.get())

        value.set(val)
        scr.update()
    elif text=="C":
        value.set("")
        scr.update
    else:
        value.set(value.get()+text)
        scr.update()

value= StringVar()
value.set("")
scr=Entry(m,textvariable=value,font="calibri 30 bold")
scr.pack(fill=X,ipadx=8,pady=10,padx=10)

f1=Frame(m,bg="grey")

b1=Button(f1,text="9",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b1.pack( side="left",padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f1,text="8",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b2.pack( side="left",padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="7",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b3.pack(side="left",padx=10,pady=10)
b3.bind("<Button-1>",click)
f1.pack()

f2=Frame(m,bg="grey")

b1=Button(f2,text="6",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b1.pack( side="left",padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f2,text="5",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b2.pack( side="left",padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f2,text="4",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b3.pack(side="left",padx=10,pady=10)
b3.bind("<Button-1>",click)
f2.pack()

f3=Frame(m,bg="grey")

b1=Button(f3,text="3",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b1.pack( side="left",padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f3,text="2",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b2.pack( side="left",padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f3,text="1",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b3.pack(side="left",padx=10,pady=10)
b3.bind("<Button-1>",click)
f3.pack()

f4=Frame(m,bg="grey")

b1=Button(f4,text="0",font="Calibri 28 bold",padx=15,pady=10,bg="black",fg="white")
b1.pack( side="left",padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f4,text="-",font="Calibri 30 bold",padx=15,pady=10,bg="black",fg="white")
b2.pack( side="left",padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f4,text="+",font="Calibri 30 bold",padx=15,pady=10,bg="black",fg="white")
b3.pack(side="left",padx=10,pady=10)
b3.bind("<Button-1>",click)
f4.pack()

f5=Frame(m,bg="grey")

b1=Button(f5,text="/",font="Calibri 27 bold",padx=15,pady=10,bg="black",fg="white")
b1.pack( side="left",padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f5,text="*",font="Calibri 27 bold",padx=15,pady=10,bg="black",fg="white")
b2.pack( side="left",padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f5,text="%",font="Calibri 27 bold",padx=15,pady=10,bg="black",fg="white")
b3.pack(side="left",padx=10,pady=10)
b3.bind("<Button-1>",click)
f5.pack()

f6=Frame(m,bg="grey")
b1=Button(f6,text=".",font="Calibri 30 bold",padx=15,pady=10,bg="black",fg="white")
b1.pack( side="left",padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f6,text="=",font="Calibri 30 bold",padx=15,pady=10,bg="black",fg="white")
b2.pack( side="left",padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f6,text="C",font="Calibri 30 bold",padx=15,pady=10,bg="black",fg="white")
b3.pack(side="left",padx=10,pady=10)
b3.bind("<Button-1>",click)
f6.pack()


m.mainloop()