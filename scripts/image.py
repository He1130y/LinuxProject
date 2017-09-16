#!/usr/bin/python2


print "Content-Type: text/html"
print 


import cgi
import commands

cName = cgi.FormContent() ['cname'][0]
iName = cgi.FormContent() ['iname'][0]

creationStatus = commands.getstatusoutput("sudo  docker  commit {1}  {0}".format(iName,cName))
 


if creationStatus[0]==0:
	print """
		<script>
			alert("Image created successfully.");
		</script>
	"""
else:
	print """
		<script>
			alert("Image name already exists.");
		</script>
	"""

print """"
	<script>
		document.location='/docker.html'
	</script>
	"""
