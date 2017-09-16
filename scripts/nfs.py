#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print 

serverIp=cgi.FormContent() ['serverip'][0]
serverPass=cgi.FormContent() ['serverpassword'][0]
vgName=cgi.FormContent() ['vgname'][0]
lvName=cgi.FormContent() ['lvname'][0]
lvSize=cgi.FormContent() ['lvsize'][0]
fName=cgi.FormContent() ['fname'][0]
clientIP=cgi.FormContent() ['clientip'][0]

#step 1 check vg in nfs server system

vgCheck=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  vgdisplay {2}".format(serverIp,serverPass,vgName))
if vgCheck[0]!=0:
	print "{0} vg doesnt exist.".format(vgNamw)
	exit()
else:

#step 2  if there,  check for lv ...if not create  a lv 

	lvCheck=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} lvdisplay /dev/{2}/{3}".format(serverIp,serverPass,vgName))
	if lvCheck[0]==0:
		print "lv already"
	else:
		lvCreate=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} lvcreate --size {4}G --name {3} {2}".format(serverIp,serverPass,vgName,lvName,lvsize))
		if lvCreate[0]==0:
			print "lv of 1gb is created"
		else:
 			print "lv cnt made"

# step 3  format , create folder , mount

commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0] mkfs.ext4 /dev/{2}/{3}".format(serverIp,serverPass,vgName,lvName))

commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} mkdir -p /{3}/{2}".format(serverIp,serverPass,lvName,fName))

mountCheck=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/{2}/{3}  /{4}/{3}".format(serverIp,ser5verPass,vgName,lvName,fName))
if mountCheck[0]==0:
		print "Mount"
else:
		print "error"
#step 4 for permanent the mount

copyCheck=commands.getstatusoutput("sshpass -p {1} scp root@{0}:/etc/fstab   /mnt/fstab".format(serverIp,serverPass))
if copyCheck[0]==0:
	fstabString="/dev/{0}/{1}			/{2}/{1}     ext4	defaults 1 2".format(vgName,lvName,fName)
	fstabfh=open('/mnt/fstab' ,'a')
	fstabfh.write(fstabString+"\n")
	fstabfh.close()
	commands.getstatusoutput("sshpass -p {1} scp /mnt/fstab  root@{0}:/etc/fstab".format(serverIp,serverPass))
	fstabStatus=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} mount -a".format(serverIp,serverPass))
	if fstabStatus[0]==0:
		print"No error"
	else:
		print"Error"
else:
	print "error"

#step  5  provide clients for the server

copyCheck2=commands.getstatusoutput("sshpass -p {1} scp root@{0}:/etc/exports   /mnt/exports".format(serverIp,serverPass))
if copyCheck2[0]==0:
	shareLocation=("/{2}/{1}     {0}".format(clientIP,lvName,fName))
	nfsfh=open('/mnt/exports','a')
	nfsfh.write(shareLocation +'\n')
	nfsfh.close()
	commands.getstatusoutput("sshpass -p {1} scp /mnt/exports  root@{0}:/etc/exports".format(serverIp,serverPass))
	print "no error2"
else:
	print "error2"

#step 6  start service

startCheck=commands.getstatusoutput("systemctl restart nfs")
if startCheck[0]==0:
	print "Success"
else:
	print "End error"



