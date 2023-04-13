import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from keys import mailpass
from api_caller import yesterday

# Define sender and recipient email addresses
sender_email = 'dev.lucafungo@gmail.com'
recipient_email = 'alfieriluca91@gmail.com'

# Define message subject and body
subject = f'Political analisys from The Guardian, {yesterday}'
body = f"Hi there,\n\nPlease see file attached with the analisys of the articles from yesterday ({yesterday})\n\n\nUn bacione!\n\nLuca"

# Define the attachment file
attachment_file = f'{yesterday}sentiment_analysis.csv'

# Create a multipart message object and add sender, recipient, subject, and body
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body))

# Open the attachment file and add it to the message object
with open(attachment_file, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(attachment_file)[1][1:])
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_file))
    message.attach(attachment)

# Send the message using Gmail's SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, f'{mailpass}')
    smtp.send_message(message)
    print('Email sent!')