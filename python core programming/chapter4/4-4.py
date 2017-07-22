from time import *
import threading
loops=[4,2]

def loop(nloop,nsec):
    print('start loop' ,nloop, 'at:',ctime())
    sleep(nsec)
    print('loop ',nloop,' end at:',ctime())

def main():
    print('starting at:',ctime())
    locks=[]
    nloops=len(loops)
    threads=[]
    for i in range(nloops):
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in range(nloops):
        threads[i].start()
    for i in range(nloops):
        threads[i].join()
    print('all done at:',ctime())

if __name__=='__main__':
    main()