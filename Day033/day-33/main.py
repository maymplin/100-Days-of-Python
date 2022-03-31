# https://docs.python-requests.org/en/latest/

# # Video 298 - Working with Responses: HTTP Codes, Exceptions & JSON Data
# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")  # returns HTTP code e.g. 200
# # print(response.status_code) # https://www.webfx.com/web-development/glossary/http-status-codes/
#
# response.raise_for_status()
#
# data = response.json()
# # print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# # https://www.latlong.net/Show-Latitude-Longitude.html
# iss_position = (latitude, longitude)

# Video 300 - Understand API Parameters: Match Sunset Times with the Current Time
# https://sunrise-sunset.org/api
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

MY_LATITUDE = 41.878113
MY_LONGITUDE = -87.629799
MY_LOCAL_UTC_OFFSET = -5


def parse_sunrise_sunset(time):
    return time.split("T")[1].split("+")[0]


def utc_to_my_local_time(utc_time):
    pass


parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()["results"]
sunrise_str = parse_sunrise_sunset(data["sunrise"])
sunset_str = parse_sunrise_sunset(data["sunset"])

time_now = datetime.now()

print(sunrise_str)
print(sunset_str)
print(time_now.hour)
