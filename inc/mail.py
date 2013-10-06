#-------------------------------------------------------------------------------
# Name:        mail
# Purpose:     Manage mail transactions (connect, send and receive)
#
# Author:      EV500B
#
# Created:     15/09/2013
# Copyright:   (c) EV500B 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python2.7
import poplib, email, getpass, string
import ConfigParser

parser = ConfigParser.ConfigParser()
parser.read("config.ini")

POP3_SERVER = parser.get("mail", "pop3")
SMTP_SERVER = parser.get("mail", "smtp")
SMTP_PORT = parser.get("mail", "smtp_port")
username = parser.get("mail", "username")
password = parser.get("mail", "password")

numMessages = int(0)

M = poplib.POP3_SSL

def connect():
    ## Connection to Email host
    global M
    M = poplib.POP3_SSL(POP3_SERVER)

    M.user(username)
    M.pass_(password)
    ## Connection done or failed

def check():
    return len(M.list()[1])
    
def email_process(numMessages):
    print "\nNew Messages found : Processing\n"
    for i in range(numMessages):
        print "=" * 40
        msg = M.retr(i+1)
        str = string.join(msg[1], "\n")
        mail = email.message_from_string(str)

        mail_from = mail["From"]
        mail_subject = mail["Subject"]

        print "From:", mail["From"]
        print "Subject:", mail["Subject"]
        print "Date:", mail["Date"]

        if mail.is_multipart():
                mail_message = mail.get_payload(0).get_payload()
        else:
                mail_message = mail.get_payload()
        print mail_message
        print "\n- - - - - EOF - - - - -\n"		## Email separator

def main():
    connect()
    
    numMessages = check()
    if numMessages > 0:
        email_process(numMessages)
    else:
        print "No new messages"
    M.quit()

    pass

if __name__ == '__main__':
    main()
