#!/usr/bin/python2


import cgi
import commands
print "Content-Type: text/html"
print

choice = cgi.FormContent()['choice'][0]

if choice == 'day':
         
         ans=commands.getoutput("date")
         dt=ans.split()
	 print """
		<html>
		<title>Day Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />

	"""
	 print "Today:  "+dt[0]

         print """
         <br/><br ><br />
         <a href=/mainmenu.html>Home</a>  <a href='/basic.html'>Back</a>
         </html>
         """

elif choice == 'date':
         
         ans=commands.getoutput("date")
         dt=ans.split()
	 print """
		<html>
		<title>Date Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />

	 """
	 print "Date: "+dt[1]+" "+dt[2]+" "+dt[5]

         print """
         <br/><br ><br />
         <a href=/mainmenu.html>Home</a>  <a href='/basic.html'>Back</a>
        
         """

elif choice == 'time':
         
         ans=commands.getoutput("date")
         dt=ans.split()
	 print """
		<html>
		<title>Time Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />

	 """
	 print "Time: "+dt[3]+" "+dt[4]

         print """
         <br/><br ><br />
         <a href=/mainmenu.html>Home</a>  <a href='/basic.html'>Back</a>
        
         """
elif choice == 'calender':
         cal=commands.getoutput("cal")
	 print """
		<html>
		<title>Calender Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />

	 """
	 print "<pre>"
         print cal
	 print "</pre>"
         print """
         
         <a href=/mainmenu.html>Home</a> <a href='/basic.html'>Back</a>
        
         """

elif choice == 'file':
         print """
         <form action='/scripts/file.py/' method='POST'>
		<title>File Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>File Operation</h1>
		<h3>Enter & select following : </h3>
		<div>
		Server_IP:<input name='server-ip'/>
		<br /><br />
		Password:<input type='password' name='password'/>
		<br/><br/>
                Enter File Name: <input type='text' name='filename' />
		<br /><br />
		<input type='radio' name='choice' value='create'> Create
		<br /><br />
		<input type='radio' name='choice' value='delete'> Delete
		<br /><br />
                <input type='Submit'/>
                <br /><br /><br />
                <a href='/mainmenu.html'>Home</a> <a href='/basic.html'>Back</a>
		</div>
        </form>
        """
 
         
elif choice == 'folder':
         print """
         <form action='/scripts/folder.py/' method='POST'>
		<title>folder Page</title>
		<link type= 'text/css'  rel= 'stylesheet'  href= '/stylesheet/stylesheet.css' />
		<h1>folder Operation</h1>
		<h3>Enter & select following : </h3>
		<div>
		Server_IP:<input name='server_ip'/>
		<br/><br/>
		Password:<input type='password' name='password'/>
		<br/><br/>
                Enter folder Name: <input type='text' name='foldername' />
		<br /><br />
		<input type='radio' name='choice' value='create'> Create
		<br /><br />
		<input type='radio' name='choice' value='delete'> Delete
		<br /><br />
                <input type='Submit'/>
                <br /><br /><br />
                <a href='/mainmenu.html'>Home</a> <a href='/basic.html'>Back</a>
		</div>
        </form>
        """
else:
	print "Error"
         


