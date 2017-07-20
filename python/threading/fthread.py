import threading
import time

class myThread(threading.Thread):
    def __init__(self,id,name,q):
        threading.Thread.__init__(self)
        self.id=id
        self.q=q
        self.name=name
    def run(self):
        print ("开启线程：" + self.name)
        print_thirty(self.name, self.q)
        print ("退出线程：" + self.name)

def print_thirty(name,q):
    while stopflag:
        queueLock.acquire()
        if not len(q)==0:
            print(name+":"+str(q.pop()))
            queueLock.release()
        else:
            queueLock.release()
        # time.sleep(0.5)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
workQueue=list(range(30))
threads = []
threadID = 1
stopflag=True
queueLock = threading.Lock()
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
while not len(workQueue)==0:
    pass

stopflag=False

for t in threads:
    t.join()

print ("退出主线程")
