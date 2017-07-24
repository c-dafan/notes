import cgi

reshtml='''Content-Type:text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo
</TITLE><HEAD>
<BODY>
<H3>FRiends list for:<I>%s</I></H3>
your name is:<B>%s</B><P>
your have<B>%s</B> friends
</BODY></HTML>'''

form=cgi.FieldStorage()
who=form['person'].value
howmany=form['howmany'].value
print(reshtml%(who,who,howmany))