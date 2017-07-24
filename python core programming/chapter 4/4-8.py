from MyThread import MyThread
from time import ctime,sleep

def fib(x):
    sleep(0.01)
    if x<2:
        return 1
    return fib(x-2)+fib(x-1)

def fac(x):
    sleep(0.05)
    if x<2:
        return 1
    return x*fac(x-1)

funcs=[fib,fac]
n=12

def main():
    nfuncs=len(funcs)
    print('single thread start at:',ctime())
    for i in range(nfuncs):
        print('starting',funcs[i].__name__,'at',ctime())
        print(funcs[i](n))
        print(funcs[i].__name__,'finished at:',ctime())
    print('single thread end at:',ctime())

    threads=[]
    print('multiple threads starting at:',ctime())
    for i in range(nfuncs):
        t=MyThread(funcs[i],args=(n,),name=funcs[i].__name__)
        threads.append(t)
    for i in range(nfuncs):
        threads[i].start()
        pass

    for i in range(nfuncs):
        threads[i].join()
        print(threads[i].getresult())
    print('multiple threads end at:',ctime())

main()