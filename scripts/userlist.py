#!/usr/bin/python2


import commands


print "Content-Type: text/html"
print 

print "<title>Create Page</title>"
print "<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />"
print "<div>"
print "<table border='10'>"

print "<tr><th>S.No.</th><th>User Name</th></tr>"

x=1
for i in commands.getoutput("sudo cat /etc/passwd | grep bash$").split("\n"):
	print "<tr><td>"+str(x)+".</td><td>"+i.split(":")[0]+"</td></tr>"
	x+=1
	
print "</table>"

print """
	<br />
	<a href=/mainmenu.html>Home</a> <a href='/user.html'>Back</a>
	</div>
"""

