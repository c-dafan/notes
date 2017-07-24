from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen,Request
from urllib.parse import urljoin
from time import sleep
from bs4 import BeautifulSoup,SoupStrainer

URLs=('http://python.org',
    'http://baidu.com',
)

def output(x):
    # print(set(x))
    print('\n'.join(sorted(set(x))))
    # sleep(0.01)

def simpleBS(url,f):
    output(urljoin(url,x['href']) for x in BeautifulSoup(f).findAll('a'))

def fasterBS(url,f):
    b=BeautifulSoup(f,parseOnlyThese=SoupStrainer('a')).findAll('a')
    output(urljoin(url,x['href']) for x in b)

def htmlparser(url,f):
    class AnchorParser(HTMLParser):
        def handle_starttag(self,tag, attrs):
            if tag!='a':
                return
            if not hasattr(self,'data'):
                self.data=[]
            for attr in attrs:
                if attr[0]=='href':
                    self.data.append(attr[1])
    parser=AnchorParser()
    parser.feed(f.read())
    output(urljoin(url,x)for x in parser.data)

def process(url,data):
    print('\n *** simpleBS')
    simpleBS(url,data)
    data.seek(0)
    print('\n*** fasterBS')
    fasterBS(url,data)
    data.seek(0)
    print('\n ***htmlparser')
    htmlparser(url,data)
    data.seek(0)

def main():
    for url in URLs:
        req=Request(url,headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'})
        f=urlopen(req)
        data=StringIO(f.read().decode())
        f.close()
        process(url,data)

if __name__=='__main__':
    main()