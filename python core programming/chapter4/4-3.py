from time import *
import _thread as thread
loops=[4,2]

def loop(nloop,nsec,lock):
    print('start loop' ,nloop, 'at:',ctime())
    sleep(nsec)
    print('loop ',nloop,' end at:',ctime())
    lock.release()

def main():
    print('starting at:',ctime())
    locks=[]
    nloops=len(loops)
    for i in range(nloops):
        lock=thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in range(nloops):
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in range(nloops):
        while locks[i].locked():
            pass
    print('all done at:',ctime())
main()