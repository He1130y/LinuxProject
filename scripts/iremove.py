#!/usr/bin/python2


import cgi
import commands

print "Content-Type: text/html"
 
iname = cgi.FormContent()['x'][0]

iremoveStatus =commands.getstatusoutput("sudo docker rmi -f  {0}".format(iname))

if iremoveStatus[0] == 0:
	print "location: imagelist.py"
	print 
else:
	print 
	print "not removed"

