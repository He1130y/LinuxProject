#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

ServerIp=cgi.FormContent()['server-ip'][0]
Password=cgi.FormContent()['password'][0]
fileName = cgi.FormContent() ['filename'][0]
choice = cgi.FormContent() ['choice'][0]

if choice == 'create':
	"""addFile=commands.getstatusoutput("sudo touch /root/Desktop/{0}".format(fileName))"""
	addFile=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} touch /root/Desktop/{2}".format(ServerIp,Password,fileName))
	if addFile [0] == 0 :
        	print """
		<script>
			alert("File created successfully.");
		</script>
		"""
	else:
		print """
			<script>
				alert("Failed.");
			</script>
			"""
elif choice== 'delete':
	"""delFile=commands.getstatusoutput("sudo rm /root/Desktop/{0}".format(fileName))"""
	delFile=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} rm /root/Desktop/{2}".format(ServerIp,Password,fileName))

	if delFile [0] == 0 :
        	print """
		<script>
			alert("File deleted successfully.");
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
