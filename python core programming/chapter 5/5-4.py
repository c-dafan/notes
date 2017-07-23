from tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold'%scale.get())

top=Tk()

top.geometry('250x150')# 这是 字母x，不是乘号
label=Label(top,text='hello world',font='Helvetica -12 bold')
# label.config(font='Helvetica -%d bold'%40)
label.pack(fill=X, expand=1)
scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
# 
scale.set(12)
scale.pack(fill=X,expand=1)

quit=Button(top,text='quit',command=top.quit,\
    activeforeground='white',activebackground='red')

quit.pack()
mainloop()   