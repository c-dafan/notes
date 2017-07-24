from time import *
import _thread as thread

def loop():
    print('start loop 0 at:',ctime())
    sleep(4)
    print('loop 0 end at:',ctime())

def loop1():
    print('start loop1 at :',ctime())
    sleep(3)
    print('end loop1 at:',ctime())

def main():
    print('starting at:',ctime())
    thread.start_new_thread(loop,())
    thread.start_new_thread(loop1,())
    sleep(6)  #如果没有这一步，主线程会直接运行结束
    print('all done at:',ctime())

main()