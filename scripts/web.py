#!/usr/bin/python2

import cgi
import commands

print "Content-type: text/html"
print

ip=cgi.FormContent() ['serverip'][0]
password=cgi.FormContent()  ['serverpassword'][0]
port=cgi.FormContent()  ['port'][0]
dirname=cgi.FormContent() ['dirname'][0]

#step 1  create host list

fh=open('../ansible/hosts','w')
fh.write("[web]\n"+ip+"	ansible_ssh_user=root	ansible_ssh_pass="+password)
fh.close()

#step 2 create conf file

conf= """
Listen {0}

documentroot /{1}

<directory /{1}>
require all granted
</directory> 

""".format(port,dirname)

fh=open('../ansible/my.conf','w')
fh.write(conf)
fh.close()

#step 3 create yml code

myansible=  """
---
- hosts: web
  tasks:
     - package:
           name: httpd
           state: present
     - copy:
           src: /webcontent/ansible/my.conf
           dest: /etc/httpd/conf.d
     - copy:
           src: /webcontent/index.html
           dest: /{0}/

     - service:
           name: httpd
           state: restarted
            
""".format(dirname)

fh=open('../ansible/web.yml','w')
fh.write(myansible)
fh.close()

#step 4 start service

setupCheck=commands.getstatusoutput("sudo ansible-playbook  ../ansible/web.yml   -i  ../ansible/hosts")

if setupCheck[0]==0:
	print """
		<script>
			alert("Web server setup successfully.");
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
