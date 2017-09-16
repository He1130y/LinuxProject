#!/usr/bin/python2

import cgi

print "Content-Type: text/html"


setupCh= cgi.FormContent() ['setup'][0]

if setupCh=='ssh':
	print"location: /ssh.html"
	print 
elif setupCh=='web':
        print"location: /web.html"
        print
elif setupCh=='nfs':
        print"location: /nfs.html"
        print
else:
	print "ERROR"


