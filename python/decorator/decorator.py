
import time

def deco(func):
    def wrapper():
        starttime=time.time()
        func()
        endtime=time.time()
        print(endtime-starttime)
    return wrapper
@deco
def myfunc():
    print('myfunc starting')
    time.sleep(0.6)
    print('myfunc end')

def main():
    b=deco(myfunc)
    print(b.__name__)
    b()
    print(myfunc.__name__)

def main1():
    print(myfunc.__name__)
    myfunc()

def deco1(func):
    def wrapper(*args,**kwargs):
        starttime=time.time()
        func(*args,**kwargs)
        endtime=time.time()
        print(endtime-starttime)
    return wrapper

def deco2(arg=True):
    if arg:
        def _deco2(func):
            def wrapper(*args,**kwargs):
                starttime=time.time()
                func(*args,**kwargs)
                endtime=time.time()
                print(endtime-starttime)
            return wrapper
    else:
        def _deco2(func):
            return func
    return _deco2

@deco2(True)
def myfunc1(a,b):
    print('myfunc starting')
    time.sleep(0.6)
    print('myfunc end')
def main2():
    myfunc1(1,2)

# if __name__=='__main__':
#     main2()
# 内置装饰器
class Foo(object):
    def __init__(self,var):
        super(Foo,self).__init__()
        self._var=var
    @property
    def var(self):
        return self._var
    @var.setter
    def var(self,var):
        self._var=var

# foo=Foo('var 1')
# print(foo.var)
# foo.var='var 2'
# print(foo.var)
# 使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
# @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
# @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。

class A(object):  
    bar = 1  
    def foo(self):  
        print ('foo'  )
 
    @staticmethod  
    def static_foo():  
        print ('static_foo'  )
        print (A.bar  )
 
    @classmethod 
    def class_foo(cls):  
        print ('class_foo'  )
        print (cls.bar  )
        # cls().foo()  
  
A.static_foo()  
A.class_foo()  