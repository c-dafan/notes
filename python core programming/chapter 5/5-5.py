from functools import partial as pto
from tkinter import Tk,Button,X
# from tkinter.tix import Control
from tkinter.messagebox import showerror,showinfo,showwarning

WARN='warn'
CRIT='crit'
REGU='regu'

SIGNS={
    'do not enter':CRIT,
    'railroad crossing':WARN,
    '55\n speed limit':REGU,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'obe way':REGU,
}

critCB=lambda:showerror('Error','Error Button Pressed')
warnCB=lambda:showwarning('Warning', 'Warning Button Pressed!')
infoCB=lambda:showinfo('Info','Info Button Pressed')

top=Tk()
top.title('Rod Signs')
Button(top,text='quit',command=top.quit,bg='red',fg='white').pack(fill=X,expand=1)

MyButton=pto(Button,top)
CritButton=pto(MyButton,command=critCB,bg='white',fg='red')
WarnButton=pto(MyButton,command=warnCB,bg='goldenrod1')
ReguButton=pto(MyButton,command=infoCB,bg='white')

for eachsign in SIGNS:
    signType=SIGNS[eachsign]
    cmd='%sButton(text=%r%s).pack(fill=X,expand=True)'%(signType.title(),eachsign,'.upper()'if signType==CRIT else '.title()')
    eval(cmd)

top.mainloop()