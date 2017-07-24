import cgi

header='Content-Type:text:html\n\n'

formhtml='''
<html lang="en">
<head>

    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>Friend list for:<i>new user</i></h3>
    <form action="/cgi-bin/friendsB.py">
        <input type='hidden' name='action' value='action'>
        <b>enter your name</b>
        <input type="text" name="person" value="new user" size="15">
        <b>how many friends do you have?</b>
            %s
            <input type="submit"></form>
    </form>
</body>
</html>
'''

fradio='<INPUT TYPE="radio" name="howmany" value="%s" %s> %s\n'

def show():
    friends=[]
    for i in (0,10,25,50,100):
        checked=''
        if i==0:
            checked='checked'
        friends.append(fradio%(str(i),checked,str(i)))
    print('%s%s'%(header,formhtml%''.join(friends)))

reshtml='''<HTML><HEAD><TITLE>
Friends CGI Demo
</TITLE><HEAD>
<BODY>
<H3>FRiends list for:<I>%s</I></H3>
your name is:<B>%s</B><P>
your have<B>%s</B> friends
</BODY></HTML>'''

def doresults(who,howmany):
    print(header+reshtml%(who,who,howmany))

def process():
    form=cgi.FieldStorage()
    if 'person' in form:
        who=form['person'].value
    else:
        who='new user'
    if 'howmany' in form:
        howmany=form['howmany'].value
    else:
        howmany=0
    if 'action' in form:
        doresults(who,howmany)
    else:
        show()
if __name__=='__main__':
    process()