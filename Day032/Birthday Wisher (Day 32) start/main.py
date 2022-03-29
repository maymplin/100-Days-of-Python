# https://docs.python.org/3/library/smtplib.html

# # Video #289 - How to Send Emails with Python using SMTP
# # smtplib practice
#
# import smtplib
#
# MY_EMAIL = "my-mail@fictious-email.com"
# MY_PASSWORD = "fictious-password"
#
#
# # connection = smtplib.SMTP("smtp.gmail.com", 587)
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#
#     # https://support.google.com/accounts/answer/185833?hl=en
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,
#                         to_addrs="nobody@anywhere.com",
#                         msg="Subject:Test Message\n\nI hope you're having a lovely day.")
#
# # connection.close()

# Video #290 - Working with the datetime Module
# datetime practice
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2022, month=3, day=28, hour=17)
# print(date_of_birth)

# Video #291 - Challenge 1 - Send Motivational Quotes on Mondays via Email
# Motivational Quote Email App

import smtplib
import datetime as dt
from random import choice


def pick_random_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
    return choice(quotes)


def send_quote():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="test_user@test.com", password="test_password")
        connection.sendmail(from_addr="test_user@test.com", to_addrs="test_recipient@@test.com", msg=f"Subject:Start the Day Right\n\n{pick_random_quote()}")


def motivate():
    weekday = dt.datetime.now().weekday()

    if weekday == 0:
        send_quote()


motivate()
