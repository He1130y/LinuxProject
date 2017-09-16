#!/usr/bin/python2

import cgi
import commands

print "Content-type: text/html"
print

ip=cgi.FormContent() ['ip'][0]
password=cgi.FormContent()  ['password'][0]
sname=cgi.FormContent()  ['sname'][0]


fh=open('../ansible/hosts','w')
fh.write("[software]\n"+ip+"	ansible_ssh_user=root	ansible_ssh_pass="+password)
fh.close()

myansible=  """
---
- hosts: software
  tasks:
     - package:
           name: {}
           state: present
""".format(sname)

fh=open('../ansible/software.yml','w')
fh.write(myansible)
fh.close()

installCheck=commands.getstatusoutput("sudo ansible-playbook  ../ansible/software.yml   -i  ../ansible/hosts")

if installCheck[0] == 0:
	print """
		<script>
			alert("Software installed successfully.");
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
		document.location='/admin.html'
	</script>
	"""

