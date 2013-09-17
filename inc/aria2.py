#-------------------------------------------------------------------------------
# Name:        aria2
# Purpose:
# 
# Author:      EV500B
#
# Created:     15/09/2013
# Copyright:   (c) EV500B 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python2.7

import string
import xmlrpclib
import getpass
import sys
import socket
import config

aria2_dir = config.aria2['dir']
aria2_host = config.aria2['host']
aria2_ip = socket.gethostbyname(aria2_host)
aria2_port = config.aria2['port']
aria2_user = config.aria2['username']

def isOpen(address, port):
	s = socket.socket()
	print "Attempting to connect to %s on port %s" % (address, port)
	try:
		s.connect((address, port))
		print "Connected to %s on port %s" % (address, port)
		return True
	except socket.error, e:
		print "Connection to %s on port %s failed: %s" % (address, port, e)
		return False


def connect():
    global s
    aria2_password = raw_input("Aria2 password: ")
    try:
        s = xmlrpclib.ServerProxy('http://'+aria2_user+':'+aria2_password+"@"+aria2_ip+':'+str(aria2_port)+'/rpc')		## Connect to the aria2 daemon
        s.aria2.tellActive()
    except:
           print "Unexpected error:", sys.exc_info()[0]
           raise

def addUrl(url):
    if url == "" :
      url = raw_input("Url please: ")
    s.aria2.addUri([url],{'dir':aria2_dir})								## Self explained

def main():
    if isOpen(aria2_ip, int(aria2_port)) == True :
       connect()
    else:
         print "Port %s inaccessible" % (aria2_port)
         exit(1)
    addUrl("")
    pass

if __name__ == '__main__':
    main()
