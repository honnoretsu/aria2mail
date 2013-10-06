#-------------------------------------------------------------------------------
# Name:        aria2mail
# Purpose:
# 
# Author:      EV500B
#
# Created:     15/09/2013
# Copyright:   (c) EV500B 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python2.7

from inc.aria2 import *
from inc.mail import *
import ConfigParser
import logging

##Manage logging part
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = ConfigParser.ConfigParser()
parser.read("inc/config.ini")

def var():
  aria2_dir = parser.get("aria2",'dir')
  aria2_host = parser.get("aria2","host")
  aria2_ip = socket.gethostbyname(aria2_host)
  aria2_port = parser.get("aria2","port")
  aria2_user = parser.get("aria2","username")

  POP3_SERVER = parser.get("mail", "pop3")
  SMTP_SERVER = parser.get("mail", "smtp")
  SMTP_PORT = parser.get("mail", "smtp_port")
  username = parser.get("mail", "username")
  password = parser.get("mail", "password")

def main():
    var()
    if aria2.isOpen(aria2_ip, int(aria2_port)) == True :
       aria2.connect()
       logger.info("Aria2 connectivity: OK")
    else:
         print "Port %s inaccessible" % (aria2_port)
         logger.error('Could not connect to aria2 host: %s:%s', aria2_host, aria2_port)
         exit(1)
    pass

if __name__ == '__main__':
    main()
