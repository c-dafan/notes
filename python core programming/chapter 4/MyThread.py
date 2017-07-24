import threading
from time import ctime

class MyThread(threading.Thread):
    res=0
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def run(self):
        print('starting ',self.name,'at:',ctime())
        self.res=self.func(*self.args)
        print(self.name,'finished at:',ctime())
    def getresult(self):
        return self.res



