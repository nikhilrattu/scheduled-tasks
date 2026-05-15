# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import random
import smtplib
from email.message import EmailMessage
import os

now = dt.datetime.now()
current_day = now.weekday()


my_email = os.environ.get("MY_EMAIL")
password = os.environ.get('MY_PASSWORD')


with open('quotes.txt', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

quote = random.choice(lines)


msg = EmailMessage()
msg["Subject"] = 'Daily Quote'
msg["From"] = my_email
msg["To"] = my_email

msg.set_content(quote)


with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.send_message(msg=msg)
