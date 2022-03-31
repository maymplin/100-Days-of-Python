import requests
from datetime import datetime
import smtplib
from threading import Timer
from time import sleep

# My location
MY_LAT = 41.878113      # Your latitude
MY_LONG = -87.629799    # Your longitude

# My email and password
MY_EMAIL = "me@here.com"
MY_PASSWORD = "password"

# Your position is within +5 or -5 degrees of the ISS position.

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def is_iss_overhead():
    # ISS position info
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude - MY_LAT <= abs(5) and iss_longitude - MY_LONG <= abs(5)


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour <= sunrise


def send_look_up_notification():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject: Look up! ISS is overhead\n\nDo you see it?")


# My alternate solution
def iss_notification():
    if is_iss_overhead() and is_dark():
        Timer(60.0, iss_notification).start()
        send_look_up_notification()


# Video 301 solution
while True:
    if is_iss_overhead() and is_dark():
        send_look_up_notification()
    sleep(60)
