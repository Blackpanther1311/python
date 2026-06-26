from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Denomination Counter")
root.geometry("650x400")
root.configure(bg="light blue")

label=Label(root, text="hey,user!Welcom to Denomination Conter Application.",bg="light blue")
label.place(relx=0.5,y=340,anchor=CENTER)

def msg():
    msg=messagebox.showinfo("Alert","Do you want to calculater the denomination count?")
    if msg=="OK":
        topwin()

button=Button(root,text="Let,s Get started!", command=msg, bg="brown", fg="white")
button.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title("Denomination Calculater")
    top.configure(bg="light blue")
    top.geometry("600x350+50+50")

    label1=Label(top,text="Enter your amount",bg="light blue")
    entry=Entry(top)
    label2=Label(top,text="here are the number of notes for each denomination",bg="light blue")

    l1=Label(top, text="2000000",bg="light blue")
    l2=Label(top, text="50000",bg="light blue")
    l3=Label(top, text="10000",bg="light blue")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    
    def calculator():
        try:
            amount=int(entry.get())

            if amount < 0:
                raise ValueError
            
            note2000000 = amount // 2000000
            amount%=2000000
            note50000 = amount // 50000
            amount%=50000

            note10000 = amount // 10000
            
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000000))
            t2.insert(END,str(note50000))
            t3.insert(END,str(note10000))

        except ValueError:
            messagebox.showerror("Error","plese enter a valid positive whole number.")

    btn=Button(top,text="Calculate",command=calculator,bg ="white",fg="golden" )

    label1.place(x=230, y=50)

    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    label2.place(x=140, y=170)


    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)


    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

root.mainloop()