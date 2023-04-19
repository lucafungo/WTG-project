import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from keys import mailpass
from api_caller import yesterday

# Define sender and recipient email addresses
sender_email = 'dev.lucafungo@gmail.com'
recipient_email = 'luca.alfieri@xandertalent.com'

# Define message subject and body
subject = f'Political analisys from The Guardian, {yesterday}'
body = f"Hi there,\n\nPlease see file attached with the analisys of the articles from yesterday ({yesterday})\n\n\nUn bacione!\n\nLuca"

# Define the attachment files
csv_attachment_file = f'{yesterday}sentiment_analysis.csv'
zip_attachment_file = f'{yesterday}.zip'
zip_attachment_file_ita = f'{yesterday}_italian.zip'

# Create a multipart message object and add sender, recipient, subject, and body
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body))

# Open the attachment files and add it to the message object
with open(csv_attachment_file, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(csv_attachment_file)[1][1:])
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(csv_attachment_file))
    message.attach(attachment)# Open the attachment file and add it to the message object
with open(zip_attachment_file, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(zip_attachment_file)[1][1:])
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(zip_attachment_file))
    message.attach(attachment)
with open(zip_attachment_file_ita, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(zip_attachment_file_ita)[1][1:])
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(zip_attachment_file_ita))
    message.attach(attachment)



# Send the message using Gmail's SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, f'{mailpass}')
    smtp.send_message(message)
    print(f'Email sent to {recipient_email}')
