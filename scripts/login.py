#!/usr/bin/python2

import cgi

print "Content-Type: text/html"
#print

#print cgi.FormContent() 



userId=cgi.FormContent()['user'][0]
Password=cgi.FormContent() ['pass'][0]


auser="pythonsiers"
apass="linuxworld"

if userId == auser and Password == apass :
	print "location: /mainmenu.html"
	print
else :
	print "location: /retry.html"
	print 
