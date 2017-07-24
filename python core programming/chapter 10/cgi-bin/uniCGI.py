Code='UTF-8'

unocode_hello=u'''
hello!
\u00A1Hola!
\u4F60\u597D!
\u3063\u3093!
'''

# header='Content-Type:text/html;charset=utf-8'
# print(header)
# print(' \n\n')
print('Content-Type:text/html;charset=%s\r'%Code)
print('\r\n')

print('<html><head><title>unicose cgi Demo</title></head>')
print('<body>')
print(unocode_hello.encode(Code))
print('</body></html>')
