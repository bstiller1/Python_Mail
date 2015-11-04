#!/usr/bin/python

import cgi, os, sys
# Enable debugging
import cgitb; cgitb.enable()
# Setup form variable to get access to form fields
form = cgi.FieldStorage()
# Print HTML header
print("Content-Type: text/html")
print("") # Blank space important after header

# Show "Back" link to go back
back = "<br /><a href='javascript:history.go(-1);' title='Back'>Back</a>"

# Check form fields
try:
	fname = form["fname"].value
except KeyError:
	print("You did not submit your First Name")
	print(back)
	sys.exit(0)

try:
	lname = form["lname"].value
except KeyError:
	print("You did not submit your Last Name")
	print(back)
	sys.exit(0)

try:
	sender = form["sender"].value
except KeyError:
	print("You did not submit your Email Address")
	print(back)
	sys.exit(0)

try:
	message = form["message"].value
except KeyError:
	print("You did not submit your Message")
	print(back)
	sys.exit(0)	

# Build message for email message
content = "From: " + fname + " " + lname + " " + sender + "\n" + message

# Try to send Email
try:
	sendmail_location = "/usr/sbin/sendmail" # sendmail location
	p = os.popen("%s -t" % sendmail_location, "w")
	p.write("From: %s \n" % sender)
	p.write("To: %s\n" % "stiller.blake@gmail.com")
	p.write("Subject: Python Mail\n")
	p.write("\n") # blank line separating headers from body
	p.write(content)
	status = p.close()
	print("Email sent!")
except:
	print("Problem sending mail")
