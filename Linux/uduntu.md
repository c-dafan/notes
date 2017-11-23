
今天又比密码忘了，记录一下找回密码的过程


前面步骤
[查考这个博客](http://www.cnblogs.com/jefflee168/p/5583456.html)


在点击f10之后，进入了root，现在如果使用passwd修改密码，改的是root密码，但是ubuntu界面登录是没有root用户的，

输入 vim /etc/passwd
查看用户有那些，一般是最后一行

然后 passwd 用户名

输入修改密码就可以了