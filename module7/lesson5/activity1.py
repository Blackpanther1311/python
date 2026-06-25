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