import threading
from time import sleep,ctime

loops=[4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
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
        t=threading.Thread(target=ThreadFunc(loop,args=(i,loops[i])))
        threads.append(t)
    for i in range(nloops):
        threads[i].start()
    for i in range(nloops):
        threads[i].join()
    print('all done at:',ctime())

