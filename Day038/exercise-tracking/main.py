# https://www.nutritionix.com/
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
# https://sheety.co/

import os
import requests
import datetime as dt

APP_ID = os.environ.get("NUTRITIONIX_ID")
API_KEY = os.environ.get("NUTRITIONIX_KEY")

weight: int = int(os.environ.get("MY_WEIGHT_KG"))
height: int = int(os.environ.get("MY_HEIGHT_CM"))
age: int = int(os.environ.get("MY_AGE"))

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/71d684f5126a1eb9125ebb3d27988875/udemyDay38MyWorkouts/workouts"

api_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": "0",
}


def get_exercise_stats(exercise):
    query_params = {
        "query": exercise,
        "gender": "female",
        "weight_kg": weight,
        "height_cm": height,
        "age": age,
    }

    with requests.post(url=exercise_endpoint, json=query_params, headers=api_header) as response:
        exercise_data = response.json()
        print(exercise_data)
        return exercise_data


def post_to_sheety(json_obj, exercise_time):
    data = json_obj["exercises"][0]
    # print(data)
    bearer_auth = {
        "authorization": "Bearer udemy_exercise",
    }

    sheety_params = {
        "workout": {
            "date": dt.datetime.today().strftime("%d/%m/%Y"),
            "time": exercise_time,
            "exercise": data["name"].title(),
            "duration": int(data["duration_min"]),
            "calories": round(float(data["nf_calories"]))
        }
    }

    with requests.post(url=sheety_endpoint, json=sheety_params, headers=bearer_auth) as response:
        print(response.text)


my_answer = input("Tell me which exercises you did: ")
exercise_stats = get_exercise_stats(my_answer)

post_to_sheety(exercise_stats, "8:32:00")
