#!/usr/bin/python2

import os
import cgi
import commands

print "Content-Type: text/html"
print

cname = os.environ['HTTP_COOKIE']
ccmd = cgi.FormContent()['cmd'][0]
print "<pre>"
print commands.getoutput("sudo docker exec {0}  {1}".format(cname,ccmd))
print "</pre>"


