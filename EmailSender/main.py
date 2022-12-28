from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_sender = SENDER_MAIL
email_password = SENDER_MAIL_PASSWORD
email_receiver = RECEIVER_MAIL
subject = EMAIL_SUBJECT
body = EMAIL_BODY

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# images = ['IMG-20220619-WA0004.jpg']
#
# for image in images:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name
#
# em.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name )

# Adding a pdf file
documents = ['cv.pdf']
for document in documents:
    with open(document,'rb') as f:
        file_data = f.read()
        file_name = f.name

em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
