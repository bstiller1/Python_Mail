#!/usr/bin/python

import cgi, os, sys
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
#form = cgi.FieldStorage(keep_blank_values=1)

print("Content-Type: text/html")
print("")

try:
	value = form["fname"].value
except KeyError:
	print("You did not submit your First Name")
	sys.exit(0)

try:
	value = form["lname"].value
except KeyError:
	print("You did not submit your Last Name")
	sys.exit(0)

try:
	value = form["sender"].value
except KeyError:
	print("You did not submit your Email Address")
	sys.exit(0)

try:
	value = form["message"].value
except KeyError:
	print("You did not submit your Message")
	sys.exit(0)	
	
fname = form["fname"].value
lname = form["lname"].value
sender = form["sender"].value
message = form["message"].value
content = "From: " + fname + " " + lname + " " + sender + "\n" + message

try:
	sendmail_location = "/usr/sbin/sendmail" # sendmail location
	p = os.popen("%s -t" % sendmail_location, "w")
	p.write("From: %s\n" % sender)
	p.write("To: %s\n" % "stiller.blake@gmail.com")
	p.write("Subject: Python Mail\n")
	p.write("\n") # blank line separating headers from body
	p.write(content)
	status = p.close()
	print("Email sent!")
except:
	print("Problem sending mail")
