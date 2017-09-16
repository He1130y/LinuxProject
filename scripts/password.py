#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

uname=cgi.FormContent() ['name'][0]
upassword=cgi.FormContent() ['newpassword'][0]

passStatus=commands.getstatusoutput("echo {1} | sudo passwd  {0}  --stdin".format(uname,upassword))

if passStatus[0]==0:
	print """
		<script>
			alert("Password changed successfully.");
		</script>
	"""
else:
	print """
		<script>
			alert("Faied.");
		</script>
	"""

print """"
	<script>
		document.location='/user.html'
	</script>
	"""
