from datetime import date, timedelta
import smtplib
import os
import json

def send_email(event, context):
    email = event['email']
    response = {}
    try:
        sender_email = "my@gmail.com"  # Enter your address
        receiver_email = "your@gmail.com"  # Enter receiver address
        subject = ''
        text = ''
        msg = '\r\n'.join([
          'From: %s' % sender_email,
          'To: %s' % receiver_email,
          'Subject: %s' % subjet,
          '',
          '%s' % text
        ])

        server = smtplib.SMTP('')
        server.starttls()
        server.login('', '')
        server.sendmail(sender_email, receiver_email, msg)
        server.quit()
        response["statusCode"] = 200
        response["body"] = '{"status":true}'

        return response
    except Exception as ex:
        print(ex)
        response["statusCode"] = 403
        response["body"] = '{"status":false}'
        return response
