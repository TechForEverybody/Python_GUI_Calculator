from tkinter import *
sk = Tk()
sk.geometry("500x650")
sk.maxsize(500, 650)
sk.minsize(500, 650)
sk.title("Shiva's CALCULATOR")
sk.config(background="#686de0")
equation=StringVar()
equation.set("")
s1="0"
s2="0"
calcsign = ""
def clicked(event):
    global equation,s1,s2,calcsign
    if equation.get()=="मुझे नहीं पता":
        equation.set("")
        screen.update()
    text=event.widget.cget("text")
    text=text.replace(" ","")
    if text=="=":
        s2=equation.get()
        try:
            v1=float(s1)
            v2=float(s2)
            v=0
            if calcsign=="+":
                v=v1+v2
            elif calcsign=="-":
                v=v1-v2
            elif calcsign=="*":
                v=v1*v2
            elif calcsign=="/":
                v=v1/v2
            else:
                v=v1+v2
            equation.set(str(v))
        except Exception as e:
            equation.set("मुझे नहीं पता")
        L.config(text="")
    elif text=="c":
        equation.set("")
        s1="0"
        s2="0"
    elif text=="+":
        if equation.get()!="":
            calcsign="+"
            L.config(text="+")
            s1=equation.get()
            equation.set("")
        else:
            equation.set("")
    elif text=="-":
        if equation.get()!="":
            L.config(text="-")
            calcsign="-"
            s1=equation.get()
            equation.set("*")
        else:
            equation.set("")
    elif text=="*":
        if equation.get()!="":
            L.config(text="*")
            calcsign="*"
            s1=equation.get()
            equation.set("")
        else:
            equation.set("")
    elif text=="/":
        if equation.get()!="":
            L.config(text="/")
            calcsign="/"
            s1=equation.get()
            equation.set("")
        else:
            equation.set("")
    else:
        equation.set(equation.get()+text)
screen=Entry(sk,textvariable=equation,font="ROMEN 45 bold")
screen.pack(fill=X,padx=5,pady=2)
L=Label(sk,text="",font="ROMEN 25 bold")
L.pack(fill=X,padx=5)
f0=Frame(sk)
f1=Frame(f0,background="blue")
b1=Button(f1,text="1",font="lucida 40 bold",padx=20)
b1.pack(padx=5,pady=5)
b1.bind("<Button-1>",clicked)
b2=Button(f1,text="2",font="lucida 40 bold",padx=20)
b2.pack(padx=5,pady=5)
b2.bind("<Button-1>",clicked)
b3=Button(f1,text="3",font="lucida 40 bold",padx=20)
b3.pack(padx=5,pady=5)
b3.bind("<Button-1>",clicked)
b4=Button(f1,text="+",font="lucida 40 bold",padx=20)
b4.pack(padx=5,pady=5)
b4.bind("<Button-1>",clicked)
f1.pack(side=LEFT,anchor="nw")
f2=Frame(f0,background="blue")
b4=Button(f2,text="4",font="lucida 40 bold",padx=20)
b4.pack(padx=5,pady=5)
b4.bind("<Button-1>",clicked)
b5=Button(f2,text="5",font="lucida 40 bold",padx=20)
b5.pack(padx=5,pady=5)
b5.bind("<Button-1>",clicked)
b7=Button(f2,text="6",font="lucida 40 bold",padx=20)
b7.pack(padx=5,pady=5)
b7.bind("<Button-1>",clicked)
b8=Button(f2,text="*",font="lucida 40 bold",padx=25)
b8.pack(padx=5,pady=5)
b8.bind("<Button-1>",clicked)
f2.pack(side=LEFT,anchor="nw")
f3=Frame(f0,background="blue")
b9=Button(f3,text="7",font="lucida 40 bold",padx=20)
b9.pack(padx=5,pady=5)
b9.bind("<Button-1>",clicked)
b10=Button(f3,text="8",font="lucida 40 bold",padx=20)
b10.pack(padx=5,pady=5)
b10.bind("<Button-1>",clicked)
b11=Button(f3,text="9",font="lucida 40 bold",padx=20)
b11.pack(padx=5,pady=5)
b11.bind("<Button-1>",clicked)
b12=Button(f3,text="/ ",font="lucida 40 bold",padx=20)
b12.pack(padx=5,pady=5)
b12.bind("<Button-1>",clicked)
f3.pack(side=LEFT,anchor="nw")
f4=Frame(f0,background="blue")
b13=Button(f4,text=". ",font="lucida 40 bold",padx=20)
b13.pack(padx=5,pady=5)
b13.bind("<Button-1>",clicked)
b14=Button(f4,text="0",font="lucida 40 bold",padx=20)
b14.pack(padx=5,pady=5)
b14.bind("<Button-1>",clicked)
b15=Button(f4,text="c",font="lucida 40 bold",padx=20)
b15.pack(padx=5,pady=5)
b15.bind("<Button-1>",clicked)
b16=Button(f4,text="=",font="lucida 40 bold",padx=20)
b16.pack(padx=5,pady=5)
b16.bind("<Button-1>",clicked)
f4.pack(side=LEFT,anchor="nw")
f0.pack()
# sign=Label(sk,text="Created by: Shivkumar Chauhan ",font="ROMEN 30 bold",fg="black")
# sign.pack(anchor="se",fill=X)
sk.mainloop()