import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#define your email details
email_sender = "sender@gmail.com"
email_receiver = "receiver@gmail.com"
email_subject = "TEST MAIL FOR EMAIL AUTOMATION"
email_body = "Hello, This is the test mail for checking if the mail is automated or not."

#login credentials for sending the email
email_password = "app_password_here" #use app-specific password if you have 2FA

#setup the mime (Multipurpose Internet Mail Extensions)
message =MIMEMultipart()
message['from'] = email_sender
message['To'] = email_receiver
message['Subject'] = email_subject

#add body to email
message.attach(MIMEText(email_body, 'plain'))

#Establish a secure session with the SMTP server
try:
    #connect to gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #start TLS (Transport Layer Security)

    #login to the email account
    server.login(email_sender, email_password)

    #send the email
    server.send_message(message)

    print(f"Email sent successfully to {email_receiver}")
except Exception as e:
    print(f"error: {e}")
finally:
    server.quit()  #close the SMTP connection
