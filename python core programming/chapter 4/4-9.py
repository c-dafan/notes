from atexit import register
from re import compile

from time import ctime
from urllib.request import urlopen,Request,build_opener
from threading import Thread

REGEX=compile('#([\d,]+) in Books ')
AMZN='https://www.amazon.com/dp/'

ISBNS={
    '0132269937':'core python programming',
    '0132356139':'python web development with Django',
    '0137143419':'python fundamentals',
}

def getRanking(isbn):
    url='%s%s'%(AMZN,isbn)
    req = Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
    oper = urlopen(req)
    data = oper.read()
    # page=urlopen('%s%s'%(AMZN,isbn))
    # data=page.read()
    # page.close()
    oper.close()
    return REGEX.findall(data.decode())[0]

def _showRanking(isbn):
    print('-%r ranked %s'%(ISBNS[isbn],getRanking(isbn)))

def _main():
    print('At',ctime(),'on amazon')
    threads=[]
    for isbn in ISBNS:
        # _showRanking(isbn)
        t=Thread(target=_showRanking,args=(isbn,))
        threads.append(t)
    for i in range(len(ISBNS)):
        threads[i].start()
    for i in range(len(ISBNS)):
        threads[i].join()
@register
def _atexit():
    print('all done at:',ctime())
if __name__=='__main__':
    _main()