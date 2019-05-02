#Import the libraries we need
#SMTPlib for interacting with SMTP servers and sending emails
import smtplib
#Getpass for getting our password without showing it to everyone
import getpass
# Ask the user for their username

def mail_notify(message):
    username = "epfl.international@gmail.com"
    # username = "tatanaveen18@gmail.com"
    #Ask the user for their password
    password = "rahulkrishnan123"
    # password = "naveenpassw0rd"
    session = smtplib.SMTP('smtp.gmail.com', 587)
    #Initiate connection to the server
    session.ehlo()
    #Start encrypting everything you're sending to the server
    session.starttls()
    #Log into the server by sending them our username and password
    session.login(username, password)
    #Define the recipient of the email
    recipient = "prashant.iyer98@gmail.com"
    #Enter the headers of the email
    headers = "\r\n".join(["from: " + username,
                        "subject: CAPS Digital",
                        "to: " + recipient,
                        "mime-version: 1.0",
                        "content-type: text/html"])
    #Enter the text of the body of the email
    body_of_email = message
    #Tie the headers and body together into the email's content
    content = headers + "\r\n\r\n" + body_of_email
    #Send the email!
    session.sendmail(username, recipient, content)
    #Close the connection to the SMTP server 
    session.quit()