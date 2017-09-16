#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

uname=cgi.FormContent() ['name'][0]

deleteStatus=commands.getstatusoutput("sudo userdel  -r  {0}".format(uname))

if deleteStatus[0]==0:
	print """
		<script>
			alert("User delete successfully.");
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
	

