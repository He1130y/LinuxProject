#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print 


choice = cgi.FormContent()['choice'][0]


if choice == 'create':
	print """
	<form action='/scripts/create.py' method='POST'>
		<title>Create Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>User Creation</h1>
		<h3>Enter the following : </h3>
		<div>
		Enter New User Name: <input type='text' name='name' />
		<br /><br />
		<input type='Submit'/>
		<br /><br /><br />
		<a href=/mainmenu.html>Home</a> <a href='/user.html'>Back</a>
	</form>
	"""
elif choice == 'delete':
	print """
		<form action='/scripts/delete.py/' method='POST'>
		<title>Delete Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>User Deletion</h1>
		<h3>Choose User: </h3>
		<div>
		<select name='name'>	
	"""
	for i in commands.getoutput("sudo cat /etc/passwd | grep bash$").split("\n"):
		print "<option>"+i.split(":")[0]+"</option>"
	print "</select>"
	print """
		<br /><br />
		<input type='Submit'/>
		<br /><br /><br />
		<a href=/mainmenu.html>Home</a>  <a href='/user.html'>Back</a>
		</div>
	</form>
	"""

elif choice == 'password':
	print """
		<form action='/scripts/password.py/' method='POST'>
		<title>Password Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>Update pasword</h1>
		<h3>Choose User: </h3>
		<div>
		<select name='name'>	
	"""
	for i in commands.getoutput("sudo cat /etc/passwd | grep bash$").split("\n"):
		print "<option>"+i.split(":")[0]+"</option>"
	print "</select>"
	print """
		<br /><br />
		Enter new password : <input type='password' name= 'newpassword'/>
		<br /><br />
		<input type='Submit'/>
		<br /><br /><br />
		<a href=/mainmenu.html>Home</a>  <a href='/user.html'>Back</a>
		</div>
	</form>
	"""

else : 
	print "Error"
