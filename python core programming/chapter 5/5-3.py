import tkinter
top=tkinter.Tk()
label=tkinter.Label(top,text='hello world')
label.pack()

quit=tkinter.Button(top,text='quit',command=top.quit)

quit.pack(fill=tkinter.X,expand=1)


tkinter.mainloop()