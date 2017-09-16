#!/usr/bin/python2

import cgi
import commands

print "Content-type: text/html"
print

ip=cgi.FormContent() ['serverip'][0]
password=cgi.FormContent()  ['serverpassword'][0]

#step 1 create host list 

fh=open('../ansible/hosts','w')
fh.write("[ssh]\n"+ip+"	ansible_ssh_user=root	ansible_ssh_pass="+password)
fh.close()

#step 2  create yml code 

myansible=  """
---
- hosts: ssh
  tasks:
     - package:
           name: openssh-clients
           state: present
     - service:
           name: sshd
           state: restarted
"""

fh=open('../ansible/ssh.yml','w')
fh.write(myansible)
fh.close()

#step 3 start service

setupCheck=commands.getstatusoutput("sudo ansible-playbook  ../ansible/ssh.yml   -i  ../ansible/hosts")

if setupCheck[0]==0:
	print """
		<script>
			alert("SSH server setup successfully.");
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
		document.location='/setup.html'
	</script>
	"""

