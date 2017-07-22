from time import *

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
    loop()
    loop1()
    print('all done at:',ctime())

main()