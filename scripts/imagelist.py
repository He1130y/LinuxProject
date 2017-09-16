#!/usr/bin/python2

import commands

print "Content-Type: text/html"
print

print "<title>Image Page</title>"
print "<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />"

print """
<script>
function u(iname)	
{
document.location='iremove.py?x=' + iname;
}
</script>
"""

print "<table border='10'>"

print "<tr><th>S.No.</th><th>OS</th><th>Version</th><th>Delete</th></tr>"

x=1
y=1
for i in commands.getoutput("sudo docker images").split("\n"):
	if y==1:
		y+=1
		pass
	else:
		j=i.split()
		print "<tr><td>"+str(x)+"</td><td>"+j[0]+"</td><td>"+j[1]+"</td><td><input value ='"+j[2]+ "' type='button' onclick='u(this.value)' /></td></tr>"
		x+=1

print "</table>"
print "<div>"
print "<br /><br /><br /><a href='/mainmenu.html'>Home</a> <a href='/docker.html'>Back</a>"
print "</div>"
