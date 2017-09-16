#!/usr/bin/python2

import cgi

print "Content-Type: text/html"

cname = cgi.FormContent()['x'][0]

print "set-cookie: {}".format(cname)
print
print """

	<form action='drun.py' method='POST'>
		<title>Shell Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<textarea cols='50' rows:'10' name="cmd">		
		</textarea>	
		<br /><br />
		<input type='Submit'/>
		<div>
		<br /><br /><br /><br />
		<a href='/mainmenu.html'>Home</a> <a href='/docker.html'>Back</a>
		</div>
	</form>	
	"""
