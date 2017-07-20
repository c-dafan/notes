import threading
import os
import queue

path="D:/Users/a/Anaconda3/Lib"
class myThread(threading.Thread):
    def __init__(self,id,name,q):
        threading.Thread.__init__(self)
        self.q=q
        self.name=name
        self.id=id
    def run(self):
        print('线程开启')
        process_data(self.name,self.q)
        print('线程关闭')

def process_data(name,q):
    while stopflag:
        threadLock.acquire()
        if not q.empty():
            data=q.get()
            threadLock.release()
            print(name+":"+data)
        else:
            threadLock.release()
threadLock=threading.Lock()
filesname=os.listdir(path)
workqueue=queue.Queue(3000)
stopflag=True
threadnames=['Thread1','Thread2','Thread3']
threadid=1
threads=[]
for i in threadnames:
    # myThread(threadid,i,workqueue)
    threads.append(myThread(threadid,i,workqueue))
    threads[-1].start()
    threadid += 1

threadLock.acquire()
for file in filesname:
    workqueue.put(file)
threadLock.release()

while not workqueue.empty():
    pass
stopflag=False

for t in threads:
    t.join()
print ("退出主线程")