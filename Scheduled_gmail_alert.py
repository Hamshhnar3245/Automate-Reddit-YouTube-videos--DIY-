import os
import smtplib
import imghdr
import datetime as dt
import time
from email.message import EmailMessage

print("Starting GMAIL ALERT")

EMAIL_ADDRESS = '' # INSERT EMAIL ADDRESS!
EMAIL_PASSWORD = '' # PASSWORD OF THAT EMAIL ADDRESS!

msg = EmailMessage()

msg['Subject'] = 'RYT videos DIY'
msg['From'] = '' # INSERT EMAIL ADDRESS!
msg['To'] = 'abc@gmail.com' # where do you want to send it?

message = """
        Welcome to a stable public release of my RYTauto work. \n
        This repository will show you how to automate videos with your system yourself with minimal investment.
        """
msg.set_content(message)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("GMAIL ALERT HAS BEEN SENT!")

time.sleep(10)
