from tkinter import Label,Button,END
from tkinter.tix import Tk,Control,ComboBox

top=Tk()

label=Label(top,text='Anmials(in pairs;min:pair,max:dozen)')
label.pack()

ct=Control(top,label='Number:',integer=True,max=12,min=2,value=3,step=2)
ct.label.config(font='Helvetival -14 bold')
ct.pack()

cb=ComboBox(top,label='Type:',editable=True)
for anmail in ('dog','cat','hamster','python'):
    cb.insert(END,anmail)
cb.pack()

qb=Button(top,text='quit',command=top.quit,bg='red',fg='white')
qb.pack()

top.mainloop()