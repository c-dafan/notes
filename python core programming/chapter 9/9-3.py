import io
import formatter
import http.client as httplib
import sys
import os
import urllib
import urllib.parse as urlparse
from html.parser import HTMLParser

class Retriever(object):
    __slots__=('url','file')
    def __init__(self,url):
        self.url,self.file=self.get_file(url)
    
    def get_file(self,url,default='index.html'):
        parsed=urllib.parse.urlparse(url)
        host=parsed.netloc.split('@')[-1].split(':')[0]
        filepath='%s%s'%(host,parsed.path)
        if not os.path.splitext(parsed.path)[1]:
            filepath=os.path.join(filepath,default)
        linkdir=os.path.isdir(filepath)
        if not os.path.isdir(linkdir):
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url,filepath
    def download(self):
        try:
            retval=urllib.request.urlretrieve(self.url,self.file)
        except (IOError,httplib.InvalidURL )as e:
            retval=(('*** "%s":%s'%(self.url,e)),)
        return retval
    def parse_links(self):
        f=open(self.file,'r')
        data=f.read()
        f.close()
        parse=HTMLParser()
        parse.feed(data)
        parse.close()
        return parse.anchorlist

class Crawler(object):
    count=0
    def __init__(self,url):
        self.q=[url]
        self.seen=set()
        parsed=urlparse.urlparse(url)
        host=parsed.netloc.split('@')[-1].split(':')[0]
        self.dom='.'.join(host.split('.')[-2:])
    def get_page(self,url,media=False):
        r=Retriever(url)
        fname=r.download()[0]
        if fname[0]=='*':
            print(fname,'... skipping parse')
            return
        Crawler.count+=1

        print('\n(',Crawler.count,')')
        print('URL:',url)
        print('File:',fname)

        self.seen.add(url)
        ftype=os.path.splitext(fname)[1]
        if ftype not in ('.htm','html'):
            return
        for link in r.parse_links():
            if link.startswith('mailto:'):
                print('...discarded ,mailto link')
                continue
            if not media:
                ftype=os.path.splitext(link)[1]
                if ftype in ('.mp3','.mp4'):
                    print('... discarded,media file')
                    continue
            if not link.startswith('http://'):
                link=urlparse.urljoin(url, link)
            print('*',link)
            if link not in self.seen:
                if self.dom not in link:
                    print('... discarded,not in domain')
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print('... new,added to Q')
                    else:
                        print('... discarded,already processed')
            else:
                print('... discarded,already processed')

    def go(self,media=False):
        while self.q:
            url=self.q.pop()
            self.get_page(url,media)

def main():
    if len(sys.argv)>1:
        url=sys.argv[1]
    else:
        try:
            url=input('Enter starting Url:')
        except (KeyboardInterrupt,EOFError):
            url=''
        if not url:
            return
        if not url.startswith('http://') and not url.startswith('ftp://'):
            url='http://%s/'%url
        robot=Crawler(url)
        robot.go()
if __name__=='__main__':
    main()