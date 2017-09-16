#!/usr/bin/python2

import cgi
import commands
print "Content-Type: text/html"
print

activity = cgi.FormContent() ['activity'][0]

if activity == 'container':
	print """
		<form action='/scripts/container.py/' method='POST'>
		<title>Container Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>Container Creation</h1>
		<h3>Select an image:- </h3>
		<div>
		<select name='imagename'>	
		"""
	y=1
	for i in commands.getoutput("sudo docker images").split("\n"):
		if y == 1:	
			y+=1
			pass
		else:
			j=i.split()
			print "<option>"+j[0]+":"+j[1]+"</option>"
	print "</select>"
	print """
		<br /><br />
		Enter container name : <input type='text' name='cname'/>
		<br /><br />
		<input type='Submit'/>
		<br /><br /><br />
		<a href=/mainmenu.html>Home</a>  <a href='/docker.html'>Back</a>
		</div>
	</form>
	"""


elif activity == 'image':
	print """
		<form action='/scripts/image.py/' method='POST'>
		<title>Image Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>Image Creation</h1>
		<h3>Select a container:- </h3>
		<div>
		<select name='cname'>	
		"""
	y=1
	for i in commands.getoutput("sudo docker ps  -a").split("\n"):
		if y == 1:	
			y+=1
			pass
		else:
			j=i.split()
			print "<option>"+j[-1]+"</option>"
	print "</select>"
	print """
		<br /><br />
		Enter image name : <input type='text' name='iname'/>
		<br /><br />
		<input type='Submit'/>
		<br /><br /><br />
		<a href=/mainmenu.html>Home</a>  <a href='/docker.html'>Back</a>
		</div>
	</form>
	"""

else:
	print "Error"


