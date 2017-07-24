import urllib

LOGIN=''
PASSWD=''
URL=''
REALM=''

def handler_version(url):
    from urllib.parse import urlparse
    hdlr=urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM,urlparse(url)[1],LOGIN,PASSWD)
    opener=urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req=urllib.request.Request(url)
    b64str=encodestring('%s:%s'%(LOGIN,PASSWD))[:-1]
    req.add_header("Authorization","Basic %s"%b64str)
    return req

for funcType in ('handler','request'):
    print("*** using %s:"%funcType)
    url=eval('%s_version'%funcType)(URL)
    f=urllib.request.urlopen(url)
    print(f.readline())
    f.close()