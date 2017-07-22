from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import sleep,ctime

lock=Lock()
Max=5
candytray=BoundedSemaphore(Max)
def refill():
    lock.acquire()
    print('refilling candy...'),
    try:
        candytray.release()
    except:
        print('full,skopping')
    else:
        print('ok')
    lock.release()

def buy():
    lock.acquire()
    print('buying candy...'),
    if candytray.acquire(False):
        print('ok')
    else:
        print('empty,skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))
def main():
    print('starting at:',ctime())
    nloops=randrange(2,6)
    print('the candy machine (full with %d bars)!'%Max)
    Thread(target=consumer,args=(randrange(nloops,nloops+Max+2),)).start()
    sleep(2)
    Thread(target=producer,args=(nloops,)).start()
@register
def _atexit():
    print('all done at:',ctime())
if __name__=='__main__':
    main()