#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

ServerIp=cgi.FormContent()['server_ip'][0]
Password=cgi.FormContent()['password'][0]
folderName = cgi.FormContent() ['foldername'][0]
choice = cgi.FormContent() ['choice'][0]

if choice== 'create':
	"""addfolder=commands.getstatusoutput("sudo mkdir /root/Desktop/{0}".format(folderName))"""
	addfolder=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} mkdir /root/Desktop/{2}".format(ServerIp,Password,folderName))

	if addfolder [0] == 0 :
        	print """
		<script>
			alert("folder created successfully.");
		</script>
		"""
	else:
		print """
			<script>
				alert("Failed.");
			</script>
			"""
elif choice== 'delete':
	"""delfolder=commands.getstatusoutput("sudo rmdir /root/Desktop/{0}".format(folderName))"""

	delfolder=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} rmdir /root/Desktop/{2}".format(ServerIp,Password,folderName))
	if delfolder [0] == 0 :
        	print """
		<script>
			alert("folder deleted successfully.");
		</script>
		"""
	else:
		print """
			<script>
				alert("Failed.");
			</script>
			"""

else:
	print "error"

print """"
	<script>
		document.location='/basic.html'
	</script>
	"""
