##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas as pd
from random import randint
import smtplib

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv

def check_birthdays():
    today = dt.datetime.today()
    df = pd.read_csv("birthdays.csv")
    friends = df.to_dict(orient="record")
    birthday_people = []

    for friend in friends:
        if friend["month"] == today.month and friend["day"] == today.day:
            birthday_people.append(friend)

    return birthday_people


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

def pick_letter(person):
    template_chosen = f"letter_templates/letter_{randint(1, 3)}.txt"

    with open(template_chosen, "r") as file:
        template = file.readlines()

    template[0] = template[0].replace("[NAME]", f"{person}")

    return ''.join(template)


# 4. Send the letter generated in step 3 to that person's email address.

def send_letter(recipient, letter):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="my_email@email.com", password="password")
        connection.sendmail(from_addr="my_email@email.com",
                            to_addrs=recipient,
                            msg=f"Subject:Happy Birthday!\n\n{letter}")


def birthday_wisher():
    birthday_today = check_birthdays()

    if len(birthday_today) > 0:
        for person in birthday_today:
            birthday_msg = pick_letter(person["name"])
            send_letter(person["email"], birthday_msg)


birthday_wisher()
