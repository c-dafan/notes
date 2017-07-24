import cgi
from urllib.parse import quote_plus


header='Content-Type:text:html\n\n'

url='/cgi-bin/friendsC.py'

errorhtml='''
<html>
    <head>
        <title>Friends cgi Demo</title>
    </head>
    <body>
        <h3>error</h3>
        <b>%s</b>
        <form>
            <input type="button" value="back" onclick="window.history.back()">
        </form>
    </body>
</html>'''
def showerror(error_str):
    print(header+errorhtml%(error_str))

formhtml='''
<html lang="en">
<head>

    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>Friend list for:<i>%s</i></h3>
    <form action="%s">
        <input type='hidden' name='action' value='edit'>
        <b>enter your name</b>
        <input type="text" name="person" value="%s" size="15">
        <b>how many friends do you have?</b>
            %s
            <input type="submit"></form>
    </form>
</body>
</html>
'''

fradio='<INPUT TYPE="radio" name="howmany" value="%s" %s> %s\n'

def showform(who,howmany):
    friends=[]
    for i in (0,10,25,50,100):
        checked=''
        if str(i)==howmany:
            checked='checked'
        friends.append(fradio%(str(i),checked,str(i)))
    print('%s%s'%(header,formhtml%(who,url,who,''.join(friends))))

reshtml='''<HTML><HEAD><TITLE>
Friends CGI Demo
</TITLE><HEAD>
<BODY>
<H3>FRiends list for:<I>%s</I></H3>
your name is:<B>%s</B><P>
your have<B>%s</B> friends

<a href="%s">here</a> to edit your data again. 
</BODY></HTML>'''

def doresults(who,howmany):
    newurl=url+'?action=reedit&person=%s&howmany=%s'%(quote_plus(who),howmany)
    print(header+reshtml%(who,who,howmany,newurl))

def process():
    error=''
    form=cgi.FieldStorage()
    if 'person' in form:
        who=form['person'].value
    else:
        who='new user'
    if 'howmany' in form:
        howmany=form['howmany'].value
    else:
        if 'action' in form and form['action'].value=='edit':
            error='please select number of friends.'
        else:
            howmany=0
    if not error:
        if 'action' in form and form['action'].value !='reedit':
            doresults(who,howmany)
        else:
            showform(who,howmany)
    else:
        showerror(error)

if __name__=='__main__':
    process()