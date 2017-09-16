#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

uname=cgi.FormContent() ['name'][0]

addStatus=commands.getstatusoutput("sudo useradd  {0}".format(uname))

if addStatus[0]==0 :
	print """
		<script>
			alert("User add successfully.");
		</script>
	"""
else:
	print """
		<script>
			alert("Failed.");
		</script>
	"""

print """"
	<script>
		document.location='/user.html'
	</script>
	"""
	

