# from tkinter import Tk
# from time import sleep
# from tkinter.messagebox import showwarning
# import win32com.client as win32

# warn=lambda app:showwarning(app,'exit?')
# Range=range(3,8)

# def ppoint():
#     app='PowerPoint'
#     ppt=win32.gencache.EnsureDispatch('%s.Application'%app)
#     pres=ppt.Presentations.Add()
#     pres.Visible=True
#     sl=pres.Slides.Add(1,win32.constants.ppLayoutText)
#     sleep(1)
#     sla=sl.Shapes[0].TextFrame.TextRange
#     sla.Text='Python-to-%s Demo'%app
#     sleep(1)
#     slb=sl.Shapes[1].TextFrame.TextRange
#     for i in Range:
#         slb.InsertAfter("line %d\r\n"%i)
#         sleep(1)

#     slb.InsertAfter("Th-th-th-that's all folks!")
#     warn(app)
#     pres.Close(False)
#     ppt.Application.Quit()

# if __name__=='__main__':
#     Tk().withdraw()
#     ppoint()