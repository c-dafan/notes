from threading import Thread,Lock,BoundedSemaphore,current_thread
from time import *
max=4
semaphore=BoundedSemaphore(max)
lock=Lock()
def loop(nsec):
    lock.acquire()
    semaphore.acquire()
    lock.release()
    print(current_thread(),'start at: ',ctime())
    sleep(nsec)
    semaphore.release()
    print('end at:',ctime())

n=7
from random import randrange
nsecs=[randrange(1,4) for i in range(7)]

def main():
    print('starting at:',ctime())
    
    for i in range(n):
        Thread(target=loop,args=(nsecs[i],)).start()
    

if __name__=='__main__':
    main()