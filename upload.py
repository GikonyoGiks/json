import json
import os
import ftplib
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("test.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    #for i in range(1, 1001):
    for i in range(len(content)):
        print(content[i])
        a=json.loads(content[i])
        print(a['output'])
        file_name=a['output']
        print(a['email'])
        email=a['email']
        if os.path.isfile('{}.mp4'.format(file_name)):
            print("Success!")
            msg = MIMEMultipart()
            msg['From'] = 'apg@crealto.ch'
            msg['To'] = "marco@marcosomaini.ch"
            msg['Subject'] = 'File Upload Successful'
            message = 'Below is the link to your uploaded file \nhttp://visualsplus.ch/delivery/{} \nKind Regards\nMarco'.format(file_name)
            print(message)
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('mail.cyon.ch')
            # identify ourselves to smtp gmail client
            mailserver.ehlo()
            # secure our email with tls encryption
            mailserver.starttls()
            # re-identify ourselves as an encrypted connection
            mailserver.ehlo()
            mailserver.login('apg@crealto.ch', 'R9win8Qq5$')
            a=mailserver.sendmail('apg@crealto.ch','marco@marcosomaini.ch',msg.as_string())
            print(a)
            mailserver.quit()
            os.remove("/home/ubuntu/project/json/{}".format(file_name))
            print("File {} Removed!".format(file_name))
        else:
            print("Failure")
