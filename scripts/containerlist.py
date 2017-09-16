#!/usr/bin/python2

import commands

print "Content-Type: text/html"
print

print "<title>Image Page</title>"
print "<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />"


print """
<script>
function start(cname)	
{
document.location='dstart.py?x=' + cname;
}
function stop(cname)	
{
document.location='dstop.py?x=' + cname;
}
function u(cname)	
{
document.location='dremove.py?x=' + cname;
}
function shell(cname)	
{
document.location='dshell.py?x=' + cname;
}
</script>
"""

print "<table border='5'>"

print "<tr><th>S.No.</th><th>Image</th><th>Container</th><th>Status</th><th>Start</th><th>Stop</th><th>Remove</th><th>Shell</th></tr>"

x=1
y=1
for i in commands.getoutput("sudo docker ps -a").split("\n"):
	if y==1:
		y+=1
		pass
	else:
		j=i.split()
		cstatus = commands.getoutput("sudo docker inspect {} | jq '.[].State.Status'".format(j[-1]))
		print "<tr><td>"+str(x)+"</td><td>"+j[1]+"</td><td>"+j[-1]+"</td><td>"+cstatus+"</td><td><input value ='"+j[-1]+ "' type='radio' onclick='start(this.value)' /></td><td><input value ='"+j[-1]+ "' type='radio' onclick='stop(this.value)' /></td><td><input value ='"+j[-1]+ "' type='radio' onclick='u(this.value)' /></td><td><input value ='"+j[-1]+ "' type='radio' onclick='shell(this.value)' /></td></tr>"
		x+=1

print "</table>"

print "<div>"
print "<br /><br /><br /><a href='/mainmenu.html'>Home</a> <a href='/docker.html'>Back</a>"
print "</div>"
