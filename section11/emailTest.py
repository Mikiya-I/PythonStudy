from email import message
from email.mime import multipart
from email.mime import text
import smtplib


smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxx@hotmail.com'
to_email = 'xxxx@hotmail.com'
username = 'xxxx@hotmail.com'
password = 'afdafafafa'

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
msg.set_content('test email')
msg['Subject'] = 'Test email subject'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('test email', 'plain'))
with open('emailTest.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'r')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()