#! /usr/bin/python
# -*- coding: utf-8 -*-
# from .mailsender import MailSender
from email.mime.image import MIMEImage
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class MailSender(object):
    def __init__(self, username, password, server='smtp.gmail.com', port=587, use_tls=True):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.use_tls = use_tls


    def send(self, sender, recipients, subject, message_plain=None, message_html='', images=None):
        '''

        :param sender: str
        :param recipients: [str]
        :param subject: str
        :param message_plain: str
        :param message_html: str
        :param images: [{id:str, path:str}]
        :return: None
        '''

        msg_related = MIMEMultipart('related')

        msg_related['Subject'] = subject
        msg_related['From'] = sender
        msg_related['To'] = ', '.join(recipients)
        msg_related.preamble = 'This is a multi-part message in MIME format.'

        msg_alternative = MIMEMultipart('alternative')
        msg_related.attach(msg_alternative)

        plain_part = MIMEText(message_plain, 'plain')
        html_part = MIMEText(message_html, 'html')

        msg_alternative.attach(plain_part)
        msg_alternative.attach(html_part)

        if images:
            for image in images:
                with open(image['path'], 'rb') as f:
                    msg_image = MIMEImage(f.read())
                    msg_image.add_header('Content-ID', '<{0}>'.format(image['id']))
                    msg_related.attach(msg_image)

        # Sending the mail

        server = smtplib.SMTP('{0}:{1}'.format(self.server, self.port))
        try:
            if self.use_tls:
                server.starttls()

            server.login(self.username, self.password)
            server.sendmail(sender, recipients, message_html)

        finally:
            server.quit()

def emailTheBastard(context):
    username = 'epfl.international@gmail.com'
    password = 'rahulkrishnan123'
    sender = "CAPS"

    images = list()
    images.append({
        'id': 'logo',
        'path': '1.png'
    })
    
    string="<p>"+str(context["price"])+"<p>"
    print(string)
    # with open('template.html') as template_html, open('template.txt') as template_plain:
    #     message_html = template_html.read()
    #     message_plain = template_plain.read()
    mail_sender = MailSender(username, password)
    mail_sender.send(sender, ['d4rshik@gmail.com', 'prashant.iyer98@gmail.com'], 'Welcome to CAPS', message_html="", message_plain=string, images="")
