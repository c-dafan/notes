import threading
from time import sleep,ctime

loops=[4,2]

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print('start loop' ,nloop, 'at:',ctime())
    sleep(nsec)
    print('loop ',nloop,' end at:',ctime())

if __name__=='__main__':
    print('starting at :',ctime())
    threads=[]
    nloops=len(loops)
    for i in range(nloops):
        t=MyThread(loop,(i,loops[i]))
        threads.append(t)
    for i in range(nloops):
        threads[i].start()
    for i in range(nloops):
        threads[i].join()
    print('all done at:',ctime())

