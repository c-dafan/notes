from random import randint
from time import sleep
from queue import Queue
from MyThread import MyThread

def writeQ(queue):
    print('producing object for Q...'),
    queue.put('xxx',1)
    print('size now',queue.qsize())

def readQ(queue):
    val=queue.get(1)
    print('consumed object from Q ... size now',\
    queue.qsize())

def writer (queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))
funcs=[writer,reader]
nfuncs=len(funcs)

def main():
    nloops=randint(2,5)
    q=Queue(32)
    threads=[]
    for i in range(nfuncs):
        t=MyThread(funcs[i],(q,nloops),funcs[i].__name__)
        threads.append(t)
    for i in range(nfuncs):
        threads[i].start()
    for i in range(nfuncs):
        threads[i].join()
    print('all Done')
if __name__=='__main__':
    main()
