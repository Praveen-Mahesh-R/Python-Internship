import random
import smtplib
from email.message import EmailMessage
import ssl

# Create SMTP object
s = smtplib.SMTP('smtp.gmail.com', 587)

# Generate OTP
otp = random.randrange(100000, 999999, 1)

# Define email sender
email_sender = 'xyz' #replace with sender email
email_password = 'xyz' #replace with sender password

# Get receiver email
email_receiver = input("Enter your email:")

# Set the subject and body of the email
subject = 'Heres your OTP'
bodytext = "Do not share this with anyone:\n\n"
body = bodytext + str(otp) 

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# Enter OTP to verify
print("Enter a 6 digit number:")
b = int(input())
if b == otp:
    print("OTP verified!")
else:
    print("Invalid OTP!")
