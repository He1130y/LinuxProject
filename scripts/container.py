#!/usr/bin/python2

print "Content-Type: text/html"
print 

import cgi
import commands


imageName =cgi.FormContent() ['imagename'][0]
cName =cgi.FormContent() ['cname'][0]

cNameCheck = commands.getstatusoutput("sudo docker inspect {}".format(cName))

if cNameCheck[0]==0:
	print "{} container name already exists.".format(cName)
else :
	creationCheck = commands.getstatusoutput("sudo docker run -dit  --name {0}  {1}".format(cName,imageName))
	if creationCheck[0] == 0:
		print """
			<script>
				alert("Container lauched successfully.");
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
		document.location='/docker.html'
	</script>
	"""
	
