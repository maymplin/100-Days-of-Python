import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
lat = 37.490115
lon = -122.200231

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

from_number = os.environ.get("TWILIO_PHONE_NUMBER")
dest_number = "+1234567890"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

with requests.get(OWM_ENDPOINT, params=weather_params) as response:
    response.raise_for_status()
    weather_data = response.json()
    # print(weather_data)

hourly_data = weather_data["hourly"][:12]
# print(hourly_data)

for hour in hourly_data:
    condition_dode = hour["weather"][0]["id"]
    if int(condition_dode) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Bring an ☔",
            from_=from_number,
            to=dest_number
        )
        print(message.status)
        break

print(message.sid)
