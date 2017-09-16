#!/usr/bin/python2


import cgi
import commands

print "Content-Type: text/html"

cname = cgi.FormContent()['x'][0]

cremoveStatus =commands.getstatusoutput("sudo docker rm -f  {0}".format(cname))

if cremoveStatus[0] == 0:
	print "location: containerlist.py"
	print 
else:
	print 
	print "not removed"

