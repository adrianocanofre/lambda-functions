from datetime import date, timedelta
import smtplib
import os
import json

def send_email(event, context):
    email = event['email']
    response = {
    }
    try:
        remetente = ''
        assunto = ''
        text = ''
        msg = '\r\n'.join([
          'From: %s' % remetente,
          'To: %s' % email,
          'Subject: %s' % assunto,
          '',
          '%s' % text
        ])

        server = smtplib.SMTP('')
        server.starttls()
        server.login('', '')
        server.sendmail(remetente, email, msg)
        server.quit()
        response["statusCode"] = 200
        response["body"] = '{"status":true}'

        return response
    except Exception as ex:
        print(ex)
        response["statusCode"] = 403
        response["body"] = '{"status":false}'
        return response
